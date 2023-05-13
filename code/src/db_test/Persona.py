class Persona:
    subordinados = []
    def __init__(self, id, ci, apellido, nombre, telefono, direccion, dependencia, salario):
        self.id = id
        self.ci = ci
        self.apellido = apellido
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.dependencia = dependencia
        self.salario = salario
