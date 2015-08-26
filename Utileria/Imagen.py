'''
Created on 22/08/2015
@author: ivan
'''

import os

import Util as Util
import Valida as Valida
import Clasifica as Clasifica

logger = Util.getLogger("Imagen")

class Imagen(object):
    ''' Objeto que abstrae las caracteristicas y funcionalidades de una rutade imagen local o web '''

    def __init__(self, source, nomClase = None):
        if Valida.isImagen(source):
            self.source = source
            self.tipoRuta = Clasifica.tipoRuta(source);
            self.nomClase = nomClase
        else:
            raise Exception(Util.getMnsjIdioma("Imagen", "Error_Ruta_Invalida"))
        
    def getPath(self):
        '''Regresa la ruta sin el arhcivo'''
        if self.tipoRuta == Clasifica.RUTA_WEB:
            return self.source[:self.source.rfind('/')]
        
        elif self.tipoRuta == Clasifica.RUTA_LOCAL:
            return self.source[:self.source.rfind(os.path.sep)]
        
        return None;
        
    def getNomArchivo(self):
        '''Regresa el nombre del archvio sin extencion ni ruta'''
        
        if self.tipoRuta == Clasifica.RUTA_WEB:
            return self.source[self.source.rfind('/')+1:self.source.rfind('.')]
        
        elif self.tipoRuta == Clasifica.RUTA_LOCAL:
            return self.source[self.source.rfind(os.path.sep)+1:self.source.rfind('.')]
        
        return None;
    
    def getExtArchivo(self):
        '''Regresa la extencion del archivo sin el '.' '''
        return self.source[self.source.rfind('.')+1:]
    
    def __eq__(self, imagen):
        '''Regresa la comparacion entre otro objeto del mismo tipo'''
        return self.source == imagen.source and self.nomClase == imagen.nomClase;
    
    def __hash__(self):
        return hash(str(self.nomClase)+self.source)
    
if __name__ == "__main__":
    
    logger.info("Unit tests for Imagen class")
    
    logger.info("TEST FOR PATH FROM THE WEB")
    prueba = Imagen("http://blogs.computing.dcu.ie/wordpress/brogand2/wp-content/uploads/sites/183/2015/03/config-parser1.png")
    print(prueba.getPath())
    print(prueba.getNomArchivo())
    print(prueba.getExtArchivo())
    
    logger.info("TEST FOR PATH OF A FILE OF A PC")
    prueba2 = Imagen("/home/ivan/Imagenes/fondos/02E3A832D.jpg")
    print(prueba2.getPath())
    print(prueba2.getNomArchivo())
    print(prueba2.getExtArchivo())