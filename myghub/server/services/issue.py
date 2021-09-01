"""GitHub Issue Service for Issues Router"""

from operator import attrgetter
from fastapi.exceptions import HTTPException
from myghub.gh.client import github
from myghub.gh.graphql import GitHub
from myghub.dt.timemachine import TimeMachine
from myghub.server.models.issue import GetIssues, Issue, Issues, GetIssuesByMilestone
from myghub.server.models.milestone import Milestone, GraphQLMilestone, GetMilestone
from myghub.server.services.milestone import MilestoneService


class IssueService:
    """IssueService"""

    def __init__(self):
        self._gh = github
        self._gql = GitHub()
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
            if issue.pull_request:
                continue
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
                url=issue.html_url,
            )

            if issue.created_at:
                issue_obj.created_at = self._tm.dt_to_str(issue.created_at)
            if issue.closed_at:
                issue_obj.closed_at = self._tm.dt_to_str(issue.closed_at)

            milestone = issue.milestone
            if milestone:
                issue_obj.milestone=Milestone(
                    id=milestone.id,
                    title=milestone.title,
                    number=milestone.number,
                    state=milestone.state,
                    url=milestone.url,
                    description=milestone.description,
                    open_issues=milestone.open_issues,
                    closed_issues=milestone.closed_issues,
                    created_at=milestone.created_at,
                    updated_at=milestone.updated_at,
                    due_on=milestone.due_on
                )

            data.issues.append(issue_obj)

        data.issues.sort(key=attrgetter('number'))
        data.counts = len(data.issues)
        return data

    def get_all_issues_by_milestone(self, options: GetIssuesByMilestone):
        service = MilestoneService()
        milestone = service.get_milestone(
            GetMilestone(
                repository=options.repository,
                title=options.milestone_title,
            )
        )

        owner, name = options.repository.split('/')
        if (state := options.state) == 'open':
            state = '[OPEN]'
        elif state == 'closed':
            state = '[CLOSED]'
        else:
            state = '[OPEN, CLOSED]'

        query = """
        {
            repository(owner: "%s", name: "%s") {
                milestone(number: %s) {
                    nodes {
                        issues(states: %s, first: 100) {
                            nodes {
                                id
                                title
                                number
                                url
                                labels(first: 20) {
                                    nodes {
                                        name
                                    }
                                }
                                createdAt
                                closedAt
                            }
                        }
                    }
                }
            }
        }
        """ % (owner, name, milestone.number, state)

        result = self._gql.execute(query)

        return result


if __name__ == '__main__':
    service = IssueService()
    result = service.get_all_issues_by_milestone(
        GetIssuesByMilestone(
            repository='mobigen/IRIS',
            state='all',
            milestone_title='v3.0.0-RC20210729.0'
        )
    )

    print(result)
