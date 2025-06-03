# Qa engineer
from src.agents.base_agent import BaseAgent

class QaEngineer(BaseAgent):
    def __init__(self, name, reports_to=None, tools=None):
        super().__init__(name=name, role="Qa Engineer", reports_to=reports_to, tools=tools)


    def perform_task(self, task):
        print(f"[Qa Engineer] {self.name}: {task}")
    