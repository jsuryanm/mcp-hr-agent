import os 
from pathlib import Path 
import logging 

logging.basicConfig(level=logging.INFO,format="[%(asctime)s]: %(message)s")

project_name = "hrms"

list_of_files = [
    "setup.py",
    "requirements.txt",
    "src/__init__.py",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/employee_manager.py",
    f"src/{project_name}/leave_manager.py",
    f"src/{project_name}/meeting_manager.py",
    f"src/{project_name}/schemas.py",
    f"src/{project_name}/ticket_manager.py",
    f"src/agents/__init__.py",
    f"src/agents/hr_agent.py",
    f"src/agents/hr_tools.py",
    f"src/agents/llm.py",
    f"src/agents/mcp_bridge.py",
    f"src/agents/llm.py",
    "src/logger/__init__.py",
    "emails.py",
    "server.py",
    "app.py",
    "utils.py"
] 

for filepath in list_of_files:
    filepath = Path(filepath)

    filedir,filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file {filename}")

    if (not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath,"w") as f:
            pass 
            logging.info(f"Creating empty file: {filename}")

    else:
        logging.info(f"{filename} is already created") 