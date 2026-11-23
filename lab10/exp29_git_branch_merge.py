"""
Experiment 29: Create a Git repository and perform version control operations
including commit, branch creation, and merging.
"""
import os
import subprocess
import tempfile


def run(cmd, cwd):
    print(f"$ {' '.join(cmd)}")
    res = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, check=True)
    if res.stdout.strip():
        print(res.stdout.strip())


with tempfile.TemporaryDirectory() as repo_dir:
    print(f"Initialized sandbox repository at: {repo_dir}\n")
    run(["git", "init", "-b", "main"], repo_dir)
    run(["git", "config", "user.name", "Lab Student"], repo_dir)
    run(["git", "config", "user.email", "student@example.com"], repo_dir)

    with open(os.path.join(repo_dir, "app.py"), "w") as f:
        f.write("print('Version 1.0: Main branch')\n")
    run(["git", "add", "app.py"], repo_dir)
    run(["git", "commit", "-m", "Initial commit on main"], repo_dir)

    run(["git", "checkout", "-b", "feature-greet"], repo_dir)
    with open(os.path.join(repo_dir, "greet.py"), "w") as f:
        f.write("def greet(name):\n    return f'Hello, {name}!'\n")
    run(["git", "add", "greet.py"], repo_dir)
    run(["git", "commit", "-m", "Add greeting module on feature branch"], repo_dir)

    run(["git", "checkout", "main"], repo_dir)
    run(["git", "merge", "feature-greet", "--no-ff", "-m", "Merge feature-greet into main"], repo_dir)
    run(["git", "log", "--oneline", "--graph", "--all"], repo_dir)
