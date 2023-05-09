
import random

    


class Nodo:    
    codigo = 0

    def __init__(self,nombre,codres):
        self.nombre = nombre
        codres = codres 
        self.hijos = []

        Nodo.codigo = random.randint(1,999)
        while(Nodo.codigo in self.hijos):
            Nodo.codigo = random.randint(1,999)
            
    def agregar_nodo(self, nodo_hijo):
        if len(self.hijos) < 5:
            self.hijos.append(nodo_hijo)
            exit
        else:
            exit

    def imprimir_arbol(self, nivel=0):
        prefijo = "    " * nivel
        print(prefijo + "|--", self.valor)
        if self.hijos:
            for hijo in self.hijos:
                hijo.imprimir_arbol(nivel + 1)


# Crear los nodos
#dependencias

nodo_raiz = Nodo("Empresa")
nodo_1 = Nodo("Sotelo")
nodo_2 = Nodo("Atilio")
nodo_3 = Nodo("Fer")
nodo_4 = Nodo("K")
nodo_5 = Nodo("Go to")
nodo_6 = Nodo("josue ")

# Construir la estructura del árbol
nodo_raiz.agregar_hijo(nodo_1)
nodo_raiz.agregar_hijo(nodo_2)
nodo_1.agregar_hijo(nodo_3)
nodo_2.agregar_hijo(nodo_4)
nodo_2.agregar_hijo(nodo_5)

# Imprimir el árbol
nodo_raiz.imprimir_arbol()
