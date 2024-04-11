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
  
  nombre = int(input("Entrez un nombre entier : "))
  
  if nombre % 2 == 0:
    print(nombre, "est un nombre pair.")
  else:
    print(nombre, "est un nombre impair.")

return "<h2>La somme de votre valeur est : </h2>" + str(valeur1 + valeur2)
