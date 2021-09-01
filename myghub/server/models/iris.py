from typing import Any
from pydantic import BaseModel


class IRISResponseField(BaseModel):
    """IRIS issue field"""

    name: str
    type: str


class IRISResponseData(BaseModel):
    """Issue object for IRIS"""

    fields: list[IRISResponseField]
    results: list[list[Any]]


class IRISResponse(BaseModel):
    data: IRISResponseData
