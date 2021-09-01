import datetime
from typing import Union
from pydantic import BaseModel
from myghub.dt.timemachine import TimeMachine


time_machine = TimeMachine()


class GetMilestone(BaseModel):
    repository: str
    title: str


class GetMilestones(BaseModel):
    repository: str
    states: list[str]


class Milestone(BaseModel):
    id: str
    title: str
    number: int
    state: str
    url: str
    description: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    due_on: datetime.datetime


class RESTMilestone(Milestone):
    open_issues: int
    closed_issues: int


class GraphQLMilestone(Milestone):
    total_count: int



class Milestones(BaseModel):
    """Milestone list"""

    counts: int
    milestones: list[Union[RESTMilestone, GraphQLMilestone]]
