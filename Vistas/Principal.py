from Tkinter import StringVar
import tkFileDialog
import ttk

from Modelo.Accion import Accion
from Modelo.AgregarImagen import AgregarImagen
from Modelo.CrearClase import CrearClase
from Modelo.EliminarClase import EliminarClase
from Modelo.EliminarImagen import EliminarImagen
from Modelo.MoverImagen import MoverImagen
import Tkinter as tk
from Utileria import Util
from Utileria.TablaRutas import TablaRutas
from Vistas.VistaCrearClase import VistaCrearClase
from Vistas.VistaGuardarDirectorioImgs import VistaGuardarDirectorioImgs
from Vistas.VistaMenuAgregarImagenes import VistaMenuAgregarImagenes
from Vistas.VistaMoverSeleccionados import VistaMoverSeleccionados


# from PIL import Image
# import ImageTk
########################################################################
logger = Util.getLogger("Principal")

########################################################################
class Principal(tk.Frame):
    '''
    Frame que muestra la ventana principal de la aplicacion
    '''
    #-------------------------------------------------------------------------------
    def __init__(self, master=None,  *args, **kw):
        '''
        Constructor de la vista e inicializacion de las propiedades de la ventana
        '''
        tk.Frame.__init__(self, master, *args, **kw)
        self.padre = master
        self.padre.geometry('1000x500+10+10')
        
        self.initUI()

    #-------------------------------------------------------------------------------
    def initUI(self):
        '''
        Crea y empaqueta todos low widgets de la ventana
        '''
        self.padre.title("Adquicicion de imagenes")
        
        frmHeader = ttk.Frame(self.padre, relief = tk.RAISED)
        mbMenu=  ttk.Menubutton(frmHeader, text="Archivo")
        mbMenu.menu = tk.Menu(mbMenu)
        mbMenu["menu"] = mbMenu.menu
        mbMenu.menu.add_command(label = "Generar Archivo De Direcciones", command = self.abrirGenerarArchivoDeDirecciones)
        mbMenu.menu.add_command(label = "Generar Directorio de Imagenes", command = self.abrirVistaGuardarDirectorioImgs)
        mbMenu.pack(side = tk.LEFT)
        frmHeader.pack(side = tk.TOP, fill = tk.X, expand = tk.TRUE)
        
        frmNorte = ttk.Frame(self.padre)
        
        frmNorteOeste  = ttk.Frame(frmNorte)        
        
        lblLogo = ttk.Label(frmNorteOeste, background = "green", text="Logo")
        lblLogo.pack(fill = tk.BOTH)
        
        frmNorteOeste.grid(column = 0, row = 0)
        
        frmNorteEste = ttk.Frame(frmNorte)
         
        btnAgregarImg = ttk.Button(frmNorteEste, 
                                   text="Agregar Imagen", 
                                   width = Util.getMnsjConf("VistaPrincipal", "tamBotones"),
                                   command = self.abrirVistaMenuAgrImgs)
        btnAgregarImg.grid(column = 1, row = 0, pady = 5)
        btnCrearClase = ttk.Button(frmNorteEste, 
                                   text="Nueva Clase", 
                                   width = Util.getMnsjConf("VistaPrincipal", "tamBotones"),
                                   command = self.abrirVistaCrearClase)
        btnCrearClase.grid(column = 1, row = 1, pady = 5)
        
        frmNorteEste.grid(column = 1, row = 0)
        
        frmNorte.grid_columnconfigure(0,weight = 1)
        frmNorte.grid_columnconfigure(1,weight = 1)
        
        frmNorte.pack(fill = tk.X, side=tk.TOP)
        
        ttk.Separator(self.padre, orient = tk.HORIZONTAL).pack()
        
        frmCenter = ttk.Frame(self.padre)
        
        frmCenterOeste = ttk.Labelframe(frmCenter, text = "Acciones sobre la tabla")
        
        ttk.Label(frmCenterOeste, text = "Cambia de clase: ").pack(fill = tk.Y, anchor = tk.NW)         
        self.selectedClase = StringVar()
        self.selectedClase.set(Accion.nomClaseDefault)
        self.cmbClases = ttk.Combobox(frmCenterOeste, 
                                      textvariable=self.selectedClase, 
                                      state = 'readonly')
        self.cmbClases['values'] = Accion.dicClases.keys()
         
        self.cmbClases.pack(fill = tk.Y, pady = 5)
        self.cmbClases.bind("<<ComboboxSelected>>", self.cambiarClase)
         
        ttk.Button(frmCenterOeste, 
                   text = "Mover Todo", 
                   width = Util.getMnsjConf("VistaPrincipal", "tamBotones"),
                   command = self.abrirVistaMoverImgs).pack(fill = tk.Y, pady = 5)
        
        ttk.Button(frmCenterOeste, 
                   text = "Eliminar Todo", 
                   width = Util.getMnsjConf("VistaPrincipal", "tamBotones"),
                   command = self.eliminarImagenes).pack(fill = tk.Y, pady = 5)
        
        ttk.Separator(frmCenterOeste, orient = tk.HORIZONTAL).pack(fill = tk.Y, expand = tk.TRUE)
        
        ttk.Button(frmCenterOeste, 
                   text = "Deshacer ultima Accion", 
                   width = Util.getMnsjConf("VistaPrincipal", "tamBotones"),
                   command = self.deshacerAccion).pack(fill = tk.Y, pady = 5)
        
        frmCenterOeste.pack(fill = tk.BOTH, side = tk.LEFT, expand = tk.TRUE, padx = 5)
        
        frmCenterEste = ttk.Labelframe(frmCenter, text = "Imagenes de la clase")
        
        self.frmTabla = TablaRutas(frmCenterEste)
        self.frmTabla.pack(fill = tk.BOTH, expand = tk.TRUE)
        
        frmCenterEste.pack(fill = tk.BOTH, side = tk.LEFT, expand = tk.TRUE, padx = 5)
        
        frmCenter.pack(fill = tk.BOTH, side = tk.TOP, expand= tk.TRUE)
        
        #++++++++++++++++++++++++ Ventanas Emergentes ++++++++++++++++++++++++#
        self.frmVentanaCrearClase = VistaCrearClase(self, self.crearClase)
        self.frmVentanaMenuAgrImgs = VistaMenuAgregarImagenes(self, self.frmTabla)
        self.frmVentanaMoverImgs = VistaMoverSeleccionados(self, self.selectedClase, self.frmTabla.lstImgsSeleccionadas)
        self.frmVentanaGuaDirImgs  = VistaGuardarDirectorioImgs(self)
        
    #-------------------------------------------------------------------------------        
    def crearClase(self):
        '''
        Metodo que crea una clase y refresca el combobox que contiene las clases de la vista
        '''
        try:
            CrearClase(self.frmVentanaCrearClase.strVarNomNvaClase.get()).efectuarAccion()
            self.frmVentanaCrearClase.strVarNomNvaClase.set("")
            self.frmVentanaCrearClase.hide()
            self.actualizarCmbClases()
        except Exception as ex:
            logger.error(ex)
        
    #-------------------------------------------------------------------------------
    def abrirVistaCrearClase(self):
        self.frmVentanaCrearClase.show()
    
    #-------------------------------------------------------------------------------
    def abrirVistaMenuAgrImgs(self):
        self.frmVentanaMenuAgrImgs.show()
    
    #-------------------------------------------------------------------------------
    def abrirVistaMoverImgs(self):
        self.frmVentanaMoverImgs.show()
        
    #-------------------------------------------------------------------------------
    def abrirVistaGuardarDirectorioImgs(self):
        self.frmVentanaGuaDirImgs.show()
    
    #-------------------------------------------------------------------------------
    def abrirGenerarArchivoDeDirecciones(self):
        f = tkFileDialog.asksaveasfilename(defaultextension=".txt")
        Accion().generarArchivoDeDirecciones(f)
        
    #-------------------------------------------------------------------------------
    def cambiarClase(self, event):
        logger.info("Cambiando de clase a : "+self.selectedClase.get())
        if self.selectedClase.get() is not None and self.selectedClase.get() != "":
            self.actualizarClase(self.selectedClase.get())
    
    #-------------------------------------------------------------------------------
    def actualizarCmbClases(self):
        self.cmbClases['values'] = Accion.dicClases.keys()
    
    #-------------------------------------------------------------------------------
    def actualizarClase(self, nomClase):
        self.frmTabla.cambiarDeClase(nomClase)
        self.frmTabla.actualizarTabla()
        self.selectedClase.set(nomClase)
        
    #-------------------------------------------------------------------------------
    def eliminarImagenes(self):
        lstAuxImgs = []
        lstAuxImgs.extend(self.frmTabla.lstImgsSeleccionadas)
        accion = EliminarImagen(lstAuxImgs)
        accion.efectuarAccion()
        self.actualizarClase(self.selectedClase.get())
        
    #-------------------------------------------------------------------------------
    def deshacerAccion(self):
        accionDeshecha = Accion().deshacerUltimaAccion()
        
        if accionDeshecha is None:
            logger.info("No hay mas acciones por deshacer")
        elif accionDeshecha.__class__ == AgregarImagen:
            self.actualizarClase(Accion.nomClaseDefault)
        elif accionDeshecha.__class__ == EliminarImagen:
            self.actualizarClase(accionDeshecha.imgsAfectadas[0].nomClaseCorrecto)
        elif accionDeshecha.__class__ == CrearClase or accionDeshecha.__class__ == EliminarClase:
            self.actualizarCmbClases()
        elif accionDeshecha.__class__ == MoverImagen:
            self.actualizarClase(accionDeshecha.claseOrigen)
        else:
            logger.error("Error no se encontro el tipo de accion que se desizo")
        
    

########################################################################        
if __name__ == '__main__':
    root = tk.Tk()
    app = Principal(master=root)
    app.mainloop()
