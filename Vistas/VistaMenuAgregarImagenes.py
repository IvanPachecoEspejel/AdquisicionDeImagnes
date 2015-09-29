'''
Created on 18/09/2015

@author: ivan
'''

import ttk
import Tkinter as tk
import tkFileDialog 
from Utileria import Util
from Utileria.Imagen import Imagen
from Modelo.AgregarImagen import AgregarImagen
from Vistas.VistaAgregarImgURLWeb import VistaAgregarImgURLWeb
from Modelo.Accion import Accion
import os

logger = Util.getLogger("VistaMenuAgregarImagenes")

#########################################################################################

class VistaMenuAgregarImagenes(tk.Toplevel):
    '''
    Ventana en la que se ofrece la posibilidad de crear una clase
    '''
    
    #----------------------------------------------------------------------
    def __init__(self, master, frmTabla):
        '''
        Constructor
        '''
        tk.Toplevel.__init__(self, master)
        self.padre = master
        self.attributes('-topmost', tk.TRUE)
        self.frmTabla = frmTabla
        self.title("Agregar Imagenes")
        
        #Opciones para el dialogo de imagenes para abrir una sola imagen de tkinter
        self.optDialogoImg = opciones = {}
        opciones['defaultextension'] = '.jpg'
        opciones['filetypes'] = [('Imagenes', Util.getMnsjConf("Validacion", "Extenciones"))]
        opciones['initialdir'] = '/home/ivan/'
        opciones['parent'] = self
        opciones['title'] = 'Escoge imagenes'
        
        #Opciones para el dialogo de imagenes para abrir un archivo con url's de imagenes de tkinter
        self.optDialogoArchivo = opciones = {}
        opciones['defaultextension'] = '.jpg'
        opciones['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
        opciones['initialdir'] = '/home/ivan/Escritorio/'
        opciones['parent'] = self
        opciones['title'] = 'Escoge un imagen archivo de texto que contenga url\'s de imagenes'
        
        #Opciones para el dialogo de imagenes para abrir un directorio con imagenes de tkinter
        self.optDialogoDir = opciones = {}
        opciones['initialdir'] = '/home/ivan/Escritorio/'
        opciones['parent'] = self
        opciones['title'] = 'Escoge un directorio con imagenes'
        
        self.initUI()
        self.hide()
        
    #----------------------------------------------------------------------
    def initUI(self):
        '''
        Crea y empaqueta los windgets de la ventana, tambien se establecen las propiedades
        de la ventana 
        '''
        self.geometry('300x210+300+100')
        self.protocol("WM_DELETE_WINDOW", "onexit")
        self.resizable(0,0)
        
        frmClases = ttk.Labelframe(self,text = "Escoge una opcion")
        
        ttk.Button(frmClases,
                   text = 'Una sola imagen de la PC.', 
                   width = 30,
                   command = self.agregarImagenPC).pack(pady = 5)
                   
        ttk.Button(frmClases,
                   text = 'Una sola imagen de la WEB.', 
                   width = 30,
                   command = self.mostrarVistaAgrImgURLWeb).pack(pady = 5)
        
        ttk.Button(frmClases,
                   text = 'Un Archivo de Direcciones WEB o PC', 
                   width = 30,
                   command = self.agregarImagenesArchivo).pack(pady = 5)
        
        ttk.Button(frmClases,
                   text = 'Una carpeta con Imagenes', 
                   width = 30,
                   command = self.agregarImagenesDeDirectorio).pack(pady = 5)
                   
        ttk.Button(frmClases, 
                   text = 'Cancelar', 
                   command = self.hide).pack(pady = 15)
                   
        
        frmClases.pack(fill = tk.BOTH)
        
        #++++++++++++++++++++++++ Ventanas Emergentes ++++++++++++++++++++++++#
        self.frmVistaAgrImgURLWeb = VistaAgregarImgURLWeb(self, self.agregarImagenWEB)
        
    #----------------------------------------------------------------------
    def hide(self):
        """
        Oculta la ventana 
        """
        self.withdraw()
        
    #----------------------------------------------------------------------
    def show(self):
        """
        Mustra la ventana
        """
        self.update()
        self.deiconify()
        
    #----------------------------------------------------------------------
    def mostrarVistaAgrImgURLWeb(self):
        self.frmVistaAgrImgURLWeb.show()
    
    #----------------------------------------------------------------------    
    def agregarImagenPC(self):
        dirImg = tkFileDialog.askopenfilename(**self.optDialogoImg)
        
        if dirImg is None or dirImg == "":
            return
        
        nvaImg = Imagen(dirImg, self.frmTabla)
        a = []
        a.append(nvaImg)
        AgregarImagen(a).efectuarAccion()
        self.padre.actualizarClase(Accion.nomClaseDefault)
    
    #----------------------------------------------------------------------
    def agregarImagenWEB(self):
        try:
            dirImg = self.frmVistaAgrImgURLWeb.nomNvaImg.get()
            nvaImg = Imagen(dirImg, self.frmTabla)
            a = []
            a.append(nvaImg)
            AgregarImagen(a).efectuarAccion()
            
            self.frmVistaAgrImgURLWeb.hide()
        except Exception as ex:
            logger.error(ex)
        self.padre.actualizarClase(Accion.nomClaseDefault)
            
    #----------------------------------------------------------------------    
    def agregarImagenesArchivo(self):
        archivo = tkFileDialog.askopenfile(**self.optDialogoArchivo)
        
        if archivo is None:
            return
        
        linea = archivo.readline()
        a = []
        while linea != "":
            try:
                nvaImg = Imagen(linea.strip(), self.frmTabla)
                a.append(nvaImg)
            except Exception as ex:
                logger.error(ex)
            linea = archivo.readline()
        AgregarImagen(a).efectuarAccion()
        self.padre.actualizarClase(Accion.nomClaseDefault)
        
    #----------------------------------------------------------------------    
    def agregarImagenesDeDirectorio(self):
        directorio = tkFileDialog.askdirectory(**self.optDialogoDir)
        if directorio is None or directorio == "":
            return
        ficheros = os.listdir(directorio)
        a = []
        for fichero in ficheros:
            try:
                nvaImg = Imagen(directorio+os.path.sep+fichero, self.frmTabla)
                a.append(nvaImg)
            except Exception as ex:
                logger.error(ex)
        AgregarImagen(a).efectuarAccion()
        self.padre.actualizarClase(Accion.nomClaseDefault)
    
    #----------------------------------------------------------------------    
    def actualizar(self):
        self.frmTabla.actualizar()
#########################################################################################
        
if __name__ == "__main__":
    
    class SampleApp(tk.Tk):
        
        def __init__(self,*args, **kwargs):
            root = tk.Tk.__init__(self, *args, **kwargs)

            self.frmTabla = VistaMenuAgregarImagenes(root)
            
        
    app = SampleApp()
    app.geometry('350x100+200+200')
    app.mainloop()
        
        
    
        
