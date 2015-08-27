'''
Created on 24/08/2015

@author: ivan
'''

import Accion.Accion as Accion
import Utileria.Util as Util

logger = Util.getLogger("Agrega")

class AgregarImagen(Accion):
    '''
    Objeto que abstrae las caracteristicas de una accion de agregar imagenes
    '''
    
    def efectuarAccion(self):
        if not self.accionRealizada :
            for img in self.imgsAfectadas:
                self.__agregarImagen(img)
                
            self.accionRealizada = True
            self.__actualizarHistorial()
        else:
            raise Exception(Util.getMnsjIdioma("Accion", "Error_Hacer_Accion"))
        
    def __deshacerAccion(self):
        if self.accionRealizada:
            for img in self.imgsAfectadas:
                self.__removerImagen(img)
            self.accionRealizada = False
        else:
            raise Exception(Util.getMnsjIdioma("Accion", "Error_Deshacer_Accion"))
        
        
        
        
        
        
         