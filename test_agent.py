import asyncio
import traceback
from src.agents.hr_agent import hr_agent


async def main():
    print("HR Agent Test Started\n")

    response = await hr_agent.ainvoke({
        "messages": [
            {"role": "user", "content": "Check leave balance of E003"}
        ]
    })

    print(response['messages'][-1].content)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception:
        traceback.print_exc()
