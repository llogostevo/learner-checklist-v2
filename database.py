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

