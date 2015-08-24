import Utileria.Util as Util
import Utileria.Valida as Valida

logger = Util.getLogger("Accion")

class Accion(object):
    
    claseDefault = {}
    clases = (claseDefault)
    
    pilaAcciones = ()
    
    def __init__(self, tipoAccion, imgsAfectadas):
        self.tipoAccion = tipoAccion
        self.imgsAfectadas=imgsAfectadas
        self.accionRealizada = False
    
    def actualizarHistorial(self):
        ''' Agrega esta accion al historial evitando que se repita '''
        if self.accionRealizada:
            self.pilaAcciones.append(self)
        else:
            raise Exception(Util.getMnsjIdioma("Accion", "Error_Act_Hist"))
        
    def efectuarAccion(self):
        ''' Realiza la accion evitando que se repita '''
        if not self.accionRealizada :
            pass
        else:
            raise Exception(Util.getMnsjIdioma("Accion", "Error_Hacer_Accion"))
        
        self.accionRealizada = True
        
    def deshacerAccion(self):
        ''' Deshace la acción que se realizo'''
        if self.accionRealizada:
            pass
        else:
            raise Exception(Util.getMnsjIdioma("Accion", "Error_DesHacer_Accion"))
        
        
    def __agregarImagen(self, imagen):
        ''' Agrega una imagen al diccionario  '''
        if imagen.clase is None :
            imagen.clase = self.claseDefault
            
        try:
            if not Valida.imagenExistente(imagen, imagen.clase):
                imagen.clase[imagen.__hash__()] = imagen
                logger.info("Imagen "+imagen.source+" agregada")
            else:
                logger.info("Imagen "+imagen.source+" ya existe en esta clase")
        except Exception as e:
            raise e