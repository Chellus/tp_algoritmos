# Este archivo se ejecuta una vez para crear y configurar la base de datos
#
#   * Creamos una tabla de dependencia
#   * Creamos una tabla de personas en la que se almacenan los empleados

import sqlite3

con = sqlite3.connect("base.db")
cur = con.cursor()

cur.execute(""" CREATE TABLE Dependencia (
            id INTEGER NOT NULL PRIMARY KEY,
            nombre TEXT,
            manager_id INTEGER
)""")

cur.execute("""CREATE TABLE Persona (
            id INTEGER NOT NULL PRIMARY KEY,
            ci TEXT,
            apellido TEXT,
            nombre TEXT,
            telefono TEXT,
            direccion TEXT,
            id_dependencia INTEGER,
            salario INTEGER,
            FOREIGN KEY(id_dependencia) REFERENCES Dependencia(id)
)""")

cur.execute("""CREATE TABLE Organigrama (
            id INTEGER NOT NULL PRIMARY KEY,
            nombre TEXT,
            fecha TEXT
)""")