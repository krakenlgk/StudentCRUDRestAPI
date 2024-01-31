from flask import Blueprint

healthcheck_bp = Blueprint('healthcheck', __name__)

@healthcheck_bp.route('/healthcheck', methods=['GET'])
def healthcheck():
    return {'status': 'OK'}
