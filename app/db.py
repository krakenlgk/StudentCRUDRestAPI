from app.models import db

def init_db(app):
    db.init_app(app)

    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    from app import create_app

    app = create_app()
    init_db(app)
