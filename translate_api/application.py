import logging.config

from flask import Flask, Blueprint, jsonify
from flask_restplus import Swagger

from translate_api import settings
from translate_api.api.translation.endpoints.translation import ns as text_translation_namespace
from translate_api.api.translation.endpoints.detection import ns as text_detection_namespace
from translate_api.api.translation.endpoints.languages import ns as languages_namespace
from translate_api.api.restplus import api

app = Flask(__name__)
Swagger(app)
log = logging.getLogger(__name__)

def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP
    flask_app.config['SWAGGER_UI_ENABLED'] = settings.SWAGGER_UI_ENABLED

def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)

    # ADD ENDPOINTS
    api.add_namespace(text_translation_namespace)
    api.add_namespace(text_detection_namespace)
    api.add_namespace(languages_namespace)
    # END ENDPOINTS


    flask_app.register_blueprint(blueprint)


def create_app():

    initialize_app(app)
    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))

    return app


if __name__ == "__main__":
    create_app()
