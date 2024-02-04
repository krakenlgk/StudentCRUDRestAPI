from flask import jsonify
from app.models import db, Student
from flask_testing import TestCase

class StudentTestCase(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///students.db')
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_all_students(self):
        # Test for getting all students
        response = self.client.get('/api/v1/students')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIn('data', data)

    def test_add_new_student(self):
        # Test for adding a new student
        new_student_data = {'name': 'Test Student', 'age': 20, 'grade': 'A'}
        response = self.client.post('/api/v1/students', json=new_student_data)
        data = response.get_json()['data']
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['data']['name'], 'Test Student')
        self.assertEqual(data['data']['age'], 20)
        self.assertEqual(data['data']['grade'], 'A')

    def test_get_student_by_id(self):
        # Test for getting a student by ID
        # Create a student for testing
        new_student_data = {'name': 'Test Student', 'age': 20, 'grade': 'A'}
        response = self.client.post('/api/v1/students', json=new_student_data)
        student_id = response.get_json()['data']['_id']

        # Get the student by ID
        response = self.client.get(f'/api/v1/students/{student_id}')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIn('data', data)
        self.assertEqual(data['data']['_id'], student_id)

    def test_update_student_information(self):
        # Test for updating student information
        # Create a student for testing
        new_student_data = {'name': 'Test Student', 'age': 20, 'grade': 'A'}
        response = self.client.post('/api/v1/students', json=new_student_data)
        student_id = response.get_json()['data']['_id']

        # Update the student information
        updated_data = {'name': 'Updated Student', 'age': 21, 'grade': 'B'}
        response = self.client.put(f'/api/v1/students/{student_id}', json=updated_data)
        updated_data = response.get_json()['data']

        # Check if the update was successful
        self.assertEqual(response.status_code, 200)
        self.assertTrue(updated_data['success'])
        self.assertEqual(updated_data['data']['name'], 'Updated Student')
        self.assertEqual(updated_data['data']['age'], 21)
        self.assertEqual(updated_data['data']['grade'], 'B')

    def test_delete_student(self):
        # Test for deleting a student
        # Create a student for testing deletion
        new_student_data = {'name': 'Test Student', 'age': 20, 'grade': 'A'}
        response = self.client.post('/api/v1/students', json=new_student_data)
        student_id = response.get_json()['data']['_id']

        # Delete the student
        response = self.client.delete(f'/api/v1/students/{student_id}')
        deleted_data = response.get_json()['data']

        # Check if the deletion was successful
        self.assertEqual(response.status_code, 200)
        self.assertTrue(deleted_data['success'])
        self.assertEqual(deleted_data['data']['name'], 'Test Student')
