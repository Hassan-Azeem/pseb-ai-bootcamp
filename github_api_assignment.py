import requests


GITHUB_USERNAMES = ("octocat", "Hassan-Azeem", "torvalds")


def main():
    for username in GITHUB_USERNAMES:
        response = requests.get(
            f"https://api.github.com/users/{username}",
            timeout=10,
        )
        if response.status_code != 200:
            raise RuntimeError(
                f"GitHub API request for {username!r} failed "
                f"with status {response.status_code}"
            )

        user = response.json()
        print(user["login"], user["public_repos"])


if __name__ == "__main__":
    main()
