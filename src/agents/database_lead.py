# Database lead
from src.agents.base_agent import BaseAgent

class DatabaseLead(BaseAgent):
    def __init__(self, name, reports_to=None, tools=None):
        super().__init__(name=name, role="Database Lead", reports_to=reports_to, tools=tools)

