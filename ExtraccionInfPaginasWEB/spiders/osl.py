# -*- coding: utf-8 -*-
############################################################################
#
# Curso Tratamiento de datos, juegos y programación gráfica en Python
#
# TEMA: Extracción de información de páginas WEB
# Tarea: Dame Posts y te diré de quienes son. 
#
# Definición del Spider para la extracción de los post en dos direcciones,
# obtiene todos los post, ya que va volcando los de las páginas anteriores.
# Es recomendable usar CLOSESPIDER_ITEMCOUNT al hacer scrapy crawl, para
# limitar el número de post cargados.
#
# Por ejemplo:
#       scrapy crawl osl -s CLOSESPIDER_ITEMCOUNT=20
#
# Implementado por: Manuel Jesús Hita Jiménez - 2017
#
############################################################################
import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from  ExtraccionInfPaginasWEB.items import ItemOSL


class OslSpider(CrawlSpider):
    name = 'osl'
    allowed_domains = ['ugr.es']
    start_urls = ['http://osl.ugr.es/'] 

    rules = (
        #Rule(LinkExtractor(restrict_xpaths='//*[starts-with(@id,"post-")]'), callback='parse_item'))
        Rule(LinkExtractor(restrict_xpaths='//*[@class="nav-previous"]')), 
        Rule(LinkExtractor(restrict_xpaths='//*[starts-with(@id,"post-")]'), callback='parse_item')
        )

    def parse_item(self, response):
        itemOSL = ItemOSL()
        itemOSL['titulo'] = response.xpath('//*[starts-with(@id,"post-")]/header/h1/text()').extract()
        itemOSL['autor'] = response.xpath('//*[starts-with(@id,"post-")]/header/div/span/span/a/text()').extract() 
        contenido = response.xpath('//*[starts-with(@id,"post-")]/section').extract()
        nuevoContenido = re.sub("<(.*?)>", "",contenido[0])
        nuevoContenido = re.sub("(\\r|\\n)", "", nuevoContenido) 
        nuevoContenido = re.sub("\\xa0(\d*)","",nuevoContenido)    
        contenido[0] = nuevoContenido    
        itemOSL['contenido'] = contenido
        itemOSL['listaCategorias'] = response.xpath('//*[starts-with(@id,"post-")]/header/div/a[@class="btn btn-mini btn-tag"]/text()').extract()
        itemOSL['listaEtiquetas'] = response.xpath('//*[starts-with(@id,"post-")]/header/div/a[@class="btn btn-mini"]/text()').extract()   
        return itemOSL

