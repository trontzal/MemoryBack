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


def read_posicion(tipo_de_juego):
    con = sqlite3.connect("puntos.db")
    cur = con.cursor()

    # Obtener los usuarios del mismo tipo de juego con los puntos en orden descendente
    cur.execute("SELECT usuario, puntos FROM datos WHERE tipo_de_juego = ? ORDER BY puntos DESC", (tipo_de_juego,))
    usuarios = cur.fetchall()

    con.close()

    return usuarios

def read_grafico(tipo_de_juego):
    con = sqlite3.connect("puntos.db")
    cur = con.cursor()
    cur.execute("SELECT puntos, COUNT(puntos) AS repeticiones FROM datos WHERE tipo_de_juego = ? GROUP BY puntos", (tipo_de_juego,))
    datos = cur.fetchall()
    con.close()
    grafica = []
    for dato in datos:
        grafica.append({
            'x': dato[0],
            'y': dato[1]
        })
    return grafica






def create(new_puntos):
    con = sqlite3.connect("puntos.db")
    cur = con.cursor()
    values = (new_puntos["usuario"], new_puntos["puntos"], new_puntos["tipo_de_juego"])
    cur.execute("INSERT INTO datos (usuario, puntos, tipo_de_juego) VALUES (?, ?, ?)", values)
    con.commit()
    con.close()
    return "he añadido datos"