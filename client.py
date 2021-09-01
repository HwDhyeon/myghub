from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport


transport = AIOHTTPTransport(
    url='https://api.github.com/graphql',
    headers={'Authorization': 'Bearer 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'}
)


client = Client(transport=transport, fetch_schema_from_transport=True)

query = gql(
    """
    {
        repository(owner: "mobigen", name: "IRIS") {
            milestone(number: 41) {
                title
                issues(first: 100) {
                    edges {
                        node {
                            title
                            number
                            url
                        }
                    }
                }
            }
        }
    }
"""
)

query = gql(
    """
    {
        repository(owner: "mobigen", name: "IRIS") {
            milestones(states: [OPEN], first: 10) {
                nodes {
                    title
                    description
                    url
                    issues(states: [OPEN, CLOSED], first: 100) {
                        nodes {
                            title
                            number
                            state
                            url
                            labels(first: 20) {
                                nodes {
                                    description
                                }
                            }
                            createdAt
                            closedAt
                        }
                        pageInfo {
                            hasNextPage
                            endCursor
                        }
                    }
                }
                pageInfo {
                    hasNextPage
                    endCursor
                }
            }
        }
    }
"""
)

result = client.execute(query)
print(result)
