# Network security engineer
from src.agents.base_agent import BaseAgent

class NetworkSecurityEngineer(BaseAgent):
    def __init__(self, name, reports_to=None, tools=None):
        super().__init__(name=name, role="Network Security Engineer", reports_to=reports_to, tools=tools)


    def perform_task(self, task):
        print(f"[Network Security Engineer] {self.name}: {task}")
