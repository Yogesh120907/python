"""
Experiment 30: Clone an existing Python project repository, modify a source file,
track modifications using Git commits, create a development branch, and merge into main.
"""
import os
import subprocess
import tempfile


def run(cmd, cwd):
    print(f"$ {' '.join(cmd)}")
    res = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, check=True)
    if res.stdout.strip():
        print(res.stdout.strip())


with tempfile.TemporaryDirectory() as workspace:
    origin_repo = os.path.join(workspace, "remote_project.git")
    seed_repo = os.path.join(workspace, "seed")
    cloned_repo = os.path.join(workspace, "cloned_project")

    os.makedirs(seed_repo)
    run(["git", "init", "--bare", "-b", "main", origin_repo], workspace)
    run(["git", "init", "-b", "main"], seed_repo)
    run(["git", "config", "user.name", "Lab Student"], seed_repo)
    run(["git", "config", "user.email", "student@example.com"], seed_repo)
    with open(os.path.join(seed_repo, "calculator.py"), "w") as f:
        f.write("def add(a, b):\n    return a + b\n")
    run(["git", "add", "calculator.py"], seed_repo)
    run(["git", "commit", "-m", "Add initial calculator.py"], seed_repo)
    run(["git", "remote", "add", "origin", origin_repo], seed_repo)
    run(["git", "push", "-u", "origin", "main"], seed_repo)

    run(["git", "clone", origin_repo, cloned_repo], workspace)
    run(["git", "config", "user.name", "Lab Student"], cloned_repo)
    run(["git", "config", "user.email", "student@example.com"], cloned_repo)

    with open(os.path.join(cloned_repo, "calculator.py"), "a") as f:
        f.write("\ndef subtract(a, b):\n    return a - b\n")
    run(["git", "diff"], cloned_repo)
    run(["git", "commit", "-am", "Add subtract function to calculator.py"], cloned_repo)

    run(["git", "checkout", "-b", "dev"], cloned_repo)
    with open(os.path.join(cloned_repo, "calculator.py"), "a") as f:
        f.write("\ndef multiply(a, b):\n    return a * b\n")
    run(["git", "commit", "-am", "Add multiply function on dev branch"], cloned_repo)

    run(["git", "checkout", "main"], cloned_repo)
    run(["git", "merge", "dev", "--no-ff", "-m", "Merge dev branch into main"], cloned_repo)
    run(["git", "log", "--oneline", "--graph", "--all"], cloned_repo)
