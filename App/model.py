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


# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def cmpStrings(string1, string2):
        if (string1 == string2):
                return 0
        elif (string1 > string2):
                return 1
        else:
                return -1
