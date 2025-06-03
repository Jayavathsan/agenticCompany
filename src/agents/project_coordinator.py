# Project coordinator
from src.agents.base_agent import BaseAgent

class ProjectCoordinator(BaseAgent):
    def __init__(self, name, reports_to=None, tools=None):
        super().__init__(name=name, role="Project Coordinator", reports_to=reports_to, tools=tools)


    def perform_task(self, task):
        print(f"[Project Coordinator] {self.name}: {task}")
