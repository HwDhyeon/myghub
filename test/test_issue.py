import unittest
from datetime import datetime, timedelta
from fastapi.exceptions import HTTPException
from myghub.server.models.issue import GetIssues, Issue, Issues
from myghub.server.services.issues import IssuesService
from myghub.dt.timemachine import TimeMachine


def get_two_dates():
    now = datetime.now()
    now = now.replace(hour=0, minute=0, second=0)

    prev_month = now - timedelta(days=30)
    prev_month = prev_month.replace(hour=23, minute=59, second=59)

    return now, prev_month


class TestIssue(unittest.TestCase):
    def setUp(self):
        self.service = IssuesService()
        self.dt_tool = TimeMachine()

    def test_get_open_issues(self):
        now, prev_month = get_two_dates()

        issues = self.service.get_all_issues(
            GetIssues(
                repository='mobigen/IRIS',
                state='open',
                search_started_at=self.dt_tool.dt_to_str(prev_month),
                search_finished_at=self.dt_tool.dt_to_str(now)
            )
        )

        self.assertIsInstance(issues, Issues)

        for issue in issues.issues:
            self.assertIsInstance(issue, Issue)
            self.assertEqual(issue.state, 'open')
            self.assertIsNotNone(issue.created_at)

    def test_get_closed_issues(self):
        now, prev_month = get_two_dates()

        issues = self.service.get_all_issues(
            GetIssues(
                repository='mobigen/IRIS',
                state='closed',
                search_started_at=self.dt_tool.dt_to_str(prev_month),
                search_finished_at=self.dt_tool.dt_to_str(now)
            )
        )

        self.assertIsInstance(issues, Issues)

        for issue in issues.issues:
            self.assertIsInstance(issue, Issue)
            self.assertEqual(issue.state, 'closed')
            self.assertIsNotNone(issue.closed_at)

    def test_get_all_issues(self):
        now, prev_month = get_two_dates()

        issues = self.service.get_all_issues(
            GetIssues(
                repository='mobigen/IRIS',
                state='all',
                search_started_at=self.dt_tool.dt_to_str(prev_month),
                search_finished_at=self.dt_tool.dt_to_str(now)
            )
        )

        self.assertIsInstance(issues, Issues)

        for issue in issues.issues:
            self.assertIsInstance(issue, Issue)
            self.assertIn(issue.state, ['open', 'closed'])
            if issue.state == 'closed':
                self.assertIsNotNone(issue.closed_at)

    def test_get_all_issues_invalid_state(self):
        with self.assertRaises(HTTPException):
            now, prev_month = get_two_dates()

            _ = self.service.get_all_issues(
                GetIssues(
                    repository='mobigen/IRIS',
                    state='isDummy',
                    search_started_at=self.dt_tool.dt_to_str(prev_month),
                    search_finished_at=self.dt_tool.dt_to_str(now)
                )
            )

if __name__ == '__main__':
    unittest.main()
