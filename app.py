import streamlit as st
import asyncio
import traceback
from src.agents.hr_agent import hr_agent


# ===============================
# Async Wrapper
# ===============================

async def run_agent(user_input: str):
    response = await hr_agent.ainvoke({
        "messages": [
            {"role": "user", "content": user_input}
        ]
    })
    return response["messages"][-1].content


def run_async(user_input: str):
    try:
        return asyncio.run(run_agent(user_input))
    except RuntimeError:
        # Handles Streamlit event loop issue
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        return loop.run_until_complete(run_agent(user_input))


# ===============================
# Streamlit UI
# ===============================

st.set_page_config(
    page_title="Agentic AI HR Assistant",
    layout="centered"
)

st.title("Agentic AI HR Assistant")
st.markdown("Agentic AI HR system powered by MCP")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chat input
if prompt := st.chat_input("Ask HR something..."):
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Show assistant thinking
    with st.chat_message("assistant"):
        with st.spinner("Processing request..."):
            try:
                response = run_async(prompt)
                st.markdown(response)
                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )
            except Exception as e:
                error_msg = f"Error: {str(e)}"
                st.error(error_msg)
                traceback.print_exc()
