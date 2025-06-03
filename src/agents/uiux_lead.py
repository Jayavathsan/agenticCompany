# Uiux lead
from src.agents.base_agent import BaseAgent

class UiuxLead(BaseAgent):
    def __init__(self, name, reports_to=None, tools=None):
        super().__init__(name=name, role="Uiux Lead", reports_to=reports_to, tools=tools)


    def perform_task(self, task):
        print(f"[Uiux Lead] {self.name}: {task}")
