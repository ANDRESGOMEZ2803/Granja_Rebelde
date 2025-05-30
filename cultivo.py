class Cultivo:
    def __init__(self, nombre, tipo, area, rendimiento):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__area = area
        self.__rendimiento = rendimiento

    def calcular_produccion(self):
        return self.__area * self.__rendimiento
    
    def editar(self, nombre=None, tipo=None, area=None, rendimiento=None):
        if nombre: self.__nombre = nombre
        if tipo: self.__tipo = tipo
        if area: self.__area = area
        if rendimiento: self.__rendimiento = rendimiento

    def __str__(self):
        return f"Cultivo: {self.__nombre}, Tipo: {self.__tipo}, Produccion: {self.calcular_produccion()}Kg"