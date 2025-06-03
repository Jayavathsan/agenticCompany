# Product owner
from src.agents.base_agent import BaseAgent

class ProductOwner(BaseAgent):
    def __init__(self, name, reports_to=None, tools=None):
        super().__init__(name=name, role="Product Owner", reports_to=reports_to, tools=tools)


    def perform_task(self, task):
        print(f"[Product Owner] {self.name}: {task}")
