import Utileria.Util as Util

from Utileria.Imagen import Imagen
import Utileria.Valida as Valida

logger = Util.getLogger("Accion")

class Accion(object):
    
    nomClaseDefault = 'Clase_Default'
    claseDefault = {}
    
    clases = {nomClaseDefault:claseDefault}
    pilaAcciones = []
    
    def __init__(self, imgsAfectadas):
        self.imgsAfectadas=imgsAfectadas
        self.accionRealizada = False
    
    def efectuarAccion(self):
        ''' Realiza la accion evitando que se repita '''
        return
    
    def deshacerAccion(self):
        ''' 
        Deshace la accion del propio objeto sin eliminarla del historial,
        es por eso que esta accion debe de ser llamada desde la funcion
        deshacerUtilmaAccion(self)
        '''
        return
    
    def deshacerUltimaAccion(self):
        ''' Deshace la ultima accion realizada eliminandola del historial'''
        if self.accionRealizada:
            self.pilaAcciones.pop().deshacerAccion()
        else:
            raise Exception(Util.getMnsjIdioma("Accion", "Error_Deshacer_Accion"))
        
    def actualizarHistorial(self):
        ''' Agrega esta accion al historial evitando que se repita '''
        if self.accionRealizada:
            self.pilaAcciones.append(self)
        else:
            logger.info("No se agrego ninguna accion al historial, la accion no se ha efectuado")
        
    def agregarImagen(self, imagen):
        '''Agrega una imagen al diccionario de la nomClaseCorrecto que trae seteada'''
        
        if imagen.nomClaseCorrecto is None :
            imagen.nomClaseCorrecto = self.nomClaseDefault     
        try:
            if not Valida.imagenExistenteOnClase(imagen,self.clases[imagen.nomClaseCorrecto]):
                self.clases[imagen.nomClaseCorrecto][imagen.__hash__()] = imagen
                logger.info("Imagen "+imagen.source+" agregada a la clase "+imagen.nomClaseCorrecto)
            else:
                logger.info("Imagen "+imagen.source+"no se puede agregar porque ya existe en esta clase "+imagen.nomClaseCorrecto)
        except KeyError:
            logger.error("Clase "+imagen.nomClaseCorrecto+" inexistente")
            raise Exception(Util.getMnsjConf('Accion', 'Error_Clase_Inexistente'))
        except Exception as e:
            raise e
        
    def removerImagen(self, imagen):
        '''Remueve una imagen de la nomClaseCorrecto en la que se encuentra '''
        
        if imagen.nomClaseCorrecto is None:
            raise Exception(Util.getMnsjIdioma("Accion", "Error_Remover_None"))
        
        try:
            del self.clases[imagen.nomClaseCorrecto][imagen.__hash__()]
            logger.info("Imagen "+imagen.source+" removida de la clase "+imagen.nomClaseCorrecto)
        except KeyError:
            logger.error("Clase "+imagen.nomClaseCorrecto+" inexistente")
            raise Exception(Util.getMnsjConf('Accion', 'Error_Clase_Inexistente'))
        except Exception as e:
            raise e
        
    def moverImagen(self, imagen, claseDestino):
        if imagen is not None:
            imagen.nomClaseCorrecto = claseDestino
        else:
            logger.error("Error la imagen es None no se puede mover")
            raise Exception(Util.getMnsjIdioma('Accion', 'Error_Imagen_None'))

if __name__ == '__main__':
    prueba2 = Imagen("/home/ivan/Imagenes/fondos/02E3A832D.jpg")
    a = Accion(1,prueba2)
    a.efectuarAccion()
    prueba3 = Imagen("/home/ivan/Imagenes/fondos/1_rajathilaknatarajan-redsky.jpg")
    b = Accion(1,prueba2)
    b.efectuarAccion()
    print (Accion.pilaAcciones)