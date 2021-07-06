"""GitHub API Server"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from myghub.server.routers import issues

tags_metadata = [
    {
        'name': 'issues',
        'description': 'Controls for GitHub issues.'
    }
]

app = FastAPI(
    title='My-GitHub API',
    description='GitHub API wrapper',
    version='0.2.0',
    openapi_tags=tags_metadata
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(issues.router)
