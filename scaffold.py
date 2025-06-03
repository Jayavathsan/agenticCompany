import os

base_dir = "src"

structure = {
    "agents": [
        "__init__.py",
        "business_analyst.py",
        "project_coordinator.py",
        "product_owner.py",
        "solution_architect.py",
        "system_designer.py",
        "uiux_lead.py",
        "uiux_designer.py",
        "frontend_lead.py",
        "frontend_engineer.py",
        "backend_lead.py",
        "backend_engineer.py",
        "database_lead.py",
        "database_engineer.py",
        "ml_lead.py",
        "ml_engineer.py",
        "mlops_lead.py",
        "mlops_engineer.py",
        "devops_lead.py",
        "devops_engineer.py",
        "security_lead.py",
        "network_security_engineer.py",
        "qa_lead.py",
        "qa_engineer.py",
        "support_lead.py",
        "support_engineer.py"
    ],
    "tools": [
        "__init__.py",
        "docker_code_tool.py",
        "github_tool.py",
        "figma_tool.py"
    ],
    "workflows": [
        "__init__.py",
        "requirement_intake.py",
        "architecture_design.py",
        "implementation.py",
        "qa_testing.py",
        "uat.py",
        "production_deploy.py",
        "support.py"
    ],
    "docs": [
        ".gitkeep"
    ],
}

root_files = [
    "main.py",
    "config.yaml",
    "README.md",
    "requirements.txt"
]

def create_structure():
    os.makedirs(base_dir, exist_ok=True)
    for folder, files in structure.items():
        dir_path = os.path.join(base_dir, folder)
        os.makedirs(dir_path, exist_ok=True)
        for f in files:
            file_path = os.path.join(dir_path, f)
            if not os.path.exists(file_path):
                with open(file_path, "w", encoding="utf-8") as fp:
                    if f.endswith(".py") and f != "__init__.py":
                        fp.write(f'# {f.replace("_", " ").capitalize().replace(".py", "")}\n')
                    elif f == "__init__.py":
                        fp.write("# package\n")
                    elif f == ".gitkeep":
                        fp.write("")
    for rf in root_files:
        if not os.path.exists(rf):
            with open(rf, "w", encoding="utf-8") as fp:
                if rf.endswith(".py"):
                    fp.write("# Entrypoint\n")
                elif rf.endswith(".yaml"):
                    fp.write("# Configurations\n")
                elif rf.endswith(".md"):
                    fp.write("# AgenticCompany\n")
                elif rf.endswith(".txt"):
                    fp.write("# Requirements\n")

if __name__ == "__main__":
    create_structure()
    print("Scaffold complete! 🚀")
