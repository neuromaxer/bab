import os

from dotenv import load_dotenv
from github import Github


load_dotenv()


def get_github_client() -> Github:
    return Github(
        login_or_token=os.getenv("BAB_GITHUB_ACCESS_TOKEN"),
    )


github_client = get_github_client()
bab_repo = github_client.get_repo(full_name_or_id=os.getenv("BAB_GITHUB_REPO_NAME"))
