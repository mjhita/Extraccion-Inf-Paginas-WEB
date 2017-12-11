#!/usr/bin/python
# coding: UTF-8

############################################################################
#
# 
# Generación de página HTML
#
# Basado en el proyecto del curso Introduccion al lenguaje de programación
# Python
# 
# Implementado por: Manuel Jesús Hita Jiménez - 2017
#
############################################################################

class PaginaHtml:
    """
    Esta clase permite generar el contenido de un archivo HTML en forma de
    cadena, con funciones para:
       - poner el título de la página en HTML
       - pasar referencias a hojas de estilo
       - definir estilos dentro de la página en HTML
       - insertar tablas
       - insertar cualquier contenido
    """
    def __init__(self,titulo ="", body = ""):
        self.doctype = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//ES">'
        self.title = titulo
        self.style = ""
        self.body = body
        self.stylesheet = ""

    def poner_titulo(self, titulo):
        """ Pone el titulo de la página HTML
        """
        self.title = titulo
             
    def poner_hoja_estilo(self, hoja_estilo):
        """ Permite pasar una hoja de estilo css

            Parámetros:
            ==========
            hoja_estilo: str
                         Nombre del archivo css, con las opciones de estilo
            
            Nota: no se usa en el ejemplo
        """
        self.stylesheet = hoja_estilo
   
    def insertar_estilo(self, estilo):
        """ Permite insertar estilos de visualización para la página HTML

            Parámetros:
            ==========
            estilo: str
                    Cadena con opciones de estilo de visualización
            
            Va concatenando las distintas inserciones en la cadena 'style'
        """        
        self.style += estilo
                  
    def insertar_contenido(self, contenido):
        """ Permite insertar cualquier contenido dentro del cuerpo de la página HTML:
            párrafos, tablas ...

            Parámetros:
            ==========
            contenido: str
                       Cadena con el contenido que se va a insertar.


            Va concatenando los distintos contenidos en la cadena 'body'
        """
            
        self.body += contenido;
     
    def crear_cabecera(self):
        """ Genera el texto necesario para la cabecera en formato HTLM

            Returns
            =======
            str: Devuelve una cadena con la cabecera HTML
        """
        cabecera = '<head>\n'
        cabecera += '<title>'+ self.title + '</title>\n'
        if self.stylesheet != "":
            cabecera += '<link rel="stylesheet" type="text/css" href="' + self.stylesheet + '">\n'
        if self.style != "":
            cabecera += '<style>\n' + self.style + ' </style>\n' 
        cabecera += '</head>\n'
        return cabecera
    
    def crear_pagina(self):
        """ Genera el contenido completo de la página HTLM
            Concatena las distintas partes de la página en la cadena 'pagina'

            Returns
            =======
            str: Devuelve una cadena con todo el contenido de la página en HTML
        """
        pagina = self.doctype + '\n'
        pagina += '<html>\n'
        pagina += self.crear_cabecera()
        pagina += '<body>\n'
        pagina += self.body
        pagina += '</body>\n'
        pagina += '</html>\n'
        return pagina
   
    def insertar_estilo_tabla_1(self, nombre_tabla):
        """ Define un estilo por defecto de tabla para la tabla "nombre_tabla".
            Es una opción "prefabricada" de presentación por defecto.
            Permite visualizar la tabla con un formato "agradable" sin trabajo adicional
            Se pueden definir otros métodos en la clase con estilos distintos o insertar los
            estilos desde fuera de la clase
        """
        self.insertar_estilo('table.' + nombre_tabla + ' { width : 100%; } \n')
        self.insertar_estilo('table, th, td { border: 1px solid black; border-collapse:collapse; } \n')
        self.insertar_estilo('th, td { padding: 5px; } \n')
        self.insertar_estilo('th { text-align: center; }\n')
        self.insertar_estilo('table tr:nth-child(even) { background-color: #eee; }\n')
        self.insertar_estilo('table tr:nth-child(odd) { background-color: #fff; }\n')
        self.insertar_estilo('table th { background-color: black; color: white; }\n')

