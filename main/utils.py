from functools import wraps

from flask import request
from marshmallow import ValidationError

from main import BadRequestError


def get_request_args():
    if request.method == "GET":
        return request.args.to_dict()
    return request.get_json() or {}


def parse_args_with(schema):
    """
    This decorator can be used to parse arguments of a request using a Marshmallow schema. If there is any validation
    error, a BadRequest exception will be raised along with the error details.
    """

    def parse_args_with_decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            request_args = get_request_args()
            try:
                parsed_args = schema.load(request_args)
            except ValidationError as exc:
                raise BadRequestError(exc.messages)
            kwargs["args"] = parsed_args
            return f(*args, **kwargs)

        return decorated_function

    return parse_args_with_decorator
