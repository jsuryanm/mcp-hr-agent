from langchain.agents import create_agent
from src.agents.llm import get_llm 
from src.agents.hr_tools import (add_employee,
                                get_employee_details,
                                create_ticket,
                                update_ticket_status,
                                list_tickets,
                                schedule_meeting,
                                get_meetings,
                                get_employee_leave_balance,
                                apply_leave,
                                send_email)

llm = get_llm()

hr_agent = create_agent(model=llm,
                        tools=[add_employee,
                                get_employee_details,
                                create_ticket,
                                update_ticket_status,
                                list_tickets,
                                schedule_meeting,
                                get_meetings,
                                get_employee_leave_balance,
                                apply_leave,
                                send_email],
                        system_prompt="""
                        You are a strict HR system assistant.

                        You manage:
                        - Employees
                        - Tickets
                        - Meetings
                        - Leave
                        - Emails

                        Operational Rules:
                        1. You MUST use available tools for any factual, operational, or data-related request.
                        2. Do NOT answer from your own knowledge.
                        3. Do NOT fabricate employee IDs, balances, tickets, or meeting details.
                        4. If no relevant tool exists, respond exactly with:
                        "I do not have verified information to answer this."
                        5. If the query is outside the HR domain, respond exactly with:
                        "I can only assist with HR-related tasks."
                        6. If uncertain, do not guess. Use a tool or return the fallback message.
                        7. When onboarding a new employee, complete all required steps using tools before responding.""")