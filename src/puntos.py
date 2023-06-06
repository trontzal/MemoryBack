from .puntos_repository_sqlite import *

def get_todos():
    return read_all()

def get_puntos_by_usuario(usuario):
    return read_por_usuario(usuario)

def get_puntos_by_tipo_de_juego(tipo_de_juego):
    return read_por_juego(tipo_de_juego)

def get_posicion(usuario, tipo_de_juego):
    return read_posicion(usuario, tipo_de_juego)

def post_puntos(new_puntos):
    print(create(new_puntos))
