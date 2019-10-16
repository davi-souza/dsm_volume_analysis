import os
from flask import Blueprint, request
from werkzeug.utils import secure_filename
from src.libs.responses import ErrorCode, error_response, json_response
from src.services.object import Object

APIKEY = os.getenv('API_KEY')

analysis = Blueprint('analysis', __name__)

@analysis.route('/volume', methods=['POST'])
def volume_analysis():
    api_key = request.headers.get('X-API-Key')

    if not api_key or api_key != APIKEY:
        return error_response(
            status=401,
            msg='Não autorizado'
        )

    if 'file' not in request.files:
        return error_response(
            status=400,
            msg='Arquivo não encontrado'
        )

    uploaded_file = request.files['file']

    filename = uploaded_file.filename

    if not filename:
        return error_response(
            status=400,
            msg='Arquivo com nome vazio'
        )

    try:
        filename = secure_filename(filename)

        filepath = os.path.join('/tmp', filename)

        uploaded_file.save(filepath)

        obj = Object(filepath)

        data = obj.get_all_info()

        os.remove(filepath)

        return json_response(200, data)

    except Exception as e:
        print(e)

        return error_response()
