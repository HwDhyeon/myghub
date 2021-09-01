from typing import Union
from fastapi.exceptions import HTTPException
from myghub.gh.graphql import GitHub
from myghub.dt.timemachine import TimeMachine
from myghub.server.models.milestone import GetMilestone, GetMilestones, GraphQLMilestone


class MilestoneService:
    def __init__(self):
        self._github = GitHub()
        self._tm = TimeMachine('%Y-%m-%dT%H:%M:%SZ')

    def _parse_options(self, options: Union[GetMilestone, GetMilestones]) -> (str, str, str):
        owner, name = options.repository.split('/')
        states = f'[{", ".join([x.upper() for x in options.states])}]'

        return owner, name, states

    def get_all_milestones(self, options: GetMilestones):
        owner, name, states = self._parse_options(options)

        query = """
        {
            repository(owner: "%s", name: "%s") {
                milestones(states: %s, first: 10) {
                    nodes {
                        id
                        title
                        number
                        state
                        url
                        description
                        issues(states: [OPEN, CLOSED], first: 100) {
                            totalCount
                        }
                        createdAt
                        updatedAt
                        dueOn
                    }
                }
            }
        }
        """ % (owner, name, states)

        result = self._github.execute(query)

        milestones = [
            GraphQLMilestone(
                id=milestone.get('id'),
                title=milestone.get('title'),
                number=milestone.get('number'),
                state=milestone.get('state').lower(),
                url=milestone.get('url'),
                description=milestone.get('description'),
                total_count=milestone.get('issues').get('totalCount'),
                created_at=self._tm.str_to_dt(milestone.get('createdAt')),
                updated_at=self._tm.str_to_dt(milestone.get('updatedAt')),
                due_on=self._tm.str_to_dt(milestone.get('dueOn')),
            ) for milestone in result['repository']['milestones']['nodes']
        ]

        return milestones

    def get_milestone(self, options: GetMilestone):
        milestones = self.get_all_milestones(
            GetMilestones(
                repository=options.repository,
                states=['OPEN', 'CLOSED']
            )
        )

        for milestone in milestones:
            if milestone.title == options.title:
                return milestone

        return None


if __name__ == '__main__':
    service = MilestoneService()
    print(
        service.get_milestone(
            GetMilestone(
                repository='mobigen/IRIS',
                states=['OPEN'],
                title='v3.0.0-RC20210729.0'
            )
        )
    )
