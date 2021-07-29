"""GitHub Issues Router for Server"""

from typing import Dict
from fastapi import APIRouter
from myghub.utils import typecast_for_iris
from myghub.server.services.issues import IssuesService
from myghub.server.models.iris import IRISResponse, IRISResponseField, IRISResponseData
from myghub.server.models.issue import GetIssues, Issues

router = APIRouter(
    prefix='/issues',
    tags=['issues'],
    responses={
        404: {
            'description': 'Not Found'
        }
    }
)

service = IssuesService()


@router.post('/', response_model=Issues)
async def read_issues(get_issues: GetIssues) -> Issues:
    """Find all issues for repository

    Args:
        get_issues (GetIssues): GetIssues object from request json data

    Returns:
        Issues: Github issues
    """

    return service.get_all_issues(get_issues)


@router.post('/iris', response_model=IRISResponse)
async def read_issues_for_iris(get_issues: GetIssues) -> IRISResponse:
    """Find all issues for repository

    Args:
        get_issues (GetIssues): GetIssues object from request json data

    Returns:
        IRISResponse: Issues convert to IRIS REST API spec
    """

    data = service.get_all_issues(get_issues)

    fields = []
    results = []
    for issue in data.issues:
        dictissue = issue.dict()
        dictissue['labels'] = str(dictissue['labels'])
        for key, value in dictissue.items():
            fields.append(
                IRISResponseField(
                    name=key,
                    type=typecast_for_iris(value)
                )
            )
        results.append(list(dictissue.values()))

    return IRISResponse(
        data=IRISResponseData(
            fields=fields,
            results=results
        )
    )
