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
  return 

@app.route("/departments")
def departments():
  return 

@app.route("/programmes")
def programmes():
  return 
