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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog():
    return model.newCatalog()

def loadData(catalog, sample):
    if sample == 1:
        file = "-small"
    elif sample == 2:
        file = "-5pct"
    elif sample == 3:
        file = "-10pct"
    elif sample == 4:
        file = "-20pct"
    elif sample == 5:
        file = "-30pct"
    elif sample == 6:
        file = "-50pct"
    elif sample == 7:
        file = "-80pct"
    elif sample == 8:
        file = "-large"

    ufosFile = cf.data_dir + "UFOS-utf8" + file + ".csv"
    input_file = csv.DictReader(open(ufosFile, encoding='utf-8'))
    for ufo in input_file:
        model.addUFO(catalog, ufo)

# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def ufosByCity(catalog, city):

    return model.ufosByCity(catalog, city)

def ufosByHour(catalog, hour0, hour1):

    return model.ufosByHour(catalog, hour0, hour1)
