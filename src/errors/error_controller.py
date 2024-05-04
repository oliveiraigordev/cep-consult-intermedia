from typing import Dict
from .http_bad_request_error import HttpBadRequestError


def handle_errors(error: Exception) -> Dict:
    if isinstance(error, HttpBadRequestError):
        return {
            "status_code": error.status_code,
            "body": {
                "errors": [{
                    "error": error.name,
                    "message": error.message
                }]
            }
        }

    return {
        "status_code": 500,
        "body": {
            "errors": [{
                "error": "Server Error",
                "message": str(error)
            }]
        }
    }