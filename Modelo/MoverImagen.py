'''
Created on 25/08/2015

@author: ivan
'''
import Accion.Accion as Accion
import Utileria.Util as Util
import EliminarImagen.EliminarImagen as EliminarImagen
import AgregarImagen.AgregarImagen as AgregarIagen

class MoverImagen(Accion):
    '''
    Objeto que abstrae los atributos y funcionalidades de la accion mover
    '''
    
    def __init__(self, imgsAfectadas, claseOrigen, claseDestino):
        self.imgsAfectadas = imgsAfectadas
        self.claseOrigen = claseOrigen
        self.claseDestino = claseDestino
        self.removerImgs = EliminarImagen(imgsAfectadas)
        self.agregarImgs = AgregarIagen(imgsAfectadas)
        
    def efectuarAccion(self):
        if not self.accionRealizada :
            
            self.removerImgs.efectuarAccion()
            for img in self.imgsAfectadas:
                self.__moverImagen(img, self.claseDestino)
            self.agregarImgs.efectuarAccion()
            
            self.accionRealizada = True
            self.__actualizarHistorial()
        else:
            raise Exception(Util.getMnsjIdioma("Accion", "Error_Hacer_Accion"))
        
    def __deshacerAccion(self):
        if self.accionRealizada:
            
            self.removerImgs.efectuarAccion()
            for img in self.imgsAfectadas:
                self.__moverImagen(img, self.claseOrigen)
            self.agregarImgs.efectuarAccion()
            
            self.accionRealizada = False
        else:
            raise Exception(Util.getMnsjIdioma("Accion", "Error_Deshacer_Accion"))
        