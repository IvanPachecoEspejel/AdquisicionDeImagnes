'''
Created on 26/08/2015

@author: ivan
'''
import Accion.Accion as Accion

import Utileria.Util as Util
import Utileria.Valida as Valida

logger = Util.getLogger("Accion:CrearClase")

class CrearClase(Accion):
    '''
    Clase que abstrae las caracteristicas de la accion crear clase
    '''
    
    def efectuarAccion(self, nomClase = None):
        ''' Crea una clase y la agrega a la lista de clases evitando que se repita '''
        if not self.accionRealizada:
            if Valida.nomClase(nomClase):
                logger.error('No se efectuo accion, Nombre de la clase invalido: '+nomClase)
                raise Exception(Util.getMnsjIdioma('Accion', 'Error_Crear_Clase_Nom_None'))
            
            if Valida.exitenciaClase(nomClase, self.clases):
                logger.error('No se efectuo accion, La clase: '+nomClase+' ya esta creada')
                raise Exception(Util.getMnsjIdioma('Accion', 'Error_Crear_Clase_Existente'))
            
            self.nomClase = nomClase
            nvaClase = {}
            self.clases[nomClase] = nvaClase
            
            self.accionRealizada = True
            self.__actualizarHistorial()
        else:
            raise Exception(Util.getMnsjIdioma("Accion", "Error_Hacer_Accion"))
    
    def __deshacerAccion(self):
        ''' 
        Deshace la accion del propio objeto sin eliminarla del historial,
        es por eso que esta accion debe de ser llamada desde la funcion
        deshacerUtilmaAccion(self)
        '''
        if self.accionRealizada:
            self.clases[self.nomClase] = []
            
            self.accionRealizada = False
        else:
            raise Exception(Util.getMnsjIdioma("Accion", "Error_Deshacer_Accion"))