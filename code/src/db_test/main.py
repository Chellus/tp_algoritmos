from Persona import Persona
from Dependencia import Dependencia
from Database import Database

DATABASE = "base.db"

dep_ceo = Dependencia("CEO", 1)
jefe = Persona("6038491", "Riveros", "Marcelo", "0991916160", "Avda Nanawa C/ Los Pinos", 0, 5000000)


db = Database(DATABASE)
db.connect()

db.insertarData("Persona", jefe.getDict())
