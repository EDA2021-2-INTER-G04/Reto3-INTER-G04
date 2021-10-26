"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import orderedmap as om
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()


def loadData(catalog, sample):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog, sample)

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Contar los avistamientos en una ciudad")
    print("3- Contar los avistamientos por duración")
    print("4- Contar avistamientos por hora/minutos del día")
    print("5- Contar los avistamientos en un rango de fechas")
    print("6- Contar los avistamientos de una zona geográfica")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Seleccione el tamaño de la muestra")
        print("1- Small")
        print("2- 5%")
        print("3- 10%")
        print("4- 20%")
        print("5- 30%")
        print("6- 50%")
        print("7- 80%")
        print("8- Large")
        sample = int(input())
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog, sample)
        print("El número de avistamientos cargados fue de ", lt.size(catalog["ufos"]), ".")
        print("Los primeros 5 avistamientos cargados son:")
        for n in range(1, 6):
            actualUFO = lt.getElement(catalog["ufos"], n)
            print("Fecha: ", actualUFO["datetime"], ", Ciudad: ", actualUFO["city"], ", País: ", actualUFO["country"], ", Forma: ", actualUFO["shape"], ", Duración: ", actualUFO["duration (seconds)"])
        print("\nLos últimos 5 avistamientos cargados son:")
        for m in range(1, 6):
            index = (lt.size(catalog["ufos"])-5)+m
            actualUFO = lt.getElement(catalog["ufos"], index)
            print("Fecha: ", actualUFO["datetime"], ", Ciudad: ", actualUFO["city"], ", País: ", actualUFO["country"], ", Forma: ", actualUFO["shape"], ", Duración: ", actualUFO["duration (seconds)"])

    elif int(inputs[0]) == 2:
        city = input("Ingrese la ciudad a consultar: ")
        sightnings = controller.ufosByCity(catalog, city)
        print("\nEl número de elementos en el árbol rojo negro por ciudades es de ",om.size(catalog["cities"]) )
        print("La altura del árbol rojo negro por ciudades es de ", om.height(catalog["cities"]))
        print("\nEl número de ciudades donde se han visto OVNIs es de ", lt.size(om.keySet(catalog["cities"])))
        print("\nSe han avistado ", lt.size(sightnings), " OVNIs en ", city)
        print("Los tres primeros avistamientos en la ciudad son:")
        for n in range(1,4):
            actualUFO = lt.getElement(sightnings, n)
            print("Fecha y hora: ", actualUFO["datetime"], ", Ciudad y país: ", actualUFO["city"], ", ", actualUFO["country"], ", Duración (s): ", actualUFO["duration (seconds)"], ", Forma: ", actualUFO["shape"])

        print("\nLos últimos tres avistamientos en la ciudad son:")
        for w in range(1,4):
            index = (lt.size(sightnings)-3)+w
            actualUFO = lt.getElement(sightnings, index)
            print("Fecha y hora: ", actualUFO["datetime"], ", Ciudad y país: ", actualUFO["city"], ", ", actualUFO["country"], ", Duración (s): ", actualUFO["duration (seconds)"], ", Forma: ", actualUFO["shape"])

    else:
        sys.exit(0)
sys.exit(0)
