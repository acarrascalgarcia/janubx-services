from typing import Any, Dict, Optional


def _parse_service_response(
        *,
        status_code: int,
        body: Dict[str, Any]
) -> Dict[str, Any]:
    return {
        'statusCode': status_code,
        'body': body
    }


def ok(
        *,
        body: Dict[str, Any]
) -> Dict[str, Any]:
    kwargs = {
        'status_code': 200,
        'body': body
    }
    return _parse_service_response(**kwargs)


def created(
        *,
        body: Dict[str, Any]
) -> Dict[str, Any]:
    kwargs = {
        'status_code': 201,
        'body': body
    }
    return _parse_service_response(**kwargs)


def bad_request(
        *,
        body: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    body = body or {}
    kwargs = {
        'status_code': 400,
        'body': body
    }
    return _parse_service_response(**kwargs)


def not_found(
        *,
        body: Dict[str, Any]
) -> Dict[str, Any]:
    kwargs = {
        'status_code': 404,
        'body': body
    }
    return _parse_service_response(**kwargs)


def internal_error(
        *,
        body: Dict[str, Any]
) -> Dict[str, Any]:
    kwargs = {
        'status_code': 500,
        'body': body
    }
    return _parse_service_response(**kwargs)
