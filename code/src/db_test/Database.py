import sqlite3

class Database:
    conn = None
    cur = None
    def __init__(self, filename):
        self._filename = filename

    def connect(self):
        self.conn = sqlite3.connect(self._filename)
        self.cur = self.conn.cursor()
    
    """
        tabla: tabla en la cual insertar los datos
        values: tuple conteniendo los datos a ser ingresados
    """
    def insertarEnTabla(self, tabla, values: tuple):
        # preparacion de la query a ser realizada
        stmt = f"INSERT INTO {tabla} VALUES ("
        for i in range(len(values)-1):
            stmt += "?, "
        stmt += "?)"
        
        # ejecucion de la query preparada
        try:
            self.cur.execute(stmt, values)
        except sqlite3.ProgrammingError:
            print("SQL::BAD REQUEST")
    
    def buscarEnTabla(self, tabla, values: tuple):
        