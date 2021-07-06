"""Issues Model for HTTP request body"""

import datetime
from typing import Optional
from pydantic import BaseModel, validator
from myghub.dt.timemachine import TimeMachine


time_machine = TimeMachine()


class GetIssues(BaseModel):
    """Object for /issues"""

    repository: str
    datetime_format: str = '%Y-%m-%d %H:%M:%S'
    state: str
    search_started_at: datetime.datetime
    search_finished_at: datetime.datetime

    @validator('search_started_at', 'search_finished_at', pre=True)
    @classmethod
    def parse_datetime(cls, value, values):
        """Use custom datetime parsor"""

        return time_machine.str_to_dt(value, values['datetime_format'])


class Issue(BaseModel):
    """Issue object"""

    title: str
    number: int
    state: str
    created_at: Optional[str]
    closed_at: Optional[str]


class Issues(BaseModel):
    """Issue list"""

    counts: int
    issues: list[Issue]
