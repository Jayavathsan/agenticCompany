class BaseAgent:
    def __init__(self, name, role, reports_to=None, tools=None):
        self.name = name
        self.role = role
        self.reports_to = reports_to
        self.tools = tools or []
        self.team = []

    def add_team_member(self, agent):
        self.team.append(agent)

    def __repr__(self):
        return f"{self.role}('{self.name}', reports_to='{self.reports_to}')"

    def perform_task(self, task):
        print(f"{self.name} performing task: {task}")
