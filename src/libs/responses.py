from flask import Response, json
from enum import Enum

class ErrorCode(Enum):
    INTERNAL_ERROR = 'INTERNAL_ERROR'
    UPLOADED_FILE = 'UPLOADED_FILE'
    MISSING_QUERY_ARG = 'MISSING_QUERY_ARG'


def error_response(code=ErrorCode.INTERNAL_ERROR, status=500, msg='An error occurred'):
    """ Builds an error response
    Parameters
    ----------
    code: enum
        internal code of the error
    status: int
        http status code
    msg: str
        message to pass to the user

    Return
    ----------
    Response
        flask response object
    """
    if not isinstance(code, ErrorCode):
        code = ErrorCode.INTERNALERROR

    error = {
        'error': {
            'code': code.value,
            'status': status,
            'msg': msg,
        },
    }

    headers = {
        'Content-Type': 'application/json',
    }

    print(error)

    return Response(
        response=json.dumps(error),
        status=status,
        headers=headers
    )

def json_response(status, payload):
    headers = {
        'Content-Type': 'application/json',
    }

    return Response(
        response=json.dumps(payload),
        status=status,
        headers=headers
    )
