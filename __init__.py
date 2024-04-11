from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return "<h2>Ma page de contact</h2>"

@app.route('/contact/')
def MaPremiereAPI():
    return render_template('contact.html')

@app.route('/somme/<int:valeur1>/<int:valeur2>')
def somme(valeur1,valeur2):
    return "<h2>La somme de votre valeur est : </h2>" + str(valeur1 + valeur2)
                                                                                                               
if __name__ == "__main__":
  app.run(debug=True)
