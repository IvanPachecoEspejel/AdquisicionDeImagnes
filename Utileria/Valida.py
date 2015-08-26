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

def imagenExistenteOnClase(imagen, clase):
    if(not clase.has_key(imagen.__hash__())):
        return False
    else: #Tomo en cuenta un error cuando el diccionario es demaciado grande y se solapan las llaves
        if imagen.__eq__(clase[imagen.__hash__()]):
            return True
        raise Exception(Util.getMnsjIdioma("Accion", "Error_Solapan_Hash"))
    
    
    