"""MyGHub Main Component"""

import fire
from myghub.server.models.issue import GetIssues
from myghub.server.services.issue import IssueService

issue_service = IssueService()


class Getter:
    """Getting data from GitHub"""

    def issues(
        self,
        repository: str,
        state: str,
        search_started_at: str,
        search_finished_at: str,
        *,
        datetime_format: str = '%Y-%m-%d %H:%M:%S'
    ) -> str:
        """Get all issues for repository

        Returns:
           list: GitHub Issue list
        """

        data = issue_service.get_all_issues(
            GetIssues(
                repository=repository,
                state=state,
                search_started_at=search_started_at,
                search_finished_at=search_finished_at,
                datetime_format=datetime_format,
            )
        )

        return data.json(ensure_ascii=False, indent=2)


class Pipeline:
    """Command Line Interface Component"""

    def __init__(self):
        self.get = Getter()


def app():
    """Run MyHub client"""

    fire.Fire(Pipeline)


if __name__ == '__main__':
    app()
