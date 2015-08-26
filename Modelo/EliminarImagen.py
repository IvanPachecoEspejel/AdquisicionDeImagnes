'''
Created on 24/08/2015

@author: ivan
'''
import Accion.Accion as Accion
import Utileria.Util as Util

class EliminarImagen(Accion):
    '''
    Objeto que abstrae las caracteristicas de una accion de elimiar imagenes
    '''
        
    def efectuarAccion(self):
        if not self.accionRealizada:
            for img in self.imgsAfectadas:
                self.__removerImagen(img)
            self.accionRealizada = True
            self.__actualizarHistorial() 
        else:
            raise Exception(Util.getMnsjIdioma("Accion", "Error_Hacer_Accion"))
        
    def deshacerAccion(self):
        
        if self.accionRealizada :
            for img in self.imgsAfectadas:
                self.__agregarImagen(img)
                
            self.accionRealizada = False
        else:
            raise Exception(Util.getMnsjIdioma("Accion", "Error_Deshacer_Accion"))
        
        