import importlib.util


if importlib.util.find_spec("github") is None:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyGithub"])
    print("Package PyGithub has been installed!")
    subprocess.check_call(["clear"])


import sys
import subprocess

from libs.utils import create_repository, setup_remote


def setup():
    repo_dir = create_repository()
    repo = setup_remote()
    subprocess.run(["bash", "assets/git_push.sh", repo_dir, repo.ssh_url], check=True)


setup()

