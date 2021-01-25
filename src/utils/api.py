from typing import Any, Dict, Union


def get_data(event: Dict[str, Any]) -> Dict[str, Any]:
    try:
        return event['body']
    except TypeError:
        return {}


def get_path(event: Dict[str, Any], path: str) -> Union[Any, None]:
    try:
        return event['path'][path]
    except KeyError:
        return None
