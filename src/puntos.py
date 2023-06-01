from .puntos_repository_sqlite import *

def get_todos():
    return read_all()

def get_puntos_by_usuario(usuario):
    return read_uno(usuario)
