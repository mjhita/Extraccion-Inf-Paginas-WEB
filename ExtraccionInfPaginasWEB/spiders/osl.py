# -*- coding: utf-8 -*-
############################################################################
#
# Curso Tratamiento de datos, juegos y programación gráfica en Python
#
# TEMA: Extracción de información de páginas WEB
# Tarea: Dame Posts y te diré de quienes son. 
#
# Definición del Spider para la extracción de los post
#
# Implementado por: Manuel Jesús Hita Jiménez - 2017
#
############################################################################

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from  ExtraccionInfPaginasWEB.items import ItemOSL


class OslSpider(CrawlSpider):
    name = 'osl'
    allowed_domains = ['ugr.es']
    # Pruebo esta página que contiene post con etiquetas
    start_urls = ['http://osl.ugr.es/page/2/'] 


    rules = (
        Rule(LinkExtractor(restrict_xpaths='//*[starts-with(@id,"post-")]'), callback='parse_item'),
    )

    def parse_item(self, response):
        itemOSL = ItemOSL()
        itemOSL['titulo'] = response.xpath('//*[starts-with(@id,"post-")]/header/h1/text()').extract()
        itemOSL['autor'] = response.xpath('//*[starts-with(@id,"post-")]/header/div/span/span/a/text()').extract()
        itemOSL['contenido'] = response.xpath('//*[starts-with(@id,"post-")]/section/p/text()').extract()
        itemOSL['listaCategorias'] = response.xpath('//*[starts-with(@id,"post-")]/header/div/a[@class="btn btn-mini btn-tag"]/text()').extract()
        itemOSL['listaEtiquetas'] = response.xpath('//*[starts-with(@id,"post-")]/header/div/a[@class="btn btn-mini"]/text()').extract()   
        return itemOSL

