'''
Created on 26/08/2015

@author: ivan
'''
from Accion import Accion
import Utileria.Util as Util
import Utileria.Valida as Valida


logger = Util.getLogger("Accion:CrearClase")

class EliminarClase(Accion):
    '''
    Clase que abstrae las caracteristicas de la accion eliminar clase
    '''
    
    def __init__(self, nomClase):
        self.nomClase = nomClase
        self.accionRealizada = False
    
    def efectuarAccion(self, ):
        logger.info("Eliminando la lcase: "+self.nomClase)
        ''' Crea una clase y la agrega a la lista de dicClases evitando que se repita '''
        if not self.accionRealizada:            
            if not Valida.exitenciaClase(self.nomClase, self.dicClases):
                logger.error('No se efectuo accion, La clase: '+self.nomClase+' no existe')
                raise Exception(Util.getMnsjIdioma('Accion', 'Error_Eliminar_Clase_Inex'))
            
            del self.dicClases[self.nomClase]
            
            self.accionRealizada = True
            self.actualizarHistorial()
            logger.info("Clase eliminada :"+self.nomClase+" <ok>")
        else:
            raise Exception(Util.getMnsjIdioma("Accion", "Error_Hacer_Accion"))
    
    def deshacerAccion(self):
        ''' 
        Deshace la accion del propio objeto sin eliminarla del historial,
        es por eso que esta accion debe de ser llamada desde la funcion
        deshacerUtilmaAccion(self)
        '''
        logger.info("Deshaciendo Accion ...")
        if self.accionRealizada:
            self.dicClases[self.nomClase] = {}
            
            self.accionRealizada = False
            logger.info("Deshaciendo Accion <ok> Clase "+self.nomClase+" Creada")
        else:
            raise Exception(Util.getMnsjIdioma("Accion", "Error_Deshacer_Accion"))
        
if __name__ == '__main__':
    eliminarClase = EliminarClase(Accion.nomClaseDefault)
    eliminarClase.efectuarAccion()
    print Accion.dicClases
    eliminarClase.deshacerAccion()
    print Accion.dicClases
    
    