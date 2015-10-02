'''
Created on 24/08/2015

@author: ivan
'''
from Accion import Accion
from AgregarImagen import AgregarImagen
from Utileria.Imagen import Imagen
import Utileria.Util as Util


class EliminarImagen(Accion):
    '''
    Objeto que abstrae las caracteristicas de una accion de elimiar imagenes
    '''
    
    def __init__(self, imgsAfectadas):
        self.imgsAfectadas=imgsAfectadas
        self.accionRealizada = False
        
    def efectuarAccion(self):
        if not self.accionRealizada:
            for img in self.imgsAfectadas:
                self.removerImagen(img)
            self.accionRealizada = True
            self.actualizarHistorial() 
        else:
            raise Exception(Util.getMnsjIdioma("Accion", "Error_Hacer_Accion"))
        
    def deshacerAccion(self):
        
        if self.accionRealizada :
            for img in self.imgsAfectadas:
                self.agregarImagen(img)
                
            self.accionRealizada = False
        else:
            raise Exception(Util.getMnsjIdioma("Accion", "Error_Deshacer_Accion"))
        
if __name__ == '__main__':
    img1 = Imagen("/home/ivan/Imagenes/fondos/02E3A832D.jpg")
    img2 = Imagen("/home/ivan/Imagenes/fondos/1_rajathilaknatarajan-redsky.jpg")
    a = (img1, img2)
    agregarImgs = AgregarImagen(a)
    agregarImgs.efectuarAccion()
    print 'Clases: '
    print Accion.dicClases
    print 'Pila de Acciones'
    print Accion.pilaAcciones
    print 'Clases Registrada'
    for clase in Accion.dicClases:
        print clase
    
    removerImgs = EliminarImagen(a)
    removerImgs.efectuarAccion()
    
    print 'Clases: '
    print Accion.dicClases
    print 'Pila de Acciones'
    print Accion.pilaAcciones
    print 'Clases Registrada'
    for clase in Accion.dicClases:
        print clase
        
    removerImgs.deshacerUltimaAccion()
    print 'Clases: '
    print Accion.dicClases
    print 'Pila de Acciones'
    print Accion.pilaAcciones
    print 'Clases Registrada'
    for clase in Accion.dicClases:
        print clase