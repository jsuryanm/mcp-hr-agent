# 🤖 MCP HR Agent

An **Agentic AI HR Assistant** built using **LangChain + MCP (Model
Context Protocol) + Streamlit** to automate HR operations like employee
onboarding, leave management, meeting scheduling, ticket handling, and
more.

------------------------------------------------------------------------

## 🚀 Features

### 👩‍💼 Employee Management

-   Get employee details
-   Check leave balance
-   Add new employees
-   Manager & employee hierarchy support

### 🗓️ HR Automation

-   Leave management
-   Meeting scheduling
-   Ticket handling
-   Email automation

### 🧠 Agentic AI

-   LangChain-groq reasoning agent (openai/gpt-oss-20b)
-   MCP tool calling
-   Modular architecture
-   Easy to extend tools

### 📊 Streamlit Dashboard

-   Chat with HR bot
-   Test employees & managers
-   Debug tool calls
-   Simple UI for demo

------------------------------------------------------------------------

## 🏗️ Architecture

User (Streamlit UI) 
    ↓ 
LangChain Agent 
    ↓ 
  MCP Client 
    ↓ 
  MCP Server (HR Tools) 
    ↓ 
  Database / Mock Data

------------------------------------------------------------------------

## 📂 Project Structure

```bash
mcp-hr-agent/
│
├── src/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── hr_agent.py
│   │   ├── hr_tools.py
│   │   ├── llm.py
│   │   └── mcp_bridge.py
│   │
│   ├── hrms/
│   │   ├── __init__.py
│   │   ├── employee_manager.py
│   │   ├── leave_manager.py
│   │   ├── meeting_manager.py
│   │   ├── ticket_manager.py
│   │   └── schemas.py
│   │
│   └── logger/
│       └── __init__.py
│
├── logs/
├── app.py
├── server.py
├── test_agent.py
├── emails.py
├── utils.py
├── template.py
├── setup.py
├── requirements.txt
├── LICENSE
├── README.md
├── .env
└── .gitignore
```
------------------------------------------------------------------------

## ⚙️ Installation
```bash
git clone https://github.com/jsuryanm/mcp-hr-agent.git\
cd mcp-hr-agent

conda create --name hr python=3.12
conda activate hr
pip install -r requirements.txt
```

------------------------------------------------------------------------

## ▶️ Running the Project

```bash
python server.py\
python test_agent.py\
streamlit run streamlit_app.py
```
------------------------------------------------------------------------

## 🧪 Testing

Example: get_employee_leave_balance(emp_id="E003")

------------------------------------------------------------------------

## Future improvements

-   Replace mock DB with PostgreSQL
-   Deploy MCP server with FastAPI
-   Add authentication
-   Deploy Streamlit on cloud

------------------------------------------------------------------------

## 🛠️ Tech Stack

Python, LangChain, Groq, MCP, Streamlit, Pydantic, AsyncIO

------------------------------------------------------------------------

## 👨‍💻 Author

Jayasuryan -- https://github.com/jsuryanm
