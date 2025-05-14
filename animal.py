class Animal:
    def __init__(self, especie, raza, edad, peso):
        self.__especie = especie
        self.__raza = raza
        self.__edad = edad
        self.__peso = peso

    def calcular_produccion(self):
        if self.__especie.lower() == 'vaca':
            return self.__peso * 0.1
        elif self.__especie.lower() =='pollo':
            return self.__peso * 0.05
        else:
            return self.__peso * 0.08
        
    def editar(self, especie=None, raza=None, edad=None, peso=None):
        if especie: self.__especie = especie
        if raza: self.__raza = raza
        if edad: self.__edad = edad
        if peso: self.__peso = peso

    def __str__(self):
        return f"Animal: {self.__especie}, Raza: {self.__raza}, Produccion: {self.calcular_produccion():.2f}Kg"