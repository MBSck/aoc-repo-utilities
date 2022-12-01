import importlib.util


if importlib.util.find_spec("github") is None:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyGithub"])
    print("Package PyGithub has been installed!")
    subprocess.check_call(["clear"])


import os
import sys
import subprocess

from libs.utils import create_repository, setup_remote, git_commit_and_push


def setup():
    repo, login = setup_remote()
    repo_dir = create_repository(login)
    git_commit_and_push(repo_dir, repo.ssh_url)


setup()

