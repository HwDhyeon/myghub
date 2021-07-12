"""GitHub Issue Service for Issues Router"""

from operator import attrgetter
from fastapi.exceptions import HTTPException
from myghub.gh.client import github
from myghub.dt.timemachine import TimeMachine
from myghub.server.models.issue import GetIssues, Issue, Issues


class IssuesService:
    """IssuesService"""

    def __init__(self):
        self._gh = github
        self._tm = TimeMachine()

    def get_all_issues(self, arg: GetIssues) -> Issues:
        """Find all issues for repository

        Args:
            arg (GetIssues): GetIssues object from request

        Returns:
            Issues: Founded all issues
        """

        if arg.state not in ['all', 'open', 'closed']:
            raise HTTPException(
                status_code=400,
                detail='State must be one of ["all", "open", "closed"].',
            )

        repo = self._gh.get_repo(arg.repository)
        issues = repo.get_issues(
            since=arg.search_started_at, sort='created_at', state=arg.state
        )

        data = Issues(counts=0, issues=[])

        for issue in issues:
            if issue.created_at < arg.search_started_at:
                continue
            if arg.search_finished_at < issue.created_at:
                continue
            if issue.state == 'closed':
                if issue.closed_at < arg.search_started_at:
                    continue
                if arg.search_finished_at < issue.closed_at:
                    continue

            issue_obj = Issue(
                title=issue.title,
                number=issue.number,
                author=issue.user.login,
                labels=[i.name for i in issue.labels],
                state=issue.state,
                created_at=None,
                closed_at=None,
            )

            if issue.created_at:
                issue_obj.created_at = self._tm.dt_to_str(issue.created_at)
            if issue.closed_at:
                issue_obj.closed_at = self._tm.dt_to_str(issue.closed_at)

            data.issues.append(issue_obj)

        data.issues.sort(key=attrgetter('number'))
        data.counts = len(data.issues)
        return data
