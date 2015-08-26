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
    if(clase.get(imagen.__hash__()) in (None, [])):
        return False
    else:
        if imagen.__eq__(clase[imagen.__hash__()]):
            return True
        #Tomo en cuenta un error cuando el diccionario es demaciado grande y se solapan las llaves
        raise Exception(Util.getMnsjIdioma("Accion", "Error_Solapan_Hash"))

def nomClase(nomClase):
    return nomClase is None 
    
def exitenciaClase(nomClase, clases):
    if clases.get(nomClase) in (None, []):
        return False
    return True
    
