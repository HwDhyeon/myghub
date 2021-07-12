"""GitHub REST API Client"""

from github import Github
from myghub import env
from myghub.exceptions import TokenNotFoundError

if not env.GH_TOKEN:
    raise TokenNotFoundError

github = Github(env.GH_TOKEN)
