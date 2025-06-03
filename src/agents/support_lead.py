# Support lead
from src.agents.base_agent import BaseAgent

class SupportLead(BaseAgent):
    def __init__(self, name, reports_to=None, tools=None):
        super().__init__(name=name, role="Support Lead", reports_to=reports_to, tools=tools)


    def perform_task(self, task):
        print(f"[Support Lead] {self.name}: {task}")
