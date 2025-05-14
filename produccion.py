class Produccion:
    @staticmethod
    def calcular_total(lista_objetos):
        return sum(obj.calcular_produccion() for obj in lista_objetos)