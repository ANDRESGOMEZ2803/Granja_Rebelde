from cultivo import Cultivo
from animal import Animal
from granja import Granja

def main():
    granja = Granja("La Rastrojera Rebelde")

    #Agregar cultivos
    maiz = Cultivo("Maiz", "Cereal", 10, 1500)
    papa = Cultivo("Papa", "Tubérculo", 5, 1200)
    granja.agregar_cultivo(maiz)
    granja.agregar_cultivo(papa)

    #Agregar animales
    vaca1 = Animal("Vaca", "Holstein", 5, 600)
    gallina = Animal("Pollo", "Leghorn", 2, 2)
    granja.agregar_animal(vaca1)
    granja.agregar_animal(gallina)

    #Mostrar Reporte
    granja.reporte()

if __name__ == "__main__":
    main()