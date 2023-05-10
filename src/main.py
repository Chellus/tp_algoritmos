import json

class Dependencia:
    def __init__(self, cod, nombre, cod_jefe):
        self.cod = cod
        self.nombre = nombre
        self.cod_jefe = cod_jefe

class Persona:
    subordinates = []

    def __init__(self, cod, ci, apellido, nombre, telefono, direccion, dependencia, salario):
        self.cod = cod
        self.ci = ci
        self.apellido = apellido
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.dependencia = dependencia
        self.salario = salario

class Organigrama:
    employees = []
    root = None

    def readData(self, data):
        employee = None

        root_id = data["L0"][0]["id"]
        root_name = data["L0"][0]["name"]
        self.root = Employee(root_id, root_name, 0)
        self.employees.append(self.root)

        for key in data:
            if key == "L0":
                continue
            for i in range(len(data[key])):
                new_id = data[key][i]["id"]
                new_name = data[key][i]["name"]
                parent_id = data[key][i]["parent"]
                employee = Employee(new_id, new_name, parent_id)
                self.employees.append(employee)

    def getSubs(self, manager_id):
        subs = []
        for e in self.employees:
            if e.managerId == manager_id:
                subs.append(e)
        return subs
    
    def buildTree(self, root):
        employee = root
        subs = self.getSubs(employee.id)
        employee.subordinates = subs
        if len(subs) == 0:
            return
        for e in subs:
            self.buildTree(e)

    def printTree(self, root, level):
        for i in range(0, level, 1):
            print("\t", end='')
        print(root.name)
        subs = root.subordinates
        for e in subs:
            self.printTree(e, level+1)

with open("data.json", "r") as f:
    data = json.load(f)

tree = Tree()
tree.readData(data)
tree.buildTree(tree.root)
tree.printTree(tree.root, 0)
