import logging

from flask import request
from flask_restplus import Resource
from translate_api.api.translation.serializers import *
from translate_api.api.restplus import api
from translate_api.api.translation.services.translate import TranslationService

log = logging.getLogger(__name__)
ns = api.namespace('text')


@ns.route('/translate')
class TranslationResource(Resource):
    @api.expect(translated_text_request)
    @api.response(200, 'Success', translated_text_response)
    @api.response(400, 'Bad Request', internal_server_error)
    @api.response(500, 'Internal Server Error', internal_server_error)
    def post(self):
        """
        Translates a text from an input language to an output language.
        """
        if not request.json:
            return {'error': 'bad request'}, 400

        success, response = TranslationService().execute(request.json)

        if not success:
            return {'errors': response}, 400

        return response, 200
