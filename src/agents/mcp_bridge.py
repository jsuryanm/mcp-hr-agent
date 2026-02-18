from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp.client.session import ClientSession
import os 
import sys 

"""bridge  allows langchain to call mcp tools via client 
and results are returned to langchain. 
in langchain we need to use @tool to call tools 
we cannot directly use the mcp tools 

"""

class MCPBridge:
    def __init__(self):
        server_path = os.path.abspath("server.py")
        # Capture the working directory at init time so the subprocess
        # can find .env, src/, emails.py, utils.py etc.
        self.project_root = os.path.dirname(server_path)

        print("Launching MCP Server at:", server_path)
        print("Working directory:", self.project_root)

        self.server_params = StdioServerParameters(
            command=sys.executable,
            args=[server_path],
            env={**os.environ},          # pass full env including .env vars
            cwd=self.project_root,       # ← THIS is the critical fix
        )

    async def call_tool(self, tool_name: str, arguments: dict):
        print("MCP CALL →", tool_name)
        print("ARGS →", arguments)

        async with stdio_client(self.server_params) as (read_stream, write_stream):
            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()   # ← ALSO required before any tool call

                result = await session.call_tool(tool_name, arguments)

                if result.isError:
                    raise Exception(f"MCP Tool Error: {result.content}")

                if isinstance(result.content, list) and len(result.content) > 0:
                    return result.content[0].text

                return str(result.content)