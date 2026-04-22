# agents/ipc_section_agent.py
from crewai import Agent
from tools.ipc_sections_search_tool import ipc_sections_search_tool

ipc_section_agent = Agent(
    name="IPC Section Agent",
    role="Legal assistant specialized in Indian Penal Code sections",
    goal="Provide accurate IPC sections for a user's legal queries",
    backstory="Trained on IPC knowledge base and legal documents",
    tools=[ipc_sections_search_tool]
)
