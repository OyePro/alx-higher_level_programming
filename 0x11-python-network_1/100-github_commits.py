#!/usr/bin/python3
"""
Script to list 10 commits (from the most recent to oldest) of the
repository "rails" by the user "rails" using:
GitHub API
format: `<sha>: <author name>`
"""


if __name__ == "__main__":

    import requests
    import sys

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    content = requests.get(url, params={"per_page": 10})

    commits_json = content.json()
    for commit in commits_json:
        sha = commit["sha"]
        author_name = commit["commit"]["author"]["name"]
        print(f"{sha}: {author_name}")
