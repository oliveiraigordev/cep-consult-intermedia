from flask import Blueprint, jsonify, request
from src.errors.error_controller import handle_errors
from src.main.factories.cep_factory import cep_factory

cep_bp = Blueprint('cep', __name__)


@cep_bp.post('/cep')
def find_cep():
    try:
        data = request.json
        result = cep_factory(data)
        return jsonify({'exists': bool(result)})
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response['body']), error_response['status_code']
