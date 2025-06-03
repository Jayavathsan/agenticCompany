# Entrypoint main.py
from src.utils.config_loader import load_config, create_agents_from_config

def main():
    config = load_config("config.yaml")
    leads, teams = create_agents_from_config(config)

    print("\nOrg Structure:")
    for team_name, members in teams.items():
        print(f"Team: {team_name}")
        for member in members:
            print(f"  - {member}")

    # Example: Assign a task to FrontendEngineer
    fe_team = teams.get("frontend_engineers", [])
    if fe_team:
        fe_engineer = fe_team[0]
        fe_engineer.perform_task("Implement login page UI")

if __name__ == "__main__":
    main()

