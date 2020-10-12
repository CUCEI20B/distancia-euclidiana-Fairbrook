from particula import Particula

class Lista:
    def __init__(self):
        self.__particulas = []

    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0,particula)

    def mostrar(self):
        for particula in self.__particulas:
            print (particula)


lista = Lista()
p1 = Particula(1,1,1,1,1,1,1,1,1)
p2 = Particula(2,2,2,2,2,2,2,2,2)
lista.agregar_final(p1)
lista.agregar_inicio(p2)
lista.agregar_inicio(p1)
lista.mostrar()