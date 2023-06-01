from flask import Flask
from .puntos import *
from flask_cors import CORS

    
app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def hello():
    return "hola"

@app.route('/todo') #devuelve todos los datos de la db
def get_todo():
    return get_todos()

@app.route('/todo/<usuario>', methods=['GET']) #devuelve todos los puntos de un usuario especifico
def un_usuario(usuario):
    return get_puntos_by_usuario(usuario)




