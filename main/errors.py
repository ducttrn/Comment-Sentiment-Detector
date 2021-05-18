from marshmallow import fields, Schema


class ErrorSchema(Schema):
    error_code = fields.Int()
    message = fields.String()
    errors = fields.Dict()


class Error(Exception):
    """This is the base class for Flask Exceptions,
    To give basic structure to error payload.
    """

    errors = None
    status_code = 500

    def __init__(self, errors=None):
        super(Error)

        if self.errors is None:
            self.errors = errors or {}


class StatusCode(object):
    BAD_REQUEST = 400
    FORBIDDEN = 403
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500


class ErrorCode(object):
    BAD_REQUEST = 40000
    NOT_FOUND = 40400
    INTERNAL_SERVER_ERROR = 50000
    FORBIDDEN = 40300


class InternalServerError(Error):
    status_code = StatusCode.INTERNAL_SERVER_ERROR
    error_code = ErrorCode.INTERNAL_SERVER_ERROR
    message = "There was a problem processing your request."


class NotFoundError(Error):
    status_code = StatusCode.NOT_FOUND
    error_code = ErrorCode.NOT_FOUND
    message = "The resource requested doesn't exist."


class BadRequestError(Error):
    status_code = StatusCode.BAD_REQUEST
    error_code = ErrorCode.BAD_REQUEST
    message = "Bad request, please try again."
