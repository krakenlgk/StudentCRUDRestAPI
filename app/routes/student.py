import logging
from flask import Blueprint, request
from flask_restful import Api, Resource
from app.models import db, Student

student_bp = Blueprint('student', __name__)
api = Api(student_bp)

# Configure logging
logging.basicConfig(level=logging.INFO)  # Set the logging level as needed

class StudentResource(Resource):
    def get(self, student_id):
        try:
            student = Student.query.get_or_404(student_id)
            logging.info(f"Student retrieved: {student.name} (ID: {student.id})")
            return {
                'success': True,
                'message': 'Student retrieved successfully',
                'data': {
                    '_id': student.id,
                    'name': student.name,
                    'age': student.age,
                    'grade': student.grade
                }
            }
        except Exception as e:
            logging.error(f"Error retrieving student: {str(e)}")
            return {
                'success': False,
                'message': 'Error retrieving student',
                'error': str(e)
            }, 500

    def put(self, student_id):
        try:
            student = Student.query.get_or_404(student_id)
            
            data = request.get_json()
            student.name = data.get('name', student.name)
            student.age = data.get('age', student.age)
            student.grade = data.get('grade', student.grade)

            db.session.commit()

            logging.info(f"Student updated: {student.name} (ID: {student.id})")
            return {
                'success': True,
                'message': 'Student updated successfully',
                'data': {
                    '_id': student.id,
                    'name': student.name,
                    'age': student.age,
                    'grade': student.grade
                }
            }
        except Exception as e:
            logging.error(f"Error updating student: {str(e)}")
            return {
                'success': False,
                'message': 'Error updating student',
                'error': str(e)
            }, 500

    def delete(self, student_id):
        try:
            student = Student.query.get_or_404(student_id)
            db.session.delete(student)
            db.session.commit()

            logging.info(f"Student deleted: {student.name} (ID: {student.id})")
            return {
                'success': True,
                'message': 'Student deleted successfully',
                'data': {
                    '_id': student.id,
                    'name': student.name,
                    'age': student.age,
                    'grade': student.grade
                }
            }
        except Exception as e:
            logging.error(f"Error deleting student: {str(e)}")
            return {
                'success': False,
                'message': 'Error deleting student',
                'error': str(e)
            }, 500

class StudentsResource(Resource):
    def get(self):
        try:
            students = Student.query.all()
            students_data = [
                {
                    '_id': student.id,
                    'name': student.name,
                    'age': student.age,
                    'grade': student.grade
                }
                for student in students
            ]

            logging.info("Students retrieved successfully")
            return {
                'success': True,
                'message': 'Students retrieved successfully',
                'data': students_data
            }
        except Exception as e:
            logging.error(f"Error retrieving students: {str(e)}")
            return {
                'success': False,
                'message': 'Error retrieving students',
                'error': str(e)
            }, 500

    def post(self):
        try:
            data = request.get_json()
            new_student = Student(
                name=data['name'],
                age=data['age'],
                grade=data['grade']
            )
            db.session.add(new_student)
            db.session.commit()

            logging.info(f"Student added: {new_student.name} (ID: {new_student.id})")
            return {
                'success': True,
                'message': 'Student added successfully',
                'data': {
                    '_id': new_student.id,
                    'name': new_student.name,
                    'age': new_student.age,
                    'grade': new_student.grade
                }
            }
        except Exception as e:
            logging.error(f"Error adding student: {str(e)}")
            return {
                'success': False,
                'message': 'Error adding student',
                'error': str(e)
            }, 500

api.add_resource(StudentsResource, '/api/v1/students')
api.add_resource(StudentResource, '/api/v1/students/<string:student_id>')
