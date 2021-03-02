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
#---------------------------------------------------------------------------------------------------------------------------------------
# Inicialización del Catálogo de videos
#---------------------------------------------------------------------------------------------------------------------------------------


def initCatalog(type):
    """
    Llama a la función de inicializacion del catalogo del modelo
    """
    catalog = model.newCatalog(type)
    return catalog


#---------------------------------------------------------------------------------------------------------------------------------------
#Funciones para la carga de datos
#---------------------------------------------------------------------------------------------------------------------------------------


def loadData(catalog):
    """
    Carga los datos de los archivos y los carga los datos en la estructura de datos
    """
    loadVideos(catalog)
    loadCategories(catalog)

def loadVideos(catalog):
    """
    Carga los videos del archivo. Por cada libro se toman el título, nombre del canal, fecha de trending, país, vistas, likes, dislikes
    """
    videos_file = cf.data_dir + 'videos/videos-small.csv'
    input_file = csv.DictReader(open(videos_file, encoding='utf-8'))
    for line in input_file:
        model.addVideoInfo(catalog, line) 

def loadCategories(catalog):
    """
    Carga los videos del archivo. Por cada libro se toman el título, nombre del canal, fecha de trending, país, vistas, likes, dislikes
    """
    videos_file = cf.data_dir + 'videos/category-id.csv'
    input_file = csv.DictReader(open(videos_file, encoding='utf-8'))
    for line in input_file:
        model.addCategory(catalog, line) 

 
 #---------------------------------------------------------------------------------------------------------------------------------------
 #Funciones para la busqueda sobre el catalogo
 #---------------------------------------------------------------------------------------------------------------------------------------


def getTopViews(catalog, number_of_videos):
    """ 
    Retorna los videos con mas vistas
    """
    topViews = model.getTopViews(catalog, number_of_videos)
    return topViews