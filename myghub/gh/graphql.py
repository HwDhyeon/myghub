from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from myghub import env


class GitHub:
    def __init__(self, token: str = None):
        if token is None:
            token = env.GH_TOKEN

        _transport = AIOHTTPTransport(
            url='https://api.github.com/graphql',
            headers={'Authorization': f'Bearer {token}'}
        )

        self._client = Client(
            transport=_transport,
            fetch_schema_from_transport=True
        )

    @property
    def client(self):
        return self._client

    def execute(self, query: str):
        r = self._client.execute(gql(query))
        return r
