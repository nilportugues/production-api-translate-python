import logging

from flask import request
from flask_restplus import Resource
from translate_api.api.translation.serializers import *
from translate_api.api.restplus import api
from translate_api.api.translation.services.detect import DetectionService

log = logging.getLogger(__name__)
ns = api.namespace('text')

@ns.route('/detect')
class LanguageDetectionResource(Resource):
    @api.expect(detect_text_request)
    def post(self):
        """
        Detects from a given text the language it has been written in.
        """
        success, response = DetectionService().execute(request.json)

        return response, 200