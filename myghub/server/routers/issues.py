"""GitHub Issues Router for Server"""

from fastapi import APIRouter
from myghub.server.services.issues import IssuesService
from myghub.server.models.issue import GetIssues, Issues

router = APIRouter(
    prefix='/issues',
    tags=['issues'],
    responses={404: {
        'description': 'Not Found'
    }}
)

service = IssuesService()


@router.post('/', response_model=Issues)
async def read_issues(get_issues: GetIssues) -> Issues:
    """Find all issues for repository

    Args:
        get_issues (GetIssues): GetIssues object from request json data
    """

    return service.get_all_issues(get_issues)
