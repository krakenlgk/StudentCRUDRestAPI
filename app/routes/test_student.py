import unittest
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from app.routes.student import student_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'your_test_database_uri'
app.config['TESTING'] = True
db = SQLAlchemy(app)

app.register_blueprint(student_bp)

class StudentAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        # Clean up the database after each test
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_student(self):
        response = self.app.get('/api/v1/students/1')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIn('data', data)

    def test_update_student(self):
        # Create a student for testing
        new_student = {'name': 'Test Student', 'age': 20, 'grade': 'A'}
        response = self.app.post('/api/v1/students', json=new_student)
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])

        # Update the student
        updated_data = {'name': 'Updated Student', 'age': 21, 'grade': 'B'}
        response = self.app.put(f'/api/v1/students/{data["data"]["_id"]}', json=updated_data)
        updated_data = response.get_json()['data']

        # Check if the update was successful
        self.assertEqual(response.status_code, 200)
        self.assertTrue(updated_data['success'])
        self.assertEqual(updated_data['data']['name'], 'Updated Student')
        self.assertEqual(updated_data['data']['age'], 21)
        self.assertEqual(updated_data['data']['grade'], 'B')

    def test_delete_student(self):
        # Create a student for testing deletion
        new_student = {'name': 'Test Student', 'age': 20, 'grade': 'A'}
        response = self.app.post('/api/v1/students', json=new_student)
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])

        # Delete the student
        response = self.app.delete(f'/api/v1/students/{data["data"]["_id"]}')
        deleted_data = response.get_json()['data']

        # Check if the deletion was successful
        self.assertEqual(response.status_code, 200)
        self.assertTrue(deleted_data['success'])
        self.assertEqual(deleted_data['data']['name'], 'Test Student')

    def test_get_all_students(self):
        # Create multiple students for testing
        students_to_create = [
            {'name': 'Student A', 'age': 22, 'grade': 'B'},
            {'name': 'Student B', 'age': 23, 'grade': 'A'},
            {'name': 'Student C', 'age': 24, 'grade': 'C'}
        ]

        # Add multiple students
        for student_data in students_to_create:
            response = self.app.post('/api/v1/students', json=student_data)
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.get_json()['success'])

        # Get all students
        response = self.app.get('/api/v1/students')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIn('data', data)
        self.assertEqual(len(data['data']), len(students_to_create))

    def test_add_student(self):
        # Add a new student
        new_student_data = {'name': 'New Student', 'age': 25, 'grade': 'A'}
        response = self.app.post('/api/v1/students', json=new_student_data)
        data = response.get_json()['data']

        # Check if the addition was successful
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['data']['name'], 'New Student')
        self.assertEqual(data['data']['age'], 25)
        self.assertEqual(data['data']['grade'], 'A')

if __name__ == '__main__':
    unittest.main()
