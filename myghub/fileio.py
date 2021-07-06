"""File IO"""

import json
from typing import Any, Union


def read_json(file: str) -> Union[dict[str, Any], list[Any]]:
    """Parse JSON file.

    Args:
        file (str): JSON file path

    Returns:
        dict or list: parsed JSON object
    """

    with open(file=file, mode='r', encoding='utf-8') as f:
        data = json.loads(f.read())
    return data


def write_json(file: str, data: Union[dict[str, Any], list[Any]]):
    """Save data for JSON file.

    Args:
        file (str): JSON file path
        data (dict or list): JSON object
    """

    with open(file=file, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=2))
