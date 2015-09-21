import Tkinter as tk
from Tkinter import StringVar
import ttk
from Utileria import Util
from Modelo.Accion import Accion
from Modelo.CrearClase import CrearClase
from Utileria.TablaRutas import TablaRutas
from Vistas.VistaCrearClase import VistaAgregarImgURLWeb
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
        self.padre.geometry('800x500+10+10')
        
        self.initUI()

    #-------------------------------------------------------------------------------
    def initUI(self):
        '''
        Crea y empaqueta todos low widgets de la ventana
        '''
        self.padre.title("Adquicicion de imagenes")
        
        frmNorte = ttk.Frame(self.padre)
        
        frmNorteOeste  = ttk.Frame(frmNorte)        
        
        lblLogo = ttk.Label(frmNorteOeste, background = "green", text="Logo")
        lblLogo.pack(fill = tk.BOTH)
        
        frmNorteOeste.grid(column = 0, row = 0)
        
        frmNorteEste = ttk.Frame(frmNorte)
         
        btnAgregarImg = ttk.Button(frmNorteEste, 
                                   text="Agregar Imagen", 
                                   width = Util.getMnsjConf("VistaPrincipal", "tamBotones"))
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
        self.cmbClases = ttk.Combobox(frmCenterOeste, textvariable=self.selectedClase, state = 'readonly')
        self.cmbClases['values'] = Accion.dicClases.keys()
         
        self.cmbClases.pack(fill = tk.Y, pady = 5)
         
        ttk.Button(frmCenterOeste, text = "Mover Todo", width = Util.getMnsjConf("VistaPrincipal", "tamBotones")).pack(fill = tk.Y, pady = 5)
        ttk.Button(frmCenterOeste, text = "Eliminar Todo", width = Util.getMnsjConf("VistaPrincipal", "tamBotones")).pack(fill = tk.Y, pady = 5)
        
        ttk.Separator(frmCenterOeste, orient = tk.HORIZONTAL).pack(fill = tk.Y, expand = tk.TRUE)
        
        ttk.Button(frmCenterOeste, text = "Deshacer ultima Accion", width = Util.getMnsjConf("VistaPrincipal", "tamBotones")).pack(fill = tk.Y, pady = 5)
        
        frmCenterOeste.pack(fill = tk.BOTH, side = tk.LEFT, expand = tk.TRUE, padx = 5)
        
        frmCenterEste = ttk.Labelframe(frmCenter, text = "Imagenes de la clase")
        
        self.frame = TablaRutas(frmCenterEste)
        self.frame.pack(fill = tk.BOTH, expand = tk.TRUE)
        
        frmCenterEste.pack(fill = tk.BOTH, side = tk.LEFT, expand = tk.TRUE, padx = 5)
        
        frmCenter.pack(fill = tk.BOTH, side = tk.TOP, expand= tk.TRUE)
        
        #++++++++++++++++++++++++ Ventanas Emergentes ++++++++++++++++++++++++#
        self.frmVentanaCrearClase = VistaAgregarImgURLWeb(self.padre, self.crearClase)
        
    #-------------------------------------------------------------------------------        
    def crearClase(self):
        '''
        Metodo que crea una clase y refresca el combobox que contiene las clases de la vista
        '''
        try:
            CrearClase(self.frmVentanaCrearClase.nomNvaClase.get()).efectuarAccion()
            self.cmbClases['values'] = Accion.dicClases.keys()
            self.frmVentanaCrearClase.nomNvaClase.set("")
            self.frmVentanaCrearClase.hide()
        except Exception as ex:
            logger.error(ex)
        
        
    #-------------------------------------------------------------------------------
    def abrirVistaCrearClase(self):
        self.frmVentanaCrearClase.show()
        

########################################################################        
if __name__ == '__main__':
    root = tk.Tk()
    app = Principal(master=root)
    app.mainloop()
