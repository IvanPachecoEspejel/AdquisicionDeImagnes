'''
Created on 23/08/2015

@author: ivan
'''

from ConfigParser import SafeConfigParser, RawConfigParser
import os
import logging.config

##########################################################################

cfgIdioma = RawConfigParser()
cfgIdioma.read('..'+os.path.sep+'MensajesIdioma.conf')

cfgModulo = RawConfigParser()
cfgModulo.read('..'+os.path.sep+'Configuracion.conf')

logging.config.fileConfig('..'+os.path.sep+'logging.conf')

##########################################################################
    
#---------------------------------------------------------------------------
def getMnsjIdioma(seccion, attr):
    '''Funcion que regresa el valor de un atributo de una seccion especifica 
        del archivo MensajesIdioma.conf'''
    return cfgIdioma.get(seccion, attr)

#---------------------------------------------------------------------------
def getMnsjConf(seccion, attr):
    '''Funcion que regresa el valor de un atributo de una seccion especifica 
        del archivo cfgModulo1.conf'''
    return cfgModulo.get(seccion, attr)

#---------------------------------------------------------------------------
def getLogger(nombre):
    return logging.getLogger(nombre)
        

##########################################################################

if __name__ == '__main__':
    logger = getLogger("Util")
    logger.info("Hola mundo Pureba logger")
    
    logger.info("TEST CONFIG MENSAJE")
    print getMnsjConf("Validacion", "Extenciones")
    
    logger.info("TEST IDIOMA MENSAJE")
    print getMnsjIdioma("Imagen", "Error_Ruta_Invalida")
    
    
