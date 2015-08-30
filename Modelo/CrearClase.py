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
        ''' Crea una clase y la agrega a la lista de clases evitando que se repita '''
        if not self.accionRealizada:
            if Valida.nomClase(self.nomClase):
                logger.error('No se efectuo accion, Nombre de la clase invalido: '+self.nomClase)
                raise Exception(Util.getMnsjIdioma('Accion', 'Error_Crear_Clase_Nom_None'))
            
            if Valida.exitenciaClase(self.nomClase, self.clases):
                logger.error('No se efectuo accion, La clase: '+self.nomClase+' ya esta creada')
                raise Exception(Util.getMnsjIdioma('Accion', 'Error_Crear_Clase_Existente'))
            
            self.nomClase = self.nomClase
            nvaClase = {}
            self.clases[self.nomClase] = nvaClase
            
            self.accionRealizada = True
            self.actualizarHistorial()
        else:
            raise Exception(Util.getMnsjIdioma("Accion", "Error_Hacer_Accion"))
    
    def deshacerAccion(self):
        ''' 
        Deshace la accion del propio objeto sin eliminarla del historial,
        es por eso que esta accion debe de ser llamada desde la funcion
        deshacerUtilmaAccion(self)
        '''
        if self.accionRealizada:
            del self.clases[self.nomClase]
            
            self.accionRealizada = False
        else:
            raise Exception(Util.getMnsjIdioma("Accion", "Error_Deshacer_Accion"))
        
if __name__ == '__main__':
    crearClase = CrearClase("Clase_Preuba")
    crearClase.efectuarAccion()
    print Accion.clases
    crearClase.deshacerUltimaAccion()
    print Accion.clases
    crearClase.efectuarAccion()
    print Accion.clases