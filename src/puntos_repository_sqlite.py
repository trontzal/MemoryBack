import sqlite3

con=sqlite3.connect("puntos.db")
cur =con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS datos (id INTEGER PRIMARY KEY AUTOINCREMENT, usuario TEXT, puntos INTEGER, tipo_de_juego TEXT)")
con.close()

def read_all():
    con=sqlite3.connect("puntos.db")
    cur =con.cursor()
    res=cur.execute("SELECT * FROM datos")
    datos=res.fetchall()
    con.close()
    resultados = []
    for dato in datos:
        resultado = {
            'id': dato[0],
            'usuario': dato[1],
            'puntos': dato[2],
            'tipo_de_juego': dato[3]
        }
        resultados.append(resultado)
    
    return resultados


def read_por_usuario(usuario):
    con=sqlite3.connect("puntos.db")
    cur=con.cursor()
    res=cur.execute("SELECT * FROM datos WHERE usuario =?", [usuario])
    datos=res.fetchall()
    con.close()
    resultados = []
    for dato in datos:
        resultado = {
            'id': dato[0],
            'usuario': dato[1],
            'puntos': dato[2],
            'tipo_de_juego': dato[3]
        }
        resultados.append(resultado)
    
    return resultados


def read_por_juego(tipo_de_juego):
    con=sqlite3.connect("puntos.db")
    cur=con.cursor()
    res=cur.execute("SELECT * FROM datos WHERE tipo_de_juego =?", [tipo_de_juego])
    datos=res.fetchall()
    con.close()
    resultados = []
    for dato in datos:
        resultado = {
            'id': dato[0],
            'usuario': dato[1],
            'puntos': dato[2],
            'tipo_de_juego': dato[3]
        }
        resultados.append(resultado)
    
    return resultados

import sqlite3

def read_posicion(usuario, tipo_de_juego):
    con = sqlite3.connect("puntos.db")
    cur = con.cursor()

    # Obtener los puntos del usuario y el tipo de juego específico
    cur.execute("SELECT puntos FROM datos WHERE usuario = ? AND tipo_de_juego = ?", (usuario, tipo_de_juego))
    user_points = cur.fetchone()
    print("Puntos del usuario:", user_points)
    
    # Obtener la posición del usuario en función de los puntos
    cur.execute("SELECT COUNT(*) FROM datos WHERE tipo_de_juego = ? AND puntos > ?", (tipo_de_juego, user_points[0]))
    position = cur.fetchone()[0] +1
    print("Posición del usuario:", position)

    con.close()

    return str(position)

print(read_posicion("anonimo", "memoriaVisual"))





def create(new_puntos):
    con = sqlite3.connect("puntos.db")
    cur = con.cursor()
    values = (new_puntos["usuario"], new_puntos["puntos"], new_puntos["tipo_de_juego"])
    cur.execute("INSERT INTO datos (usuario, puntos, tipo_de_juego) VALUES (?, ?, ?)", values)
    con.commit()
    con.close()
    return "he añadido datos"