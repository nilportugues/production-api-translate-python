from flask_restplus import fields

from rest_api_demo.api.restplus import api

translated_text_request = api.model('Translate text', {
    'from_language': fields.String(description='Translate to'),
    'to_language': fields.String(description='Translate to'),
    'text': fields.String(description='Text to translate'),
})

translated_text_response = api.model('Translated text', {
    'text_original': fields.String(description='Original text'),
    'text_translated': fields.String(description='Translated text'),

})
