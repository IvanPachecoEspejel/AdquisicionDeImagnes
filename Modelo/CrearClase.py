'''
Created on 26/08/2015

@author: ivan
'''
from Accion import Accion
import Utileria.Util as Util
import Utileria.Valida as Valida


logger = Util.getLogger("Accion:CrearClase")

class CrearClase(Accion):
    '''
    Clase que abstrae las caracteristicas de la accion crear clase
    '''
    
    def __init__(self, nomClase):
        self.nomClase = nomClase
        self.accionRealizada = False
    
    def efectuarAccion(self, ):
        ''' Crea una clase y la agrega a la lista de dicClases evitando que se repita '''
        logger.info("Creando la lcase: "+self.nomClase+"...")
        if not self.accionRealizada:
            if not Valida.nomClaseCorrecto(self.nomClase):
                logger.error('No se efectuo accion, Nombre de la clase invalido: '+self.nomClase)
                raise Exception(Util.getMnsjIdioma('Accion', 'Error_Crear_Clase_Nom_None'))
            
            if Valida.exitenciaClase(self.nomClase, self.dicClases):
                logger.error('No se efectuo accion, La clase: '+self.nomClase+' ya esta creada')
                raise Exception(Util.getMnsjIdioma('Accion', 'Error_Crear_Clase_Existente'))
            
            nvaClase = {}
            self.dicClases[self.nomClase] = nvaClase
            
            self.accionRealizada = True
            self.actualizarHistorial()
            logger.info("Clase creada :"+self.nomClase+" <ok>")
        else:
            raise Exception(Util.getMnsjIdioma("Accion", "Error_Hacer_Accion"))
        print Accion.dicClases
    
    def deshacerAccion(self):
        ''' 
        Deshace la accion del propio objeto sin eliminarla del historial,
        es por eso que esta accion debe de ser llamada desde la funcion
        deshacerUtilmaAccion(self)
        '''
        logger.info("Deshaciendo accion...")
        if self.accionRealizada:
            del self.dicClases[self.nomClase]
            
            self.accionRealizada = False
            logger.info("Deshaciendo accion <ok> Clase "+self.nomClase+" Eliminada")
        else:
            raise Exception(Util.getMnsjIdioma("Accion", "Error_Deshacer_Accion"))
        
if __name__ == '__main__':
    crearClase = CrearClase("Clase_Preuba")
    crearClase.efectuarAccion()
    print Accion.dicClases
    crearClase.deshacerUltimaAccion()
    print Accion.dicClases
    crearClase.efectuarAccion()
    print Accion.dicClases
    
    crearClase2 = CrearClase("")
    crearClase2.efectuarAccion()
    print Accion.dicClases
    