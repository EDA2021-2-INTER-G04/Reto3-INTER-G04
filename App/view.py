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
    print("7- Visualizar los avistamientos de una zona geográfica")

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
        print("\nEl número de avistamientos cargados fue de ", lt.size(catalog["ufos"]))
        for n in range(1, 6):
            actualUFO = lt.getElement(catalog["ufos"], n)
            print("Fecha: ", actualUFO["datetime"], ", Ciudad: ", actualUFO["city"], ", País: ", actualUFO["country"], ", Forma: ", actualUFO["shape"], ", Duración: ", actualUFO["duration (seconds)"])
        print("="*100)
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
        for n in range(1,4):
            actualUFO = lt.getElement(sightnings, n)
            print("Fecha y hora: ", actualUFO["datetime"], ", Ciudad y país: ", actualUFO["city"], ", ", actualUFO["country"], ", Duración (s): ", actualUFO["duration (seconds)"], ", Forma: ", actualUFO["shape"])
        print("="*100)
        for w in range(1,4):
            index = (lt.size(sightnings)-3)+w
            actualUFO = lt.getElement(sightnings, index)
            print("Fecha y hora: ", actualUFO["datetime"], ", Ciudad y país: ", actualUFO["city"], ", ", actualUFO["country"], ", Duración (s): ", actualUFO["duration (seconds)"], ", Forma: ", actualUFO["shape"])

    elif int(inputs[0]) == 4:
        hour0 = input("Ingrese desde qué hora filtrar los avistamientos (HH:MM): ")+":00"
        hour1 = input("Ingrese hasta qué hora filtrar los avistamientos (HH:MM): ")+":00"
        filtredUfos = controller.ufosByHour(catalog, hour0, hour1)
        size = 0
        for l in range(1, lt.size(filtredUfos)+1):
            actualHour = lt.getElement(filtredUfos, l)
            size += lt.size(actualHour)

        hours = om.keySet(catalog["hours"])
        print("\nLas horas más tardías donde se han visto OVNIs son:")
        for p in range(1,6):
            index = (lt.size(hours)+1)-p
            actualHour = lt.getElement(hours, index)
            print(actualHour, ": ", lt.size(om.get(catalog["hours"], actualHour)["value"]), " avistamientos.")

        print("\nHay registro de ", size, " avistamientos entre las ", hour0, " y las ", hour1)

        bigIndex = 1
        counted = 1
        while bigIndex <= lt.size(filtredUfos) and counted <= 3:
            actualHour = lt.getElement(filtredUfos, bigIndex)
            littleIndex = 1
            while littleIndex <= lt.size(actualHour) and counted <= 3:
                actualUFO = lt.getElement(actualHour, littleIndex)
                print("Fecha y hora: ", actualUFO["datetime"], ", Ciudad y país: ", actualUFO["city"], ", ", actualUFO["country"], ", Duración (s): ", actualUFO["duration (seconds)"], ", Forma: ", actualUFO["shape"])
                littleIndex += 1
                counted += 1
            bigIndex += 1
        print("="*100)
        lastThree = lt.newList("SINGLE_LINKED")
        bigIndex = lt.size(filtredUfos)
        counted = 1
        while 1 <= bigIndex <= lt.size(filtredUfos) and counted <= 3:
            actualHour = lt.getElement(filtredUfos, bigIndex)
            littleIndex = lt.size(actualHour)
            while 1 <= littleIndex <= lt.size(actualHour) and counted <= 3:
                actualUFO = lt.getElement(actualHour, littleIndex)
                lt.addFirst(lastThree, actualUFO)
                littleIndex -= 1
                counted += 1
            bigIndex -= 1
        for t in range(1, 4):
            actualUFO = lt.getElement(lastThree, t)
            print("Fecha y hora: ", actualUFO["datetime"], ", Ciudad y país: ", actualUFO["city"], ", ", actualUFO["country"], ", Duración (s): ", actualUFO["duration (seconds)"], ", Forma: ", actualUFO["shape"])

    elif int(inputs[0]) == 6:
        lonMin = str(round(float(input("Ingrese el límite inferior de longitud: ")),2))
        lonMax = str(round(float(input("Ingrese el límite superior de longitud: ")),2))
        latMin = str(round(float(input("Ingrese el límite inferior de latitud: ")),2))
        latMax = str(round(float(input("Ingrese el límite superior de latitud: ")),2))

        listUfosInZone = controller.ufosByZone(catalog, lonMin, lonMax, latMin, latMax)

        print("\nEl total de avistamientos dentro del área es de: ", lt.size(listUfosInZone))

        if lt.size(listUfosInZone) != 0:
            if lt.size(listUfosInZone) // 2 < 5:
                sample1 = lt.size(listUfosInZone) // 2
                sample2 = lt.size(listUfosInZone) - sample1
            else:
                sample1 = 5
                sample2 = sample1

            for n in range(1, sample1+1):
                actualUFO = lt.getElement(listUfosInZone, n)
                print("Fecha y hora: ", actualUFO["datetime"], ", Ciudad y país: ", actualUFO["city"],", ",  actualUFO["country"], ", Forma: ", actualUFO["shape"], ", Duración: ", actualUFO["duration (seconds)"], ", Coordenadas (lat, long): ", actualUFO["latitude"],", ", actualUFO["longitude"])
            print("="*100)
            for m in range(1, sample2+1):
                index = (lt.size(listUfosInZone)-sample2)+m
                actualUFO = lt.getElement(listUfosInZone, index)
                print("Fecha y hora: ", actualUFO["datetime"], ", Ciudad y país: ", actualUFO["city"],", ", actualUFO["country"], ", Forma: ", actualUFO["shape"], ", Duración: ", actualUFO["duration (seconds)"], ", Coordenadas (lat, long): ", actualUFO["latitude"],", ", actualUFO["longitude"])
    
    elif int(inputs[0]) == 7:
        lonMin = str(round(float(input("Ingrese el límite inferior de longitud: ")),2))
        lonMax = str(round(float(input("Ingrese el límite superior de longitud: ")),2))
        latMin = str(round(float(input("Ingrese el límite inferior de latitud: ")),2))
        latMax = str(round(float(input("Ingrese el límite superior de latitud: ")),2))
        lonAvg = (float(lonMin)+float(lonMax))/2
        latAvg = (float(latMin)+float(latMax))/2

        listUfosInZone = controller.ufosByZone(catalog, lonMin, lonMax, latMin, latMax)

        print("\nEl total de avistamientos dentro del área es de: ", lt.size(listUfosInZone))

        if lt.size(listUfosInZone) != 0:
            if lt.size(listUfosInZone) // 2 < 5:
                sample1 = lt.size(listUfosInZone) // 2
                sample2 = lt.size(listUfosInZone) - sample1
            else:
                sample1 = 5
                sample2 = sample1

            for n in range(1, sample1+1):
                actualUFO = lt.getElement(listUfosInZone, n)
                print("Fecha y hora: ", actualUFO["datetime"], ", Ciudad y país: ", actualUFO["city"],", ",  actualUFO["country"], ", Forma: ", actualUFO["shape"], ", Duración: ", actualUFO["duration (seconds)"], ", Coordenadas (lat, long): ", actualUFO["latitude"],", ", actualUFO["longitude"])
            print("="*100)
            for m in range(1, sample2+1):
                index = (lt.size(listUfosInZone)-sample2)+m
                actualUFO = lt.getElement(listUfosInZone, index)
                print("Fecha y hora: ", actualUFO["datetime"], ", Ciudad y país: ", actualUFO["city"],", ", actualUFO["country"], ", Forma: ", actualUFO["shape"], ", Duración: ", actualUFO["duration (seconds)"], ", Coordenadas (lat, long): ", actualUFO["latitude"],", ", actualUFO["longitude"])
        
            controller.sightningsMap(lonAvg,latAvg)

    else:
        sys.exit(0)
sys.exit(0)
