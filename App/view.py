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
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Videos con más views en un país")
    print("3- Video con más tiempo en trending en un país")
    print("4- Video con más tiempo en trending para una categoria")
    print("5- Videos con más likes en un país")
    print("6- Cerrar programa")

def initCatalog():
   """
   Esta función inicializa el catalogo de videos
   """
   return controller.initCatalog()

def loadData(catalog): 
    """
    Carga los videos en la estructura de datos
    """
    controller.loadData(catalog)


catalog = None

"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información del catálogo ....")
        catalog = initCatalog()
        loadData(catalog)
        #El total de registros de videos cargados del archivo.
        print('La cantidad de videos cargados es: '+ str(lt.size(catalog['videos'])))
        print('------------------------------------------------------------')
        #(title, cannel_title, trending_date, country, views, likes, dislikes).
        first_element = lt.firstElement(catalog['videos'])
        print('Los datos del primer video son:')
        print('Título: '+str(first_element['title']))
        print('Nombre del canal: '+str(first_element['channel_title']))
        print('Fecha de trending: '+str(first_element['trending_date']))
        print('País: '+str(first_element['country']))
        print('Vistas: '+str(first_element['views']))
        print('Likes: '+str(first_element['likes']))
        print('Dislikes: '+str(first_element['dislikes']))
        print('------------------------------------------------------------')
        #La lista de las categorías cargadas mostrando su id y nombre.
        position = 1
        while position <= lt.size(catalog['categories']):
            element = lt.getElement(catalog['categories'], position)
            print(str(element['idname']))
            """
            Preguntar en Cupitaller esta monda
            """
            position += 1

        
    elif int(inputs[0]) == 2:
        country = input('Ingrese un pais')
        print("Los videos con más likes en " + country + "son:")

    elif int(inputs[0]) == 3:
        country = input('Ingrese un pais')
        print("Los videos con más tiempo en trending en " + country + "son:")

    elif int(inputs[0]) == 4:
        categoria = input('Ingrese una categoria')
        print("El video con más tiempo en trending para una la categoria:" + categoria )

    elif int(inputs[0]) == 5:
        country = input('Ingrese un pais')
        print("Los videos con más likes en " + country * "son:")

    else:
        sys.exit(0)
sys.exit(0)
