.PHONY: setup run migrate test

setup:
    pip install -r requirements.txt

run:
    python run.py

migrate:
    flask db init
    flask db migrate
    flask db upgrade

test:
    python -m unittest discover -s tests
