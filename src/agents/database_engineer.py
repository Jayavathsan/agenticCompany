# Database engineer
from src.agents.base_agent import BaseAgent

class DatabaseEngineer(BaseAgent):
    def __init__(self, name, reports_to=None, tools=None):
        super().__init__(name=name, role="Database Engineer", reports_to=reports_to, tools=tools)

    def perform_task(self, task):
        print(f"[Database Engineer] {self.name}: {task}")  



