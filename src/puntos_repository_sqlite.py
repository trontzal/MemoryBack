import sqlite3

con=sqlite3.connect("puntos.db")
cur =con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS datos (id INTEGER PRIMARY KEY, usuario TEXT, puntos INTEGER, tipo_de_juego TEXT)")
con.close()

def read_all():
    con=sqlite3.connect("puntos.db")
    cur =con.cursor()
    res=cur.execute("SELECT * FROM datos")
    datos=res.fetchall()
    con.close()
    print("*************", datos)
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
    return datos
