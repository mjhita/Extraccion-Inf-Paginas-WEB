# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

# import scrapy
from scrapy.item import Item, Field

class ItemOSL(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    titulo = Field()
    autor = Field()
    contenido = Field()
    listaCategorias = Field()
    listaEtiquetas = Field()
    
    # Campos de información general
    url = Field()
    projecto = Field()
    spider = Field()
    server = Field()
    fecha = Field()
