from langchain.tools import tool
from src.agents.mcp_bridge import MCPBridge

bridge = MCPBridge()

async def call_mcp(tool_name: str, arguments: dict):
    return await bridge.call_tool(tool_name, arguments)


# =========================
# Employee Tools
# =========================

@tool
async def add_employee(emp_name: str, manager_id: str, email: str) -> str:
    """Add a new employee to the HR system."""
    return await call_mcp("add_employee", {
        "emp_name": emp_name,
        "manager_id": manager_id,
        "email": email
    })


@tool
async def get_employee_details(name: str) -> str:
    """Get employee details by name."""
    return await call_mcp("get_employee_details", {
        "name": name
    })


# =========================
# Ticket Tools
# =========================

@tool
async def create_ticket(emp_id: str, item: str, reason: str) -> str:
    """Create a new IT ticket for an employee."""
    return await call_mcp("create_ticket", {
        "emp_id": emp_id,
        "item": item,
        "reason": reason
    })


@tool
async def update_ticket_status(ticket_id: str, status: str) -> str:
    """Update the status of an existing ticket."""
    return await call_mcp("update_ticket_status", {
        "ticket_id": ticket_id,
        "status": status
    })


@tool
async def list_tickets(emp_id: str, status: str = None) -> str:
    """List tickets for an employee, optionally filtered by status."""
    return await call_mcp("list_tickets", {
        "emp_id": emp_id,
        "status": status
    })


# =========================
# Meeting Tools
# =========================

@tool
async def schedule_meeting(emp_id: str, meeting_datetime: str, topic: str) -> str:
    """Schedule a meeting for an employee."""
    return await call_mcp("schedule_meeting", {
        "emp_id": emp_id,
        "meeting_datetime": meeting_datetime,
        "topic": topic
    })


@tool
async def get_meetings(emp_id: str) -> str:
    """Retrieve meetings scheduled for an employee."""
    return await call_mcp("get_meetings", {
        "emp_id": emp_id
    })


@tool
async def cancel_meeting(emp_id: str, meeting_datetime: str, topic: str) -> str:
    """Cancel a scheduled meeting for an employee."""
    return await call_mcp("cancel_meeting", {
        "emp_id": emp_id,
        "meeting_datetime": meeting_datetime,
        "topic": topic
    })


# =========================
# Leave Tools
# =========================
@tool
async def get_employee_leave_balance(emp_id: str) -> str:
    """Retrieve the leave balance for an employee."""
    return await call_mcp("get_employee_leave_balance", {
        "emp_id": emp_id
    })




@tool
async def apply_leave(emp_id: str, leave_dates: list) -> str:
    """Apply leave for specific dates for an employee."""
    return await call_mcp("apply_leave", {
        "emp_id": emp_id,
        "leave_dates": leave_dates
    })


# =========================
# Email Tool
# =========================

@tool
async def send_email(to_emails: list, subject: str, body: str, html: bool = False) -> str:
    """Send an email to one or more recipients."""
    return await call_mcp("send_email", {
        "to_emails": to_emails,
        "subject": subject,
        "body": body,
        "html": html
    })
