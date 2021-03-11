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
from DISClib.Algorithms.Sorting import insertionsort as insertionsort
from DISClib.Algorithms.Sorting import selectionsort as selectionsort
from DISClib.Algorithms.Sorting import shellsort as shellsort
assert cf
import time

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
#---------------------------------------------------------------------------------------------------------------------------------------
# Construccion de modelos
#---------------------------------------------------------------------------------------------------------------------------------------


def newCatalog(type):
    """
    Inicializa el catalogo de videos, crea una lista vacia para guardar:
    - Todos los videos
    - Las Categorias de los videos
    """
    catalog = {'videos': None,
               'categories': None}

    catalog['videos'] = lt.newList(type)
    catalog['categories'] = lt.newList(type)

    return catalog


#---------------------------------------------------------------------------------------------------------------------------------------
# Funciones para agregar informacion al catalogo
#---------------------------------------------------------------------------------------------------------------------------------------


def addVideoInfo(catalog, line):
    #Se adiciona la line del video a la lista de videos
    lt.addLast(catalog['videos'],line)
    
def addCategory(catalog, line):
    #Se adiciona la line del video a la lista de videos
    lt.addLast(catalog['categories'],line)
    
#---------------------------------------------------------------------------------------------------------------------------------------
# Funciones para creacion de datos
#---------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------
# Funciones de consulta
#---------------------------------------------------------------------------------------------------------------------------------------


def filterCategoryCountry(catalog, category, country):
    videos = catalog['videos']

    filtered_videos = lt.newList()
    for video in lt.iterator(videos):
        if (video['category_id']== category) and (video['country']==country):
            
            lt.addLast(filtered_videos,video)
    return filtered_videos

def filterCategory(catalog, category):
    videos = catalog['videos']

    filtered_videos = lt.newList(cmpfunction= cmpVideosByViews)
    for video in lt.iterator(videos):
        if (video['category_id']== category):

            lt.addLast(filtered_videos,video)
    return filtered_videos



#---------------------------------------------------------------------------------------------------------------------------------------
# Funciones utilizadas para comparar elementos dentro de una lista
#---------------------------------------------------------------------------------------------------------------------------------------


def cmpVideosByViews(video_1,video_2):
    return ((int(video_1['views']))>(int(video_2['views'])))


#---------------------------------------------------------------------------------------------------------------------------------------
# Funciones de ordenamiento
#---------------------------------------------------------------------------------------------------------------------------------------

def sortTopViews(filtered_videos, sort):
    start_time = time.process_time()
    if sort == 1:
        print("Insertion sort efectuandose")
        sorted_videos = insertionsort.sort(filtered_videos, cmpVideosByViews)
    elif sort == 2:
        sorted_videos = selectionsort.sort(filtered_videos, cmpVideosByViews)
    elif sort == 3:
        sorted_videos = shellsort.sort(filtered_videos, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_videos

def sortVideosCategory(filtered_videos):
    sorted_videos = shellsort.sort(filtered_videos, cmpVideosByViews)
    return sorted_videos

