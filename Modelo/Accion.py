import Utileria.Util as Util
import tkFileDialog
import Utileria.Valida as Valida
import os

######################################################################################
logger = Util.getLogger("Accion")
######################################################################################
class Accion(object):
    
    nomClaseDefault = 'Clase_Default'
    claseDefault = {}
    
    dicClases = {nomClaseDefault:claseDefault}
    pilaAcciones = []
    
    #-----------------------------------------------------------------------------------------------
    def __init__(self, direccionProyecto = None):
        self.imgsAfectadas=[]
        self.accionRealizada = True
        self.dirProyecto = direccionProyecto
    
    #-----------------------------------------------------------------------------------------------
    def efectuarAccion(self):
        ''' Realiza la accion evitando que se repita '''
        return
    
    #-----------------------------------------------------------------------------------------------
    def deshacerAccion(self):
        ''' 
        Deshace la accion del propio objeto sin eliminarla del historial,
        es por eso que esta accion debe de ser llamada desde la funcion
        deshacerUtilmaAccion(self)
        '''
        return

    #-----------------------------------------------------------------------------------------------    
    def deshacerUltimaAccion(self):
        ''' Deshace la ultima accion realizada eliminandola del historial'''
        if self.accionRealizada:
            accion = None
            if len(self.pilaAcciones)>0 :
                accion = self.pilaAcciones.pop()
                accion.deshacerAccion()
            return accion
        else:
            raise Exception(Util.getMnsjIdioma("Accion", "Error_Deshacer_Accion"))
        
    #-----------------------------------------------------------------------------------------------    
    def actualizarHistorial(self):
        ''' Agrega esta accion al historial evitando que se repita '''
        if self.accionRealizada:
            self.pilaAcciones.append(self)
        else:
            logger.info("No se agrego ninguna accion al historial, la accion no se ha efectuado")
            
    #-----------------------------------------------------------------------------------------------    
    def agregarImagen(self, imagen):
        '''Agrega una imagen al diccionario de la nomClaseCorrecto que trae seteada'''
        
        if imagen.nomClaseCorrecto is None :
            imagen.nomClaseCorrecto = self.nomClaseDefault     
        try:
            if not Valida.imagenExistenteOnClase(imagen,self.dicClases[imagen.nomClaseCorrecto]):
                self.dicClases[imagen.nomClaseCorrecto][imagen.__hash__()] = imagen
                logger.info("Imagen "+imagen.source+" agregada a la clase "+imagen.nomClaseCorrecto)
            else:
                logger.info("Imagen "+imagen.source+"no se puede agregar porque ya existe en esta clase "+imagen.nomClaseCorrecto)
        except KeyError:
            logger.error("Clase "+imagen.nomClaseCorrecto+" inexistente")
            raise Exception(Util.getMnsjConf('Accion', 'Error_Clase_Inexistente'))
        except Exception as e:
            raise e
        
    #-----------------------------------------------------------------------------------------------    
    def removerImagen(self, imagen):
        '''Remueve una imagen de la nomClaseCorrecto en la que se encuentra '''
        
        if imagen.nomClaseCorrecto is None:
            raise Exception(Util.getMnsjIdioma("Accion", "Error_Remover_None"))
        
        try:
            del self.dicClases[imagen.nomClaseCorrecto][imagen.__hash__()]
            logger.info("Imagen "+imagen.source+" removida de la clase "+imagen.nomClaseCorrecto)
        except KeyError:
            logger.error("Clase "+imagen.nomClaseCorrecto+" inexistente")
            raise Exception(Util.getMnsjConf('Accion', 'Error_Clase_Inexistente'))
        except Exception as e:
            raise e
    
    #-----------------------------------------------------------------------------------------------    
    def moverImagen(self, imagen, claseDestino):
        if imagen is not None:
            imagen.nomClaseCorrecto = claseDestino
        else:
            logger.error("Error la imagen es None no se puede mover")
            raise Exception(Util.getMnsjIdioma('Accion', 'Error_Imagen_None'))
        
    #-----------------------------------------------------------------------------------------------
    def generarArchivoDeDirecciones(self):
        f = tkFileDialog.asksaveasfile(mode = "w", defaultextension=".txt")
        if f is None:
            return
        for clase in self.dicClases:
            f.write("["+clase+"]\n")
            for img in self.dicClases[clase].values():
                f.write(img.source+"\n")
        
        f.flush()
        f.close()
    
    #-----------------------------------------------------------------------------------------------
    def generarFolderDeImagenes(self, dirProyecto):
        diag = os.path.sep                          #Separador de archivos
        
        if os.path.exists(dirProyecto):
            try:
                self.eliminarDirectorio(dirProyecto)
            except Exception as ex:
                logger.error("Error al generar Folder de imagenes no se puede eliminar: "+dirProyecto)
                raise ex
            
        os.mkdir(dirProyecto)
            
        for clase in self.dicClases:
            directorioClase = dirProyecto+diag+clase
            os.mkdir(directorioClase)
            i = 0
            for img in self.dicClases[clase].values():
                img.guardarImagen(directorioClase+diag+"img"+str(i)+".jpg")
                i = i+1
        
    #-----------------------------------------------------------------------------------------------
    def eliminarDirectorio(self, direccionDirectorio):
        if not os.path.exists(direccionDirectorio):
            return
        try:
            for root, dirs, files in os.walk(direccionDirectorio, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
                    
            os.rmdir(direccionDirectorio)
        except Exception as ex:
            logger.error("Error al eliminar el directorio: "+direccionDirectorio)
            raise ex 
######################################################################################