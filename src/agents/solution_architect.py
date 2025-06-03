# Solution architect
from src.agents.base_agent import BaseAgent

class SolutionArchitect(BaseAgent):
    def __init__(self, name, reports_to=None, tools=None):
        super().__init__(name=name, role="Solution Architect", reports_to=reports_to, tools=tools)


    def perform_task(self, task):
        print(f"[Solution Architect] {self.name}: {task}")


