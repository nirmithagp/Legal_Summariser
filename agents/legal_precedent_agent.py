# agents/legal_precedent_agent.py
from crewai import Agent
from tools.legal_precedent_search_tool import legal_precedent_search_tool

legal_precedent_agent = Agent(
    name="Legal Precedent Agent",
    role="Legal assistant specialized in case law and legal precedents",
    goal="Provide relevant legal precedents for a user's query",
    backstory="Trained on Indian legal precedents and court cases",
    tools=[legal_precedent_search_tool]
)
