# StudentCRUDRestAPI
StudentCRUDRestAPI

This README file provides information on setting up and using the Student CRUD REST API. The API is designed to manage student records, allowing users to perform operations such as adding, retrieving, updating, and deleting student information.

# Table of Contents
Prerequisites
Installation
API Endpoints
Add a new student
Get all students
Get a student by ID
Update existing student information
Delete a student record

# Prerequisites
Before setting up the Student CRUD REST API, ensure you have the following prerequisites installed:

Python 3
Flask
MongoDB (Make sure MongoDB server is running)

# Installation
Clone the repository:
git clone https://github.com/yourusername/StudentCRUDRestAPI.git
cd StudentCRUDRestAPI

Install dependencies:
pip install -r requirements.txt

Set up environment variables:
Create a .env file in the root directory and add the following:
FLASK_APP=app.py
FLASK_ENV=development
MONGODB_URI=mongodb://localhost:27017/studentdb


Start the server:
flask run

# API Endpoints
#Add a new student
#Endpoint: POST /api/students
Request Body:
{
  "name": "John Doe",
  "age": 21,
  "grade": "A"
}

Response:
{
  "success": true,
  "message": "Student added successfully",
  "data": {
    "_id": "1234567890",
    "name": "John Doe",
    "age": 21,
    "grade": "A"
  }
}

Get all students
Endpoint: GET /api/students
Response:
{
  "success": true,
  "message": "Students retrieved successfully",
  "data": [
    {
      "_id": "1234567890",
      "name": "John Doe",
      "age": 21,
      "grade": "A"
    },
    {
      "_id": "0987654321",
      "name": "Jane Smith",
      "age": 20,
      "grade": "B"
    }
    // More student records...
  ]
}

Get a student by ID
Endpoint: GET /api/students/:id
Response:
{
  "success": true,
  "message": "Student retrieved successfully",
  "data": {
    "_id": "1234567890",
    "name": "John Doe",
    "age": 21,
    "grade": "A"
  }
}

Update existing student information
Endpoint: PUT /api/students/:id
Request Body:
{
  "age": 22,
  "grade": "B"
}

Response:
{
  "success": true,
  "message": "Student updated successfully",
  "data": {
    "_id": "1234567890",
    "name": "John Doe",
    "age": 22,
    "grade": "B"
  }
}

Delete a student record
Endpoint: DELETE /api/students/:id
Response:
{
  "success": true,
  "message": "Student deleted successfully",
  "data": {
    "_id": "1234567890",
    "name": "John Doe",
    "age": 22,
    "grade": "B"
  }
}

