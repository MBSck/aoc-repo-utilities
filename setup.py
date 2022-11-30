import datetime
import getpass

try:
    from github import Github
except ImportError:
    print("Could not import module 'PyGithub'!")
    confirm = input("Do you want to install? (yN) ")
    if confirm.lower() == "y":
        try:
            import sys
            import subprocess
            subprocess.check_call([sys.executable, "-m", "pip", "install", "PyGithub"])
            subprocess.check_call(["clear"])
        except Exception as e:
            raise RuntimeError(e)
        else:
            print("Package PyGithub has been installed!")
    else:
        print("Please install PyGithub manually!")
        sys.exit()

    from github import Github


def get_user_input():
    """Gets the user input for the bash-script"""
    name = input("Enter your name: ")
    folder_name = f"advent-of-code-{datetime.date.year}"
    github_username = input("Enter your Github username: ")
    github_password = getpass.getpass("Enter your Github password: ")
    g = Github(github_username, github_password)
    user = g.get_user()
    print(user)

    return name, folder_name #, github_repo_ssh


def create_github_repo(g: Github):
    ...


if __name__ == "__main__":
    get_user_input()

