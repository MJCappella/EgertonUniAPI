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

  return jsonify('faculties': faculty_list)
