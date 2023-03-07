from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DBCONNECTIONSTRING']

engine = create_engine(db_connection_string, connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)

def load_courses_from_db():
  #connect to the db, then once out of the block close connection automatically
  with engine.connect() as conn:
    result = conn.execute(text("select * from course"))
  
    column_names = result.keys()
  
  courses = []
  for row in result.all():
    courses.append(dict(zip(column_names, row)))

  return courses


# not sure how to get this to work for all users
def load_teacherTopics_from_db(id):
  with engine.connect() as conn:
    s = text("Select user.firstname,  user.lastname, unit.unit_number, unit.unit_name, criteria.criteria_name, subcriteria.subcriteria_name FROM (((((teacher inner join teaching on teaching.teacher_id = teacher.teacher_id) Inner join subcriteria on teaching.subcriteria_id = subcriteria.subcriteria_id) Inner join criteria on subcriteria.criteria_id = criteria.criteria_id) Inner join unit on unit.unit_id = criteria.unit_id) Inner join user on user.user_id = teacher.user_id) where user.user_id = :val")
    result = conn.execute(s, {'val':id})
    
  column_names = result.keys()
  topics = []
  for row in result.all():
    topics.append(dict(zip(column_names, row)))

  return topics