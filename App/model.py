"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as ms
from datetime import datetime
from DISClib.ADT import orderedmap as om
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
        catalog = {"ufos": None}

        catalog["ufos"] = lt.newList("ARRAY_LIST")
        catalog["cities"] = om.newMap(omaptype="RBT", comparefunction=cmpStrings)
        catalog["hours"] = om.newMap(omaptype="RBT", comparefunction=cmpHours)

        return catalog

def addUFO(catalog, ufo):
        lt.addLast(catalog["ufos"], ufo)

        city = ufo["city"]
        isPresent = om.contains(catalog["cities"], city)
        if isPresent == True:
                listCities = om.get(catalog["cities"], city)["value"]
                lt.addLast(listCities, ufo)
                om.put(catalog["cities"], city, listCities)
        else:
                listCities = lt.newList('ARRAY_LIST')
                lt.addLast(listCities, ufo)
                om.put(catalog["cities"], city, listCities)

        datetime = ufo["datetime"]
        hour = datetime[11:19]
        isPresent = om.contains(catalog["hours"], hour)
        if isPresent == True:
                listHours = om.get(catalog["hours"], hour)["value"]
                lt.addLast(listHours, ufo)
                om.put(catalog["hours"], hour, listHours)
        else:
                listHours = lt.newList('ARRAY_LIST')
                lt.addLast(listHours, ufo)
                om.put(catalog["hours"], hour, listHours)


# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta
def ufosByCity(catalog, city):
        cityUfosList = om.get(catalog["cities"], city)["value"]
        ms.sort(cityUfosList, cmpDateHour)        

        return cityUfosList

def ufosByHour(catalog, hour0, hour1):
        hoursTree = catalog["hours"]
        filtredValues = om.values(hoursTree, hour0, hour1) #Lista de listas

        for y in range(1, lt.size(filtredValues)+1):
                actualHour = lt.getElement(filtredValues, y)
                ms.sort(actualHour, cmpDateHour)

        return filtredValues

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpDateHour(ufo1, ufo2):
        datetime1str = ufo1["datetime"]
        datetime2str = ufo2["datetime"]
        time1 = datetime.strptime(datetime1str, "%Y-%m-%d %H:%M:%S")
        time2 = datetime.strptime(datetime2str, "%Y-%m-%d %H:%M:%S")

        return time1 < time2

# Funciones de ordenamiento
def cmpStrings(string1, string2):
        if (string1 == string2):
                return 0
        elif (string1 > string2):
                return 1
        else:
                return -1

def cmpHours(hour1, hour2):
        time1 = datetime.strptime(hour1, "%H:%M:%S")
        time2 = datetime.strptime(hour2, "%H:%M:%S")
        if (time1 == time2):
                return 0
        elif (time1 > time2):
                return 1
        else:
                return -1


