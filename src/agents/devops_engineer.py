# Devops engineer
from src.agents.base_agent import BaseAgent

class DevopsEngineer(BaseAgent):
    def __init__(self, name, reports_to=None, tools=None):
        super().__init__(name=name, role="Devops Engineer", reports_to=reports_to, tools=tools)

    def perform_task(self, task):
        print(f"[Devops Engineer] {self.name}: {task}")
