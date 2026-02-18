from mcp.server.fastmcp import FastMCP
from src.hrms.employee_manager import EmployeeManager
from src.hrms.ticket_manager import TicketManager
from src.hrms.meeting_manager import MeetingManager
from src.hrms.leave_manager import LeaveManager
from src.hrms.schemas import (
    EmployeeCreate, TicketCreate, TicketStatusUpdate,
    MeetingCreate, MeetingCancelRequest, LeaveApplyRequest,
)
from emails import EmailSender
from utils import seed_services
from datetime import datetime
from typing import List, Optional
import os
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP("atliq-hr-assistant")

employee_manager = EmployeeManager()
leave_manager = LeaveManager()
ticket_manager = TicketManager()
meeting_manager = MeetingManager()

seed_services(employee_manager, leave_manager, meeting_manager, ticket_manager)

emailer = EmailSender(
    smtp_server="smtp.gmail.com",
    port=587,
    username=os.getenv("CB_EMAIL"),
    password=os.getenv("CB_PASSWORD"),
    use_tls=True,
)

# ======================================================
# EMPLOYEE TOOLS
# ======================================================

@mcp.tool()
def add_employee(emp_name: str, email: str, manager_id: Optional[str] = None) -> str:
    emp = EmployeeCreate(
        emp_id=employee_manager.get_next_emp_id(),
        name=emp_name,
        manager_id=manager_id,
        email=email,
    )
    employee_manager.add_employee(emp)
    return f"Employee {emp_name} added successfully."


@mcp.tool()
def get_employee_details(name: str) -> str:
    matches = employee_manager.search_employee_by_name(name)
    if not matches:
        return f"No employees found with name {name}"
    emp_id = matches[0]
    return str(employee_manager.get_employee_details(emp_id))


# ======================================================
# TICKET TOOLS
# ======================================================

@mcp.tool()
def create_ticket(emp_id: str, item: str, reason: str) -> str:
    req = TicketCreate(emp_id=emp_id, item=item, reason=reason)
    return ticket_manager.create_ticket(req)


@mcp.tool()
def update_ticket_status(ticket_id: str, status: str) -> str:
    req = TicketStatusUpdate(status=status)
    return ticket_manager.update_ticket_status(req, ticket_id)


@mcp.tool()
def list_tickets(emp_id: str, status: Optional[str] = None) -> str:
    tickets = ticket_manager.list_tickets(employee_id=emp_id, status=status)
    if not tickets:
        return f"No tickets found for employee {emp_id}."
    formatted = [
        f"{t['ticket_id']} | {t['item']} | {t['status']} | Created: {t['created_at']}"
        for t in tickets
    ]
    return "\n".join(formatted)


# ======================================================
# MEETING TOOLS
# ======================================================

@mcp.tool()
def schedule_meeting(emp_id: str, meeting_datetime: str, topic: str) -> str:
    meeting_dt = datetime.fromisoformat(meeting_datetime)
    req = MeetingCreate(emp_id=emp_id, meeting_dt=meeting_dt, topic=topic)
    return meeting_manager.schedule_meeting(req)


@mcp.tool()
def get_meetings(emp_id: str) -> str:
    meetings = meeting_manager.get_meetings(emp_id)
    if not meetings:
        return f"No meetings found for {emp_id}."
    formatted = "\n".join([f"- {m['date']} | {m['topic']}" for m in meetings])
    return f"Meetings for {emp_id}:\n{formatted}"


@mcp.tool()
def cancel_meeting(emp_id: str, meeting_datetime: str, topic: Optional[str] = None) -> str:
    meeting_dt = datetime.fromisoformat(meeting_datetime)
    req = MeetingCancelRequest(emp_id=emp_id, meeting_dt=meeting_dt, topic=topic)
    return meeting_manager.cancel_meeting(req)


# ======================================================
# LEAVE TOOLS
# ======================================================

@mcp.tool()
def get_employee_leave_balance(emp_id: str) -> str:
    return leave_manager.get_leave_balance(emp_id)


@mcp.tool()
def apply_leave(emp_id: str, leave_dates: List[str]) -> str:
    parsed_dates = [datetime.fromisoformat(d).date() for d in leave_dates]
    req = LeaveApplyRequest(emp_id=emp_id, leave_dates=parsed_dates)
    return leave_manager.apply_leave(req)


# ======================================================
# EMAIL TOOL
# ======================================================

@mcp.tool()
def send_email(to_emails: List[str], subject: str, body: str, html: bool = False) -> str:
    emailer.send_email(
        subject=subject,
        body=body,
        to_emails=to_emails,
        from_email=emailer.username,
        html=html,
    )
    return "Email sent successfully."


if __name__ == "__main__":
    mcp.run(transport="stdio")