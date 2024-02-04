from flask import Flask
from app.config import Config
from app.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize database
    db.init_app(app)

    with app.app_context():
        # Import models here if you need to create database tables
        from app.models import Student

        # Create tables
        db.create_all()

    # Register blueprints and other configurations if needed
    from app.routes.student import student_bp
    app.register_blueprint(student_bp, url_prefix='/api/v1')

    return app
