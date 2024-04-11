from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/contact')
def hello_world():
    return "<h2>Ma page de contact</h2>"

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')
                                                                                                               
if __name__ == "__main__":
  app.run(debug=True)
