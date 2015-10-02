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
    '''
        Valida que la imagen dada esta contenida en la clase dada
    '''
    
    if(clase.get(imagen.__hash__()) is None):
        return False
    else:
        if imagen.__eq__(clase[imagen.__hash__()]):
            return True
        #Tomo en cuenta un error cuando el diccionario es demaciado grande y se solapan las llaves
        raise Exception(Util.getMnsjIdioma("Accion", "Error_Solapan_Hash"))
    
def imagenesExistenteOnClase(imgs, clase):
    '''
    Funcion que valida que todas las imagenes estan contenidas en la clase dada
    '''
    print type(imgs)
    for img in imgs:
        print img
        if not imagenExistenteOnClase(img, clase):
            return False
    return True

def nomClaseCorrecto(nomClase):
    '''
    Valida que el nombre de la clase sea correcta
    '''
    return nomClase is not None and nomClase is not '' 
    
def exitenciaClase(nomClase, clases):
    '''
    Funcion que valida que la clase nomClase este contenida en la lista clases
    '''
    if clases.get(nomClase) is None:
        return False
    return True
