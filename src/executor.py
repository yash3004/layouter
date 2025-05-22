import dataclasses

@dataclasses.dataclass
class ProjectInfo:
    name: str
    email: str
    project_name: str
    code_lang: str
    git_username: str
    description: str
    dependencies: list
    licence: str
    use_ci: bool
    ci: str = None


def take_info():
    print("welcome to the layouter")
    name = input("Enter Your Name (John Doe):")
    email = input("Enter Your Email (JohnDoe@email.com):")
    project_name = input("Enter Project Name :")
    code_lang = input("Enter Code Language (Go , Python , C/C++,...):")
    git_username = input("Enter Git Username:")
    description = input("Enter Description (What are u building):")
    dependencies = input(
        "Enter Dependencies (what tool/db u will use separated by comma):"
    )
    dependencies = dependencies.split(",")
    licence = input("Choose Licence: \nMIT:1\nApache:2\nGPL:3")
    use_ci = input("Do you want to use CI/CD? (y/n):")
    ci = None
    if use_ci == "n":
        use_ci = False
    if use_ci == "y":
        use_ci = True
        ci = input(
            "Choose CI/CD Tool: \nGithub Actions:1\nGitlab "
            "CI:2\nTravis CI:3\nCircle CI:4"
        )
        if ci == "1":
            ci = "github-actions"
        if ci == "2":
            ci = "gitlab-ci"
        if ci == "3":
            ci = "travis-ci"
        if ci == "4":
            ci = "circle-ci"

    return ProjectInfo(
        name,
        email,
        project_name,
        code_lang,
        git_username,
        description,
        dependencies,
        licence,
        use_ci,
        ci,
    )

