"""GitHub REST API Client"""

from github import Github
from myghub import env

github = Github(env.GH_TOKEN)
