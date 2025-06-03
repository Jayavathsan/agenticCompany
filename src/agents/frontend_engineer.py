# Frontend engineer
from src.agents.base_agent import BaseAgent

class FrontendEngineer(BaseAgent):
    def __init__(self, name, reports_to=None, tools=None):
        super().__init__(name=name, role="Frontend Engineer", reports_to=reports_to, tools=tools)

    def perform_task(self, task):
        print(f"[Frontend] {self.name}: {task}")
        # Future: Add LLM/tool calls here
