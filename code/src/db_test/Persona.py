class Persona:
    subordinados = []
    id = None
    def __init__(self, ci, apellido, nombre, telefono, direccion, dependencia, salario):
        self.ci = ci
        self.apellido = apellido
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.dependencia = dependencia
        self.salario = salario

    def cambioId(self, id):
        self.id = id

    def getTuple(self):
        return (self.ci, self.apellido, self.nombre, self.telefono, self.direccion, self.dependencia, self.salario)
    
    def getDict(self):
        return {
            "ci": self.ci,
            "apellido": self.apellido,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "id_dependencia": self.dependencia,
            "salario": self.salario
        }