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

def initCatalog(type):
   """
   Esta función inicializa el catalogo de videos
   """
   return controller.initCatalog(type)

def loadData(catalog): 
    """
    Carga los videos en la estructura de datos
    """
    controller.loadData(catalog)


#---------------------------------------------------------------------------------------------------------------------------------------
# Funciones para imprimir datos
#---------------------------------------------------------------------------------------------------------------------------------------

def printInfoCatalog(catalog):
    #El total de registros de videos cargados del archivo.

    print('La cantidad de videos cargados es: '+ str(lt.size(catalog['videos'])))

    #(title, cannel_title, trending_date, country, views, likes, dislikes).
    print('------------------------------------------------------------')

    first_element = lt.firstElement(catalog['videos'])
    print('Los datos del primer video son:')
    print('Título: '+str(first_element['title']))
    print('Nombre del canal: '+str(first_element['channel_title']))
    print('Fecha de trending: '+str(first_element['trending_date']))
    print('País: '+str(first_element['country']))
    print('Vistas: '+str(first_element['views']))
    print('Likes: '+str(first_element['likes']))
    print('Dislikes: '+str(first_element['dislikes']))
    

    #La lista de las categorías cargadas mostrando su id y nombre.
    print('------------------------------------------------------------')

    for category in lt.iterator(catalog['categories']):
        print(category['id']+' -> '+category['name'].strip())
        

def printTopViews(videos_list, country, category, number_of_videos):
    size = lt.size(videos_list[1])
    if size:
        top = 1
        print("Los "+str(number_of_videos)+ "videos con más vistas en " + country + " bajo la categoría número: "+ category +' son: \n')
        for video in lt.iterator(videos_list[1]):
            # recorre la lista del top de videos y extrae: trending_date/title/cannel_title/publish_time/views/likes/dislikes
            print(str(top)+')   Fecha de trending: '+ video['trending_date']+ '  Título: '+
                   video['title'] + '   Nombre del canal: '+video['channel_title']+
                   '    Fecha de publicación: '+video['publish_time']+' Vistas: '+video['views']+
                   '    Likes: '+video['likes']+ '  Dislikes: ' + video['dislikes'])
            top += 1 
        print('Y el tiempo trasncurrido fue de '+str(videos_list[0])+'milisegundos')
    else:
        print('Esta lista esta vacia')


catalog = None

"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
 
        print('\nSeleccione el tipo de representacion de la lista:\n1)ARRAY_LIST\n2)LINKED_LIST')

        list_type = int(input(': '))
        catalog = initCatalog(list_type)

        print("Cargando información del catálogo ....")

        loadData(catalog)
        printInfoCatalog(catalog)
   
    elif int(inputs[0]) == 2:

        country = input('Ingrese un pais: ')
        category = input('Ingrese una categoría: ')
        number_of_videos = int(input('Ingrese una cantidad n de videos con más vistas: '))

        size = lt.size(catalog['videos'])

        if number_of_videos > size:
            print('\nLa cantidad de videos seleccionados supera la cantidad de videos cargados\n')
        
        else: 
            filtered_videos = controller.filterCategoryCountry(catalog, category, country)
            #Luego de haber filtrado los datos por ciudad y categoria se ordenan los datos según lo que indica el usuario
            print('Seleccione el tipo de ordenamiento iterativo que desea ejecutar')
            ordering = int(input('1)Selection\n2)Insertion\n3)Shell\n: '))
            
            if ordering == 1:
                result = controller.sortTopViews(filtered_videos, 'selectionsort')
            elif ordering == 2:
                result = controller.sortTopViews(filtered_videos, 'insertionsort')
            elif ordering == 3:
                result = controller.sortTopViews(filtered_videos, 'shellsort')

            printTopViews(result, country, category, number_of_videos)

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

    #
sys.exit(0)
