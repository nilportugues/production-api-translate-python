import logging

from flask import request
from flask_restplus import Resource
from rest_api_demo.api.translation.serializers import *
from rest_api_demo.api.restplus import api
from rest_api_demo.api.translation.services.translate import TranslationService

log = logging.getLogger(__name__)
ns = api.namespace('translate')


@ns.route('/')
class TranslationResource(Resource):
    @api.expect(translated_text_request)
    def post(self):
        success, response = TranslationService().execute(request.json)

        if not success:
            return {'errors': response}, 400

        return response, 200
