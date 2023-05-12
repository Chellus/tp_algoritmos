import sqlite3

conn = sqlite3.connect("database_main.db")
c = conn.cursor()

#creacion de las tablas
# if creado:
#     c.execute("""CREATE TABLE organigrama(
#                 COD INTEGER,
#                 ORG TEXT,
#                 FEC TEXT
#     )
#     """)
#     c.execute("""CREATE TABLE dependencia(
#                 COD INTEGER,
#                 NOM TEXT,
#                 CODRES INTEGER
#     )
#     """)
#     c.execute("""CREATE TABLE persona(
#                 COD INTEGER,
#                 DOC INTEGER,
#                 APE TEXT,
#                 NOM TEXT,
#                 TEL INTEGER,
#                 DIR TEXT,
#                 DEP INTEGER,
#                 SAL INTEGER
#     )
#     """)
#     print("Tablas creadas")


def crear_organigrama(cod_o,org_o,fec_o):
    if cod_o > 3:
        print("Ingrese un codigo menor o igual a 3 digitos")
    c.execute("SELECT * FROM organigrama")
    items = c.fetchall()
    for item in items:
        while cod_o == item[0]:
            print("Ingresa otro codigo")

    c.executemany("INSERT INTO organigrama VALUES(?,?,?)",list)

conn.commit()
conn.close()
