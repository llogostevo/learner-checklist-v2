from flask import Flask, render_template
from judgements import *

app = Flask(__name__)

user = 'Joe Bloggs'


@app.route("/")
def index():
  return render_template('home.html',
                         company='PLC',
                         options=OPTIONS,
                         courses=COURSES,
                         teacherCourses=teacherCourses,
                         user='Joe Bloggs')


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

  
# this will run the app when run is pressed
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
