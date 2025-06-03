import yaml
import os
from src.agents.base_agent import BaseAgent
from src.agents.frontend_engineer import FrontendEngineer

ROLE_CLASS_MAP = {
    "Frontend Engineer": FrontendEngineer,
    # Expand as you implement more agent classes
}

def load_config(path="config.yaml"):
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} not found")
    with open(path, "r") as f:
        return yaml.safe_load(f)

def create_agents_from_config(config):
    org = config["organization"]
    leads = {}
    for k, v in org["leads"].items():
        agent = BaseAgent(name=v, role=k.replace("_", " ").title(), reports_to="Project Coordinator" if k != "project_coordinator" else "Owner")
        leads[k] = agent

    teams = {}
    for team_name, info in org["teams"].items():
        members = []
        for i in range(info["count"]):
            role = team_name[:-1].replace("_", " ").title()
            name = f"{role} {i+1}"
            reports_to_key = info["reports_to"]
            reports_to_agent = leads.get(reports_to_key)
            cls = ROLE_CLASS_MAP.get(role, BaseAgent)
            if cls is BaseAgent:
                member = cls(name=name, role=role, reports_to=reports_to_agent.name if reports_to_agent else None)
            else:
                member = cls(name=name, reports_to=reports_to_agent.name if reports_to_agent else None)

            members.append(member)
        teams[team_name] = members

    return leads, teams
