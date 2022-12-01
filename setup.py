import sys
import subprocess
import importlib.util


if importlib.util.find_spec("github") is None:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyGithub"])

if importlib.util.find_spec("git") is None:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "GitPython"])

subprocess.check_call(["clear"])


from libs.utils import create_repository, setup_remote, git_commit_and_push


def setup():
    login, github_token = setup_remote()
    repo_dir = create_repository(login)
    git_commit_and_push(repo_dir, github_token, login)


setup()

