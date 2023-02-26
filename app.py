from flask import Flask, render_template
from judgements import *
app = Flask(__name__)



@app.route("/")
def hello_world():
  return render_template('home.html', 
                         company='PLC', 
                        options =  OPTIONS)


# this will run the app when run is pressed
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)