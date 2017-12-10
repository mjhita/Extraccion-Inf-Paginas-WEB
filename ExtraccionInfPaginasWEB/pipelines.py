# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
from scrapy.exceptions import DropItem
from scrapy.exceptions import CloseSpider

class ExtraccionInfPaginasWEBJsonPipeline(object):

    def open_spider(self, spider):
        try:
            self.fichero = codecs.open('OSL.json', 'w', encoding = 'utf-8')
        except:
            raise CloseSpider("No se ha podido crear el archivo JSON con los Post") 
        try: 
            self.ficheroSinEtiquetas = codecs.open('OSLSinEtiquetas.json', 'w', encoding = 'utf-8')
        except:
            raise CloseSpider("No se ha podido crear el archivo JSON con los Post sin etiquetas")        

    def close_spider(self, spider):
        try:
            self.fichero.close()
        except:
            raise CloseSpider("No se ha podido cerrar el archivo JSON con los Post") 
        try:
            self.ficheroSinEtiquetas.close()
        except:
            raise CloseSpider("No se ha podido cerrar el archivo JSON con los Post sin etiquetas")    

    
    def process_item(self, item, spider):
        if item['titulo']:
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            if item['listaEtiquetas'] and len(item['listaEtiquetas']) > 0:
                self.fichero.write(line)
            else:
                self.ficheroSinEtiquetas.write(line) 
            return item
        else:
            raise DropItem("Falta el título del post")


class ExtraccionInfPaginasWEBTablaHTMLPipeline(object):
    def PonerInicioHTML(esConEtiqueta):
        if esConEtiqueta:
            fichero = self.fichero
        else:
            fichero = self.ficheroSinEtiquetas
        fichero.write('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//ES"> \n')
        fichero.write('<html> \n')
        fichero.write('<head> \n')
        if esConEtiqueta:
            fichero.write('<title>Tabla de post de osl.ugr.es </title> \n') 
        else: 
            fichero.write('<title>Tabla de post sin etiquetas de osl.ugr.es </title> \n') 
        fichero.write('<style> \n')
        fichero.write('table.osl { width : 100%; } \n')
        fichero.write('table, th, td { border: 1px solid black; border-collapse:collapse; } \n ')
        fichero.write('th, td { padding: 5px; } \n')
        fichero.write('th { text-align: center; } \n')
        fichero.write('table tr:nth-child(even) { background-color: #eee; } \n')
        fichero.write('table tr:nth-child(odd) { background-color: #fff; } \n')
        fichero.write('table th { background-color: black; color: white; } \n')
        fichero.write('</style> \n')
        fichero.write('</head> \n')
        fichero.write('<body> \n')
        fichero.write('<table class="osl"> \n')
        fichero.write('<thead> \n')
        fichero.write('<tr> \n')
        if esConEtiqueta:
            fichero.write('<th>Titulo</th><th>Autor</th><th>Categorias</th><th>Etiquetas</th> \n')
        else:
            fichero.write('<th>Titulo</th><th>Autor</th><th>Categorias</th> \n')
        fichero.write('</tr> \n')
        fichero.write('</thead> \n')
        fichero.write('<tbody> \n')

    def PonerFinHTML(esConEtiqueta):
        if esConEtiqueta:
            fichero = self.fichero
        else:
            fichero = self.ficheroSinEtiquetas
        fichero.write('</tr> \n')
        fichero.write('</tbody> \n')
        fichero.write('</table> \n')
        fichero.write('</body> \n')
        fichero.write('</html> \n')

 
    def open_spider(self, spider):
        try:
            self.fichero = open('OSL.html', 'w')
            self.PonerInicioHTML(True)
        except:
            pass #raise CloseSpider("No se ha podido crear el archivo HTML con los Post") 
        try: 
            self.ficheroSinEtiquetas = open('OSLSinEtiquetas.html', 'w')
            self.PonerInicioHTML(False)
        except:
            pass #raise CloseSpider("No se ha podido crear el archivo HTML con los Post sin etiquetas")        

    def close_spider(self, spider):
        try:
            self.PonerFinHTML(True)
            self.fichero.close()
        except:
            pass# raise CloseSpider("No se ha podido cerrar el archivo HTML con los Post") 
        try:
            self.PonerFinHTML(False)
            self.ficheroSinEtiquetas.close()
        except:
            pass# raise CloseSpider("No se ha podido cerrar el archivo HTML con los Post sin etiquetas")        

    def process_item(self, item, spider):
        if item['titulo']:    
            if item['listaEtiquetas'] and len(item['listaEtiquetas']) > 0:
                
                self.fichero.write('<tr> \n')
                self.fichero.write("<td>" + item['titulo'] + "</td><td>" + item['autor'] + "</td><td>" + item['listaCategorias']+ "</td><td>" + item['listaEtiquetas']+ "</td> \n")
                self.fichero.write('</tr> \n') 
            else:
                self.ficheroSinEtiquetas.write('<tr> \n')
                self.ficheroSinEtiquetas.write("<td>" + item['titulo'] + "</td><td>" + item['autor'] + "</td><td>" + item['listaCategorias']+ "</td> \n")
                self.ficheroSinEtiquetas.write('</tr> \n')
            return item
        else:
            raise DropItem("Falta el título del post")


