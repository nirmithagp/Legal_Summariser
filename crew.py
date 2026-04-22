
# crew.py

from crewai import Crew
from agents.ipc_section_agent import ipc_section_agent
from agents.legal_precedent_agent import legal_precedent_agent

legal_assistant_crew = Crew(
    name="Legal Assistant Crew",
    agents=[ipc_section_agent, legal_precedent_agent]

)

