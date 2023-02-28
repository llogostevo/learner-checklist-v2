from flask import Flask, render_template, jsonify
from judgements import *
from database import load_courses_from_db

app = Flask(__name__)

user = 'Joe Bloggs'

@app.route("/")
def index():
  courses = load_courses_from_db()
  return render_template('home.html',
                         company='PLC',
                         options=OPTIONS,
                         courses=courses,
                         teacherCourses=teacherCourses,
                         user='Joe Bloggs', 
                        )


@app.route("/student/studentUnitChecklist.html")
def studentUnitChecklist():
  return render_template('student/studentUnitChecklist.html',
                         company='PLC',
                         options=OPTIONS,
                         courses=COURSES,
                         teacherCourses=teacherCourses,
                         user='Joe Bloggs',
                         criteria=criteria)


@app.route("/teacher/teacherUnitChecklist.html")
def teacherUnitChecklist():
  return render_template('/teacher/teacherUnitChecklist.html',
                         company='PLC',
                         options=OPTIONS,
                         courses=COURSES,
                         teacherCourses=teacherCourses,
                         user='Joe Bloggs',
                         criteria=criteria)

@app.route("/UX/uxExamples.html")
def uxExamples():
  return render_template('/UX/uxExamples.html',
                         company='PLC',
                         options=OPTIONS,
                         courses=COURSES,
                         teacherCourses=teacherCourses,
                         user='Joe Bloggs',
                         criteria=criteria)


# Can be used to test the data coming from the db functions, just put the db function to be assigned to data
# running the path will display the returned data format to the browser
@app.route("/api/json.html")
def api():
  data = load_courses_from_db()
  return  jsonify(data)


      
# this will run the app when run is pressed
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
