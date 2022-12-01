import os
import sys
import shutil
import datetime
import subprocess
import importlib.util


if importlib.util.find_spec("github") is None:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyGithub"])
    print("Package PyGithub has been installed!")

subprocess.check_call(["clear"])

from github import Github


def get_user_input_for_install(folder_name):
    """Gets the user input for the bash-script"""
    import getpass

    name = input("Enter your name: ")
    github_token = getpass.getpass("Enter your Github token: ")
    g = Github(login_or_token=github_token)
    user = g.get_user()

    # NOTE: Lazyload of the user -> Avoids errors and makes API work?! WTF?!
    login = user.login

    try:
        repo = user.get_repo(folder_name)
    except Exception:
        repo = user.create_repo(folder_name)

    return name, login, repo


def create_secrets_and_write_yaml(year, folder_name, login, repo):
    user_id = input("Enter your user-id. If left blank defaults to Github-username: ")
    user_id = login if not user_id else user_id
    session_id = input("Enter your session-id: ")
    leaderboard_id = input("Enter your leaderboard-id: ")

    repo.create_secret("AOC_USER_ID", user_id)
    repo.create_secret("AOC_LEADERBOARD_ID", leaderboard_id)
    repo.create_secret("AOC_SESSION", session_id)
    repo.create_secret("AOC_YEAR", str(year))

    workflow_dir = os.path.join("..", folder_name, ".github/workflows")
    if not os.path.exists(workflow_dir):
        os.makedirs(workflow_dir)

    shutil.copy("readme-stars.yml", os.path.join(workflow_dir, "readme-stars.yml"))


def call_setup_bash():
    year = datetime.datetime.now().year
    folder_name = f"advent-of-code-{year}"
    name, login, repo = get_user_input_for_install(folder_name)
    subprocess.run(["bash", "create_repo.sh", name, folder_name], check=True)
    create_secrets_and_write_yaml(year, folder_name, login, repo)
    subprocess.run(["bash", "git_push.sh", "../"+folder_name, repo.ssh_url], check=True)


if __name__ == "__main__":
    call_setup_bash()

