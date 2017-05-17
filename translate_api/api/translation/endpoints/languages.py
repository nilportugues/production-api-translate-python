import logging

from flask import request
from flask_restplus import Resource
from translate_api.api.translation.serializers import *
from translate_api.api.restplus import api
from translate_api.api.translation.services.translate import TranslationService
from googletrans.constants import LANGUAGES
log = logging.getLogger(__name__)
ns = api.namespace('text')


language_list = api.model('language_list', {
    'languages': fields.Raw(LANGUAGES, required=True)
})


@ns.route('/languages')
class LanguagesResource(Resource):
    @api.response(200, 'Success', language_list)
    def get(self):
        """
        Returns a key-value list with all the supported languages.
        """
        return {'languages': LANGUAGES}, 200

