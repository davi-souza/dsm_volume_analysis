from flask import Response, json
from enum import Enum

class ErrorCode(Enum):
    INTERNAL_ERROR = 'INTERNAL_ERROR'
    UNAUTHORIZED = 'UNAUTHORIZED'
    UPLOADED_FILE = 'UPLOADED_FILE'
    MISSING_QUERY_ARG = 'MISSING_QUERY_ARG'

def error_response(status=500, msg='Ocorreu um erro'):
    """
    Builds an error response
    @param {int}        status http status code
    @param {string}     msg message to pass to the user
    @return {object}    flask response object
    """
    if not isinstance(code, ErrorCode):
        code = ErrorCode.INTERNALERROR

    payload = {
        'data': None,
        'errors': [{
            'message': msg,
            'extensions': {
                'message': msg,
                'status': status,
            },
        }],
    }

    headers = {
        'Content-Type': 'application/json',
    }

    print(payload)

    return Response(
        response=json.dumps(payload),
        status=status,
        headers=headers
    )

def json_response(status, data):
    headers = {
        'Content-Type': 'application/json',
    }

    payload = {
        'data': data,
        'errors': None,
    }

    return Response(
        response=json.dumps(payload),
        status=status,
        headers=headers
    )
