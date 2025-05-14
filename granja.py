from cultivo import Cultivo
from animal import Animal
from produccion import Produccion

class Granja:
    def __init__(self, nombre):
        self._nombre = nombre
        self._cultivos = []
        self._animales = []

    def agregar_cultivo(self, cultivo):
        self._cultivos.append(cultivo)

    def eliminar_cultivo(self, cultivo):
        self._cultivos.remove(cultivo)

    def agregar_animal(self, animal):
        self._animales.append(animal)

    def eliminar_animal(self, animal):
        self._animales.remove(animal)

    def calcular_produccion_total(self):
        total_cultivos = Produccion.calcular_total(self._cultivos)
        total_animales = Produccion.calcular_total(self._animales)
        return total_cultivos + total_animales
    
    def reporte(self):
        print(f"Reporte de la Granja: {self._nombre}")
        print("Cultivos:")
        for c in self._cultivos:
            print(" ", c)
        print("Animales: ")
        for a in self._animales:
            print("", a)
        print(f"Produccion total: {self.calcular_produccion_total():.2f} kg")
