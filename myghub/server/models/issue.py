"""Issues Model for HTTP request body"""

import datetime
from typing import Optional
from pydantic import BaseModel, validator
from myghub.dt.timemachine import TimeMachine
from myghub.server.models.milestone import Milestone


time_machine = TimeMachine()


class GetIssues(BaseModel):
    """Object for /issues"""

    repository: str
    state: str = 'all'
    datetime_format: str = '%Y-%m-%d %H:%M:%S'
    search_started_at: datetime.datetime
    search_finished_at: datetime.datetime

    @validator('search_started_at', 'search_finished_at', pre=True)
    @classmethod
    def parse_datetime(cls, value, values):
        """Use custom datetime parsor"""

        return time_machine.str_to_dt(value, values['datetime_format'])


class GetIssuesByMilestone(BaseModel):
    repository: str
    state: str = 'all'
    milestone_title: str


class Issue(BaseModel):
    """Issue object"""

    title: str
    number: int
    author: str
    labels: list[str]
    state: str
    created_at: Optional[str]
    closed_at: Optional[str]
    url: str
    milestone: Optional[Milestone]


class Issues(BaseModel):
    """Issue list"""

    counts: int
    issues: list[Issue]
