import unittest
from flask_testing import TestCase
from app import create_app, db

class StudentTestCase(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_all_students(self):
        # Test for getting all students

    def test_add_new_student(self):
        # Test for adding a new student

    def test_get_student_by_id(self):
        # Test for getting a student by ID

    def test_update_student_information(self):
        # Test for updating student information

    def test_delete_student(self):
        # Test for deleting a student
