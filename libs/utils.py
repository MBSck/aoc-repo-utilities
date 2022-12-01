import os
import shutil
import getpass
import datetime

from pathlib import Path
from typing import Optional
from github import Github, AuthenticatedUser


REPO_NAME = f"advent-of-code-{datetime.datetime.now().year}"
ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")


def get_repo_dir(path: Optional[Path] = None) -> str:
    """Sets the (to be created) repo's path to the home path if not otherwise specified

    Parameters
    ----------
    repo_path: Path, optional

    Returns
    -------
    repo_path: str
    """
    parent_dir = os.environ["HOME"]\
            if ((not path) or (not os.path.exists(path))) else path
    return os.path.join(parent_dir, REPO_NAME)


def create_yaml(repo_dir: Path):
    """Creates a workflow file and directory if it does not exist

    Parameters
    ----------
    repo_dir: Path
    """
    workflow_dir = os.path.join(repo_dir, ".github/workflows")
    if not os.path.exists(workflow_dir):
        os.makedirs(workflow_dir)

    shutil.copy(os.path.join(ASSETS_DIR, "readme-stars.yml"),
                os.path.join(workflow_dir, "readme-stars.yml"))


def create_readme(repo_dir: Path, login: str) -> None:
    """Creates a workflow file and directory if it does not exist

    Parameters
    ----------
    repo_dir: Path
    """
    with open(os.path.join(ASSETS_DIR, "readme_template.md")) as in_file,\
            open(os.path.join(repo_dir, "README.md")) as out_file:
        out_file.write(f"{login}'s Advent of Code\n")

        for line in in_file:
            out_file.write(line)


def create_day_folders(repo_dir: Path) -> None:
    for number in range(1, 25):
        if number < 10:
            day_folder = f"Day-0{number}"
        else:
            day_folder = f"Day-{number}"

    day_dir = os.path.join(repo_dir, day_folder)

    if not os.path.exists(day_dir):
        os.makedirs(day_dir)


def create_repository(path: Optional[Path] = None) -> None:
    """Creates the local repository

    Parameters
    ----------
    path: Path, optional
        The path, where the repository should be created
    """
    repo_dir = get_repo_dir(path=path)
    if not os.path.exists(repo_dir):
        os.makedirs(repo_dir)
    create_yaml(repo_dir)
    create_readme(repo_dir)
    create_day_folders(repo_dir)
    return repo_dir


def github_login():
    """Logs the user into Github

    Returns
    -------
    user: AuthenticatedUser
        The login
    login: str
        The nickname of the Github-account
    """
    github_token = getpass.getpass("Enter your Github token: ")
    g = Github(login_or_token=github_token)
    user = g.get_user()

    # NOTE: Lazyload of the user -> Avoids errors and makes API work?! WTF?!
    login = user.login
    return user, login


def create_remote(user: AuthenticatedUser):
    """Gets a repo from Github or creates it

    Parameters
    ----------
    user: AuthenticatedUser
    repo_name: str
        The name of the repo

    Returns
    -------
    repo
    """
    try:
        repo = user.get_repo(REPO_NAME)
    except Exception:
        repo = user.create_repo(REPO_NAME)
    return repo


def create_github_secrets(repo, login: str):
    """Creates the secrets for the Github repo from user input

    Parameters
    ----------
    repo
    login: str
    """
    user_id = input("Enter your user-id. If left blank defaults to Github-username: ")
    user_id = login if not user_id else user_id
    session_id = input("Enter your session-id: ")
    leaderboard_id = input("Enter your leaderboard-id: ")

    repo.create_secret("AOC_USER_ID", user_id)
    repo.create_secret("AOC_LEADERBOARD_ID", leaderboard_id)
    repo.create_secret("AOC_SESSION", session_id)
    repo.create_secret("AOC_YEAR", str(datetime.datetime.now().year))


def setup_remote() -> None:
    """This sets the remote up for pushing"""
    user, login = github_login()
    repo = create_remote(user)
    create_github_secrets(repo, login)
    return repo


if __name__ == "__main__":
    print(get_repo_dir())
