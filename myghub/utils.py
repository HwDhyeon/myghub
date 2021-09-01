import datetime
from typing import Any


def typecast_for_iris(data: Any) -> str:
    if isinstance(data, int):
        return 'INTEGER'
    elif isinstance(data, float):
        return 'REAL'
    elif isinstance(data, datetime.date):
        return 'DATE'
    else:
        return 'TEXT'
