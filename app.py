from flask import Flask, jsonify, request, url_for
import mysql-connector

app = Flask(__name__)
app = SQLAlchemy(db)

db = mysql.connector.connect(
  host = "localhost"
  user = "root"
  passwd = ""
)

cur = db.cursor()
cur.execute()

@app.route("/")
def home():
  return 

@app.route("/faculties")
def faculties():
  faculties = (SELECT * FROM faculties)
  return json(faculties)

@app.route("/departments")
def departments():
  departments = (SELECT * FROM departments)
  return json(departments)

@app.route("/programmes")
def programmes():
  programmes = (SELECT * FROM programmes)
  return json(programmes)
