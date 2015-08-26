import Utileria.Util as Util

from Utileria.Imagen import Imagen
import Utileria.Valida as Valida

logger = Util.getLogger("Accion")
nomClaseDefault = 'Clase_Default'

class Accion(object):
    
    claseDefault = {}
    clases = {nomClaseDefault:claseDefault}
    
    pilaAcciones = ()
    
    def __init__(self, imgsAfectadas):
        self.imgsAfectadas=imgsAfectadas
        self.accionRealizada = False
        
    def efectuarAccion(self):
        ''' Realiza la accion evitando que se repita '''
        pass
    
    def __deshacerAccion(self):
        ''' 
        Deshace la accion del propio objeto sin eliminarla del historial,
        es por eso que esta accion debe de ser llamada desde la funcion
        deshacerUtilmaAccion(self)
        '''
        pass
        
    def deshacerUltimaAccion(self):
        ''' Deshace la ultima accion realizada eliminandola del historial'''
        if self.accionRealizada:
            self.pilaAcciones.pop().deshacerAccion()
        else:
            raise Exception(Util.getMnsjIdioma("Accion", "Error_Deshacer_Accion"))
        
    def __actualizarHistorial(self):
        ''' Agrega esta accion al historial evitando que se repita '''
        if self.accionRealizada:
            self.pilaAcciones.append(self)
        else:
            logger.info("No se agrego ninguna accion al historial, la accion no se ha efectuado")
        
    def __agregarImagen(self, imagen):
        '''Agrega una imagen al diccionario de la nomClase que trae seteada'''
        
        if imagen.nomClase is None :
            imagen.nomClase = nomClaseDefault     
        try:
            if not Valida.imagenExistenteOnClase(imagen,self.clases[imagen.nomClase]):
                self.clases[imagen.nomClase][imagen.__hash__()] = imagen
                logger.info("Imagen "+imagen.source+" agregada a la clase "+imagen.nomClase)
            else:
                logger.info("Imagen "+imagen.source+"no se puede agregar porque ya existe en esta clase "+imagen.nomClase)
        except Exception as e:
            raise e
        
    def __removerImagen(self, imagen):
        '''Remueve una imagen de la nomClase en la que se encuentra '''
        
        if imagen.nomClase is None:
            raise Exception(Util.getMnsjIdioma("Accion", "Error_Remover_None"))
        
        try:
            if Valida.imagenExistenteOnClase(imagen, self.clases[imagen.nomClase]):
                self.clases[imagen.nomClase][imagen.__hash__()] = []
                logger.info("Imagen "+imagen.source+" removida de la clase "+imagen.nomClase)
            else:
                logger.info("Imagen "+imagen.source+" no se puede remover, porque no esta en la clase "+imagen.nomClase)
        except Exception as e:
            raise e
        
if __name__ == '__main__':
    prueba2 = Imagen("/home/ivan/Imagenes/fondos/02E3A832D.jpg")
    a = Accion(1,prueba2)
    a.efectuarAccion()
    prueba3 = Imagen("/home/ivan/Imagenes/fondos/1_rajathilaknatarajan-redsky.jpg")
    b = Accion(1,prueba2)
    b.efectuarAccion()
    print (Accion.pilaAcciones)