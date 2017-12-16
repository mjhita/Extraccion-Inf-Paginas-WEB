# -*- coding: utf-8 -*-

############################################################################
#
# Curso Tratamiento de datos, juegos y programación gráfica en Python
#
# TEMA: Extracción de información de páginas WEB
# Tarea: Dame Posts y te diré de quienes son. 
#
# Definición del modelo para extracción de Items
#
# Implementado por: Manuel Jesús Hita Jiménez - 2017
#
############################################################################

from scrapy.item import Item, Field

class ItemOSL(Item):
    # Definición de campos que extraer
    titulo = Field()
    autor = Field()
    contenido = Field()
    listaCategorias = Field()
    listaEtiquetas = Field()
    
 
