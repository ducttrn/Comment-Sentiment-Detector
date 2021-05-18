from flask import Flask, request, jsonify

from main.configs import config
from main.controllers import init_routes
from main.memcache_client import MemcacheClient
from main.errors import NotFoundError, InternalServerError, BadRequestError

app = Flask(__name__)
app.config.from_object(config)
init_routes()


memcache_client = MemcacheClient(servers=config.MEMCACHED_SERVERS)


# Errors handlers
def _response_error(exception=None):
    """To manipulate structure of response payload.
    :param exception: Exception instance for errors
    :return: flask.Response instance
    """

    prepared_data = {"error_code": exception.error_code, "message": exception.message}

    if exception.errors != {}:
        prepared_data["errors"] = exception.errors

    return jsonify(prepared_data), exception.status_code


@app.errorhandler(errors.Error)
def handle_error(exception):
    return _response_error(exception=exception)


@app.errorhandler(404)
def page_not_found(*_):
    return _response_error(exception=NotFoundError())


@app.errorhandler(500)
def internal_server_error(*_):
    return _response_error(exception=InternalServerError())


# Allow CORS for API requests
@app.after_request
def after_request(response):
    header = response.headers
    header["Access-Control-Allow-Origin"] = "*"
    header["Access-Control-Allow-Methods"] = "*"
    header["Access-Control-Allow-Headers"] = "*"

    if request.method == "OPTIONS":
        response.status_code = 200

    return response
