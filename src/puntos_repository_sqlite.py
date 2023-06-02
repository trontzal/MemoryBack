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


def read_uno(usuario):
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


def create(new_puntos):
    con = sqlite3.connect("puntos.db")
    cur = con.cursor()
    values = (new_puntos["usuario"], new_puntos["puntos"], new_puntos["tipo_de_juego"])
    cur.execute("INSERT INTO datos (usuario, puntos, tipo_de_juego) VALUES (?, ?, ?)", values)
    con.commit()
    con.close()
    return "he añadido datos"