from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy

healthcheck_bp = Blueprint('healthcheck', __name__)

@healthcheck_bp.route('/healthcheck', methods=['GET'])
def healthcheck():
    return {'status': 'OK'}

@healthcheck_bp.route('/database-check', methods=['GET'])
def database_check():
    try:
        # Check the database connection
        db = SQLAlchemy()
        db.session.execute('SELECT 1')  # Execute a simple query
        db.session.commit()

        return {'database_status': 'OK', 'message': 'Database connection check passed successfully'}
    except Exception as e:
        return {'database_status': 'Error', 'error': str(e), 'message': 'Database connection check failed'}, 500
