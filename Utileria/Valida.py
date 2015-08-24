'''
Created on 22/08/2015

@author: ivan
'''



import Util as Util

logger = Util.getLogger("Valida")

def isImagen(sourceRuta):
    '''Valida si la ruta del archivo pertenece a una imagen'''
    extension =  sourceRuta[sourceRuta.rfind('.')+1:]
    return extension in Util.getMnsjConf('Validacion', 'Extenciones')
  
if __name__ == "__main__":
        
    logger.info("Pruebas unitaras para function's Valida")
    logger.info("TEST FOR def isImagen(sourceRuta):")
    print (isImagen("adfasdf.jpg"));
    
    
    