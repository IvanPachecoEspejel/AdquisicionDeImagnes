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

def imagenExistente(imagen, clase):
    if(clase[imagen.__hash__()] is None):
        return False
    else:
        if imagen.__eq__(clase[imagen.__hash__()]):
            return True
        raise Exception(Util.getMnsjIdioma("Accion", "Error_Solapan_Hash"))
  
if __name__ == "__main__":
        
    logger.info("Pruebas unitaras para function's Valida")
    logger.info("TEST FOR def isImagen(sourceRuta):")
    print (isImagen("adfasdf.jpg"));
    
    
    