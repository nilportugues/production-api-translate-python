from flask_restplus import fields

from translate_api.api.restplus import api

internal_server_error = api.model('internal_server_error', {
    'error': fields.String(description='Error description'),
})

# ----------------------------

detect_text_request = api.model('detect_text_request', {
    'text': fields.String(description='Text to detect'),
})

detect_text_response = api.model('detect_text_response', {
    'language': fields.String(description='Guessed language'),
    'confidence': fields.Float(description="Degree of confindence")
})

translated_text_request = api.model('Translate text', {
    'from_language': fields.String(description='Translate to'),
    'to_language': fields.String(description='Translate to'),
    'text': fields.String(description='Text to translate'),
})

translated_text_response = api.model('Translated text', {
    'original': fields.String(description='Original text'),
    'translated': fields.String(description='Translated text'),

})
