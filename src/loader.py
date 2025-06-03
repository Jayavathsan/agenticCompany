import yaml
from src.agents.base_agent import BaseAgent
# Import all agent classes (as shown in AGENT_CLASS_MAP above)
from src.agents.frontend_engineer import FrontendEngineer
from src.agents.backend_engineer import BackendEngineer
from src.agents.business_analyst import BusinessAnalyst
from src.agents.solution_architect import SolutionArchitect
from src.agents.system_designer import SystemDesigner
from src.agents.uiux_lead import UiuxLead
from src.agents.uiux_designer import UiuxDesigner
from src.agents.frontend_lead import FrontendLead
from src.agents.backend_lead import BackendLead
from src.agents.database_lead import DatabaseLead
from src.agents.database_engineer import DatabaseEngineer
from src.agents.ml_lead import MlLead
from src.agents.ml_engineer import MlEngineer
from src.agents.mlops_lead import MlopsLead
from src.agents.mlops_engineer import MlopsEngineer
from src.agents.devops_lead import DevopsLead
from src.agents.devops_engineer import DevopsEngineer
from src.agents.security_lead import SecurityLead
from src.agents.network_security_engineer import NetworkSecurityEngineer
from src.agents.qa_lead import QaLead
from src.agents.qa_engineer import QaEngineer
from src.agents.support_lead import SupportLead
from src.agents.support_engineer import SupportEngineer
from src.tasks.task import Task

AGENT_CLASS_MAP = {
    "frontend_engineer": FrontendEngineer,
    "backend_engineer": BackendEngineer,
    "business_analyst": BusinessAnalyst,
    "solution_architect": SolutionArchitect,
    "system_designer": SystemDesigner,
    "uiux_lead": UiuxLead,
    "uiux_designer": UiuxDesigner,
    "frontend_lead": FrontendLead,
    "backend_lead": BackendLead,
    "database_lead": DatabaseLead,
    "database_engineer": DatabaseEngineer,
    "ml_lead": MlLead,
    "ml_engineer": MlEngineer,
    "mlops_lead": MlopsLead,
    "mlops_engineer": MlopsEngineer,
    "devops_lead": DevopsLead,
    "devops_engineer": DevopsEngineer,
    "security_lead": SecurityLead,
    "network_security_engineer": NetworkSecurityEngineer,
    "qa_lead": QaLead,
    "qa_engineer": QaEngineer,
    "support_lead": SupportLead,
    "support_engineer": SupportEngineer,
}

def load_agents(yaml_path):
    with open(yaml_path, "r") as f:
        config = yaml.safe_load(f)
    agents = {}
    for a in config["agents"]:
        role = a["role"]
        cls = AGENT_CLASS_MAP.get(role, BaseAgent)
        agent = cls(
            name=a["name"],
            reports_to=a.get("reports_to"),
            tools=a.get("tools", [])
        )
        agents[a["name"]] = agent
    return agents

def load_tasks(yaml_path, agents):
    with open(yaml_path, "r") as f:
        config = yaml.safe_load(f)
    tasks = []
    for t in config["tasks"]:
        assigned_to = t["assigned_to"]
        if assigned_to not in agents:
            print(f"Warning: No agent with name '{assigned_to}' found. Skipping task '{t['description']}'.")
            continue
        agent = agents[assigned_to]
        task = Task(
            description=t["description"],
            assigned_to=agent.name,
            approval_required=t.get("approval_required", False)
        )
        agent.assign_task(task)
        tasks.append(task)
    return tasks
