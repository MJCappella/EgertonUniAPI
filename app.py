from flask import Flask, jsonify, request, url_for
import mysql.connector

app = Flask(__name__)

#MySQL connection configuration
db_config = {
  'host': 'localhost',
  'user': 'root',
  'passwd': '',
  'database': 'egertonapi',
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# API endpoints
@app.route("/faculties", methods=['GET'])
def get_faculties():
  query = "SELECT * FROM faculties"
  cursor.execute(query)
  faculties = cursor.fetchall()

  faculty_list = []
  for faculty in faculties:
    faculty_data = {
      'id': faculty[0],
      'name': faculty[1],
      'no_of_departments': faculty[2],
    }
    faculty_list.append(faculty_data)

  return jsonify({'faculties':faculty_list})



@app.route("/departments", methods=['GET'])
def get_departments():
  query = "SELECT * FROM departments"
  cursor.execute(query)
  departments = cursor.fetchall()

  departments_list = []
  for department in departments:
    department_data = {
      'id': department[0],
      'name': department[1],
      'faculty_id': department[2],
    }
    department_list.append(department_data)

  return jsonify({'departments':department_list})



@app.route("/programmes", methods=['GET'])
def get_programmes():
  query = "SELECT * FROM programmes"
  cursor.execute(query)
  programmes = cursor.fetchall()

  programmes_list = []
  for programme in programmes:
    programme_data = {
      'id': programmes[0],
      'name': programmes[1],
      'dept_id': programmes[2],
    }
    programmes_list.append(programme_data)

  return jsonify({'programmes':programmes_list})

if __name = "__main__":
  run(app)
