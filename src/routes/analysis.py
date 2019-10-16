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

    print(request.files)
    uploaded_file = request.files.get('file')

    if not uploaded_file:
        return error_response(
            status=400,
            msg='Arquivo não encontrado'
        )

    filename = uploaded_file.get('filename')

    if not filename:
        return error_response(
            status=400,
            msg='Arquivo com nome vazio'
        )

    if not uploaded_file.get('buffer') or not uploaded_file.get('buffer').get('data'):
        return error_response(
            status=400,
            msg='Arquivo vazio'
        )

    try:
        filename = secure_filename(filename)

        bytes_list = uploaded_file.get('buffer').get('data')

        path_to_file = os.path.join('/tmp', filename)

        open(path_to_file, 'wb').write(bytes(bytes_list))

        obj = Object(path_to_file)

        data = obj.get_all_info()

        os.remove(path_to_file)

        return json_response(200, data)

    except Exception as e:
        print(e)

        return error_response()
