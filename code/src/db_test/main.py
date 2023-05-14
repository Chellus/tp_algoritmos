from Persona import Persona
from Dependencia import Dependencia
from Database import Database

DATABASE = "base.db"

dep_ceo = Dependencia("CEO", 1)
jefe = Persona("6038497", "Riveros", "Fernando", "0991880416", "Avda Nanawa C/ Los Pinos", 1, 2500000)

db = Database(DATABASE)
db.connect()

#db.insertarData("Dependencia", dep_ceo.getDict())
res = db.buscarData("Empleado", "id = 1", ["nombre", "manager_id"])
print(res)
