from flask import Flask, request
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

@app.route('/todo/user/<usuario>', methods=['GET']) #devuelve todos los puntos de un usuario especifico
def un_usuario(usuario):
    return get_puntos_by_usuario(usuario)

@app.route('/todo/game/<tipo_de_juego>', methods=['GET']) #devuelve todos los puntos de un tipo de juego especifico)
def tipo_de_juego(tipo_de_juego):
    return get_puntos_by_tipo_de_juego(tipo_de_juego)

@app.route('/todo/posicion/<usuario>/<tipo_de_juego>', methods=['GET']) #devuelve la posicion )
def posicion(usuario, tipo_de_juego):
    return get_posicion(usuario, tipo_de_juego)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/todo' , methods=['POST']) #Para guardar datos en la db
def new_puntuacion():
    data = request.get_json()
    print('**nueva puntuacuon', data)
    post_puntos(data)
    return ""




