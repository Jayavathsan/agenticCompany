# Frontend lead
from src.agents.base_agent import BaseAgent

class FrontendLead(BaseAgent):
    def __init__(self, name, reports_to=None, tools=None):
        super().__init__(name=name, role="Frontend Lead", reports_to=reports_to, tools=tools)


    def perform_task(self, task):
        print(f"[Frontend Lead] {self.name}: {task}")
