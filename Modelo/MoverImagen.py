'''
Created on 25/08/2015

@author: ivan
'''
from Accion import Accion
import Utileria.Util as Util
import Utileria.Valida as Valida
from EliminarImagen import  EliminarImagen
from AgregarImagen import AgregarImagen
from CrearClase import CrearClase
from Utileria.Imagen import Imagen

class MoverImagen(Accion):
    '''
    Objeto que abstrae los atributos y funcionalidades de la accion mover
    '''
    
    logger = Util.getLogger("MoverImagen")
    
    def __init__(self, imgsAfectadas, claseOrigen, claseDestino):
        self.imgsAfectadas = imgsAfectadas
        self.claseOrigen = claseOrigen
        self.claseDestino = claseDestino
        self.removerImgs = EliminarImagen(imgsAfectadas)
        self.agregarImgs = AgregarImagen(imgsAfectadas)
        self.accionRealizada = False
        
        if not Valida.exitenciaClase(self.claseOrigen, Accion.clases):
            self.logger.error("Clase "+claseOrigen+" inexistente")
            raise Exception(Util.getMnsjIdioma('Accion', 'Error_Crear_Clase_Existente'))
        if not Valida.exitenciaClase(self.claseDestino, Accion.clases):
            self.logger.error("Clase "+claseDestino+" inexistente")
            raise Exception(Util.getMnsjIdioma('Accion', 'Error_Crear_Clase_Existente'))
        if not Valida.imagenesExistenteOnClase(self.imgsAfectadas, Accion.clases[claseOrigen]):
            self.logger.error("Error imagenes incosistentes, no todas se encuentran en la clase origen: "+claseOrigen)
            raise Exception(Util.getMnsjIdioma('Accion', 'Error_Imagenes_Inconsistentes'))
        
        for img in imgsAfectadas:
            img.nomClaseCorrecto = claseOrigen
        
    def efectuarAccion(self):
        if not self.accionRealizada :
            
            self.removerImgs.efectuarAccion()
            for img in self.imgsAfectadas:
                self.moverImagen(img, self.claseDestino)
            self.agregarImgs.efectuarAccion()
            
            self.accionRealizada = True
            self.actualizarHistorial()
        else:
            raise Exception(Util.getMnsjIdioma("Accion", "Error_Hacer_Accion"))
        
    def deshacerAccion(self):
        if self.accionRealizada:
            # Se deshace la accion de agregar imagenes de la clase Destino
            self.deshacerUltimaAccion()
            # Se vuelven a mover las imagenes
            for img in self.imgsAfectadas:
                self.moverImagen(img, self.claseOrigen)
            # Se deshace la accion de eliminar imagenes de la clase Origen
            self.deshacerUltimaAccion()
        else:
            raise Exception(Util.getMnsjIdioma("Accion", "Error_Deshacer_Accion"))

if __name__ == '__main__':
    img1 = Imagen("/home/ivan/Imagenes/fondos/02E3A832D.jpg")
    img2 = Imagen("/home/ivan/Imagenes/fondos/1_rajathilaknatarajan-redsky.jpg")
    a = (img1, img2)
    agregarImgs = AgregarImagen(a)
    agregarImgs.efectuarAccion()
    
    nvaClase = CrearClase('Clase2')
    nvaClase.efectuarAccion()
    print 'Clases: '
    print Accion.clases
    print 'Pila de Acciones'
    print Accion.pilaAcciones
    print 'Clases Registrada'
    for clase in Accion.clases:
        print clase
    print " "
    
    moverImagenes = MoverImagen(a, Accion.nomClaseDefault, 'Clase2')
    moverImagenes.efectuarAccion()
    
    print 'Clases: '
    print Accion.clases
    print 'Pila de Acciones'
    print Accion.pilaAcciones
    print 'Clases Registrada'
    for clase in Accion.clases:
        print clase
    print " "
        
    moverImagenes.deshacerUltimaAccion()
    
    print 'Clases: '
    print Accion.clases
    print 'Pila de Acciones'
    print Accion.pilaAcciones
    print 'Clases Registrada'
    for clase in Accion.clases:
        print clase
    print " "