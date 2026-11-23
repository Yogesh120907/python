"""
Experiment 31: Fork an existing GitHub repository, resolve a reported issue,
submit a solution through a pull request, and synchronize with upstream.
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
    upstream_bare = os.path.join(workspace, "upstream.git")
    fork_bare = os.path.join(workspace, "fork.git")
    maintainer_dir = os.path.join(workspace, "maintainer")
    contributor_dir = os.path.join(workspace, "contributor_fork")

    os.makedirs(maintainer_dir)
    run(["git", "init", "--bare", "-b", "main", upstream_bare], workspace)
    run(["git", "init", "-b", "main"], maintainer_dir)
    run(["git", "config", "user.name", "Upstream Owner"], maintainer_dir)
    run(["git", "config", "user.email", "owner@example.com"], maintainer_dir)
    with open(os.path.join(maintainer_dir, "math_utils.py"), "w") as f:
        f.write("def divide(a, b):\n    return a / b\n")
    run(["git", "add", "math_utils.py"], maintainer_dir)
    run(["git", "commit", "-m", "Initial release with divide function"], maintainer_dir)
    run(["git", "remote", "add", "origin", upstream_bare], maintainer_dir)
    run(["git", "push", "-u", "origin", "main"], maintainer_dir)

    run(["git", "clone", "--bare", upstream_bare, fork_bare], workspace)
    run(["git", "clone", fork_bare, contributor_dir], workspace)
    run(["git", "config", "user.name", "Contributor"], contributor_dir)
    run(["git", "config", "user.email", "contributor@example.com"], contributor_dir)
    run(["git", "remote", "add", "upstream", upstream_bare], contributor_dir)

    run(["git", "checkout", "-b", "fix-issue-1"], contributor_dir)
    with open(os.path.join(contributor_dir, "math_utils.py"), "w") as f:
        f.write("def divide(a, b):\n    if b == 0:\n        raise ValueError('Cannot divide by zero')\n    return a / b\n")
    run(["git", "commit", "-am", "Fix #1: Handle division by zero"], contributor_dir)
    run(["git", "push", "-u", "origin", "fix-issue-1"], contributor_dir)

    run(["git", "fetch", fork_bare, "fix-issue-1"], maintainer_dir)
    run(["git", "merge", "FETCH_HEAD", "--no-ff", "-m", "Merge PR #2: Fix issue #1"], maintainer_dir)
    run(["git", "push", "origin", "main"], maintainer_dir)

    run(["git", "checkout", "main"], contributor_dir)
    run(["git", "fetch", "upstream"], contributor_dir)
    run(["git", "merge", "upstream/main"], contributor_dir)
    run(["git", "push", "origin", "main"], contributor_dir)
    run(["git", "log", "--oneline", "--graph", "--all"], contributor_dir)
