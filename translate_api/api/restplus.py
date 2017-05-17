import logging

from flask_restplus import Api
from werkzeug.exceptions import BadRequest

from translate_api import settings
from translate_api.settings import SWAGGER_UI_ENABLED

log = logging.getLogger(__name__)

swagger_docs = '/'
if not SWAGGER_UI_ENABLED:
    swagger_docs = False

api = Api(version='1.0', title='Translation API', doc=swagger_docs, catch_all_404s=True)


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': "" + message}, 500


@api.errorhandler(BadRequest)
def bad_request_handler(e):
    response = {
        'message': None,
        "_embedded": {
            "errors": [
                {
                    "message": "Failed to decode JSON object.",
                    "path": "/"
                }
            ]
        },
        "total": 1
    }

    return response, 400
