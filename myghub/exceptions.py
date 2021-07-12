"""Define MyGHub Errors"""


class MyGHubError(Exception):
    """Default MyGHub Error"""


class TokenNotFoundError(ValueError):
    """Occurs when GitHub Token does not exist."""

    def __init__(self, meesage: str = 'GitHub Token is not found.'):
        super().__init__(self, meesage)
