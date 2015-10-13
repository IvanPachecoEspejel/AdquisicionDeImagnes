'''
Created on 22/08/2015
@author: ivan
'''

import os
import ttk

import Clasifica as Clasifica
import Util as Util
from Utileria.Fila import Fila
import Valida as Valida


#################################################################################################
logger = Util.getLogger("Imagen")
#################################################################################################
class Imagen(object):
    ''' Objeto que abstrae las caracteristicas y funcionalidades de una rutade imagen local o web '''
    
    #------------------------------------------------------------------------------------
    def __init__(self, source, widgetTabla=None, nomClaseCorrecto = None):
        
        if not Valida.isImagen(source):
            raise Exception(Util.getMnsjIdioma("Imagen", "Error_Ruta_Invalida")%(source))
        
        self.source = source
        self.tipoRuta = Clasifica.tipoRuta(source);
        self.nomClaseCorrecto = nomClaseCorrecto
        if widgetTabla is not None: # Para realizar pruebas unitaras
            self.widgetFila = Fila(self, widgetTabla)
            
    
    #------------------------------------------------------------------------------------
    def getPath(self):
        '''Regresa la ruta sin el arhcivo'''
        if self.tipoRuta == Util.RUTA_WEB:
            return self.source[:self.source.rfind('/')]
        
        elif self.tipoRuta == Util.RUTA_LOCAL:
            return self.source[:self.source.rfind(os.path.sep)]
        
        return None;
    
    #------------------------------------------------------------------------------------
    def getNomArchivo(self):
        '''Regresa el nombre del archvio sin extencion ni ruta'''
        
        if self.tipoRuta == Util.RUTA_WEB:
            return self.source[self.source.rfind('/')+1:self.source.rfind('.')]
        
        elif self.tipoRuta == Util.RUTA_LOCAL:
            return self.source[self.source.rfind(os.path.sep)+1:self.source.rfind('.')]
        
        return None;
    
    #------------------------------------------------------------------------------------
    def getExtArchivo(self):
        '''Regresa la extencion del archivo sin el '.' '''
        return self.source[self.source.rfind('.')+1:]
    
    #------------------------------------------------------------------------------------
    def guardarImagen(self, direccionSalida):
        try:
            if self.widgetFila.widgetPrevisualizacion is not None and self.widgetFila.widgetPrevisualizacion.__class__ == ttk.Label:
                self.widgetFila.widgetPrevisualizacion.save(direccionSalida)
            else:
                self.widgetFila.crearIconoImagen().save(direccionSalida)
            logger.info("Imagen Guardada en "+direccionSalida)
        except IOError as ex:
            logger.error(ex)
            logger.error("No se pudo guardar la imagen "+self.source)
            
    
            
    #------------------------------------------------------------------------------------
    def __eq__(self, imagen):
        '''Regresa la comparacion entre otro objeto del mismo tipo'''
        return self.source == imagen.source and self.nomClaseCorrecto == imagen.nomClaseCorrecto;

    #------------------------------------------------------------------------------------
    def __hash__(self):
        return hash(str(self.nomClaseCorrecto)+self.source)
    
#################################################################################################
if __name__ == "__main__":
    
    logger.info("Unit tests for Imagen class")
    
#     logger.info("TEST FOR PATH FROM THE WEB")
#     prueba = Imagen("http://blogs.computing.dcu.ie/wordpress/brogand2/wp-content/uploads/sites/183/2015/03/config-parser1.png")
#     print(prueba.getPath())
#     print(prueba.getNomArchivo())
#     print(prueba.getExtArchivo())
    
    logger.info("TEST FOR PATH OF A FILE OF A PC")
    prueba2 = Imagen("/home/ivan/Imagenes/fondos/02E3A832D.jpg")
    prueba2.guardarImagen("/home/ivan/Imagenes/fondos/02E3A832D.png")
    print(prueba2.getPath())
    print(prueba2.getNomArchivo())
    print(prueba2.getExtArchivo())