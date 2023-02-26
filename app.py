from flask import Flask, render_template
from judgements import *
app = Flask(__name__)

user = 'Joe Bloggs'

@app.route("/")
def hello_world():
  return render_template('home.html', 
                         company='PLC', 
                        options =  OPTIONS, 
                        user = 'Joe Bloggs')


# this will run the app when run is pressed
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)