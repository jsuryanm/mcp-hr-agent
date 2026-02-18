import asyncio
from mcp.client.stdio import stdio_client

class MCPBridge:
    def __init__(self,command="python server.py"):
        self.command = command 
    
    async def call_tool(self,tool_name: str,arguments: dict):
        async with 
        