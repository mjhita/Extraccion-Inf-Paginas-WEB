# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
import sys
import re
from scrapy.exceptions import DropItem
from scrapy.exceptions import CloseSpider
from paginaHTML import PaginaHtml
def crearTablaHTML(esConEtiquetas):
    try:
        if esConEtiquetas:
            fichJson = codecs.open('OSL.json', 'r', encoding = 'utf-8')
        else:
            fichJson = codecs.open('OSLSinEtiquetas.json', 'r', encoding = 'utf-8')        
    except IOError as e:
        print "Error abriendo archivo Json para generar tabla en HTML ({0}): {1}".format(e.errno, e.strerror)
        return ""
    except:
        print "Error inexperado abriendo archivo Json para generar tabla en HTML:", sys.exc_info()[0]
        return ""
    else:
        contenidofichero = "[" + fichJson.read() + "]"
        contenidofichero = re.sub("}{", "},{",contenidofichero)
        #tabla = json.loads(fichJson.read())
        fichJson.close()
        tabla = json.loads(contenidofichero)
        
        tablaHTML = '<table class="osl"> \n'
        tablaHTML += '<thead> \n'
        tablaHTML += '<tr> \n'   
        tablaHTML += '<th>Titulo</th><th>Autor</th><th>Descripcion</th> \n'
        tablaHTML += '</tr> \n'
        tablaHTML += '</thead> \n'
        tablaHTML += '<tbody> \n'
        for fila in tabla:
           tablaHTML += '<tr> \n'
           titulo = (fila['titulo'][0]).encode('utf-8')
           if len(fila['autor']):
               autor =  (fila['autor'][0]).encode('utf-8')
           else:
               autor = ""
           if len(fila['contenido']):
               contenido = (fila['contenido'][0]).encode('utf-8')
           else:
               contenido = ""
           tablaHTML += "<td>" + titulo + "</td><td>" + autor + "</td><td>" + contenido + "</td>"
           tablaHTML += '</tr> \n'
        tablaHTML += '</tbody> \n'
        tablaHTML += '</table> \n'
        return tablaHTML


def crearTablasHTML():
  
    html = PaginaHtml("Tabla OSL con etiquetas")   
    html.insertar_estilo_tabla_1('osl')
    tabla = crearTablaHTML(True)
    if tabla:
        html.insertar_contenido(tabla)
        try:
            with open("OSL.html", "w") as f:
                f.write(html.crear_pagina())       
        except IOError as e:
            print "Error I/O ({0}): {1}".format(e.errno, e.strerror)
        except:
            print "Error inexperado:", sys.exc_info()[0]
                
    htmlSin = PaginaHtml("Tabla OSL sin etiquetas")   
    htmlSin.insertar_estilo_tabla_1('osl')
    tablaSin = crearTablaHTML(False)
    if tablaSin:
        htmlSin.insertar_contenido(tablaSin)
        try:
            with open("OSLSinEtiquetas.html", "w") as f:
                f.write(htmlSin.crear_pagina())       
        except IOError as e:
            print "Error I/O ({0}): {1}".format(e.errno, e.strerror)
        except:
            print "Error inexperado:", sys.exc_info()[0]

class ExtraccionInfPaginasWEBJsonPipeline(object):

    def open_spider(self, spider):
        try:
            self.fichero = codecs.open('OSL.json', 'w', encoding = 'utf-8')
            #self.fichero.write("[")
        except:
            raise CloseSpider("No se ha podido crear el archivo JSON con los Post") 
        try: 
            self.ficheroSinEtiquetas = codecs.open('OSLSinEtiquetas.json', 'w', encoding = 'utf-8')
            #self.ficheroSinEtiquetas.write("[")
        except:
            raise CloseSpider("No se ha podido crear el archivo JSON con los Post sin etiquetas")        

    def close_spider(self, spider):
        try:
            #self.fichero.write("]")
            self.fichero.close()
        except:
            raise CloseSpider("No se ha podido cerrar el archivo JSON con los Post")
        try:
            #self.ficheroSinEtiquetas.write("]")
            self.ficheroSinEtiquetas.close()
        except:
            raise CloseSpider("No se ha podido cerrar el archivo JSON con los Post sin etiquetas")
        crearTablasHTML()

    
    def process_item(self, item, spider):
        if item['titulo']:
            line = json.dumps(dict(item), ensure_ascii=False) 
            if item['listaEtiquetas'] and len(item['listaEtiquetas']) > 0:
                self.fichero.write(line)
            else:
                self.ficheroSinEtiquetas.write(line)
            return item
        else:
            raise DropItem("Falta el título del post")
