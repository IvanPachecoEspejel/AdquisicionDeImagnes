import Tkinter as tk
from Tkinter import StringVar
import ttk
from  Utileria import Util
from Modelo.Accion import Accion
from Modelo.CrearClase import CrearClase
from PIL import Image
import ImageTk

class Principal(tk.Frame):

    logger = Util.getLogger("Principal")
    
    def __init__(self, master=None,  *args, **kw):
        tk.Frame.__init__(self, master, *args, **kw)
        self.parent = master
        self.parent.geometry('600x500+200+200')
        self.initUI()

    def initUI(self):
        self.parent.title("Adquicicion de imagenes")
        
        lblLogo = ttk.Label(self.parent, background = "green", text="Logo")
        lblLogo.grid(row = 0, column = 0)
        
        btnAgregarImg = ttk.Button(self.parent, text="Agregar Imagen")
        btnAgregarImg.grid(row=0, column = 1)
        
        self.selectedClase = StringVar()
        self.cmbClases = ttk.Combobox(self.parent, textvariable=self.selectedClase, state = 'readonly')
        self.cmbClases['values'] = Accion.clases.keys()
        
        self.cmbClases.grid(row = 1, column = 0)
        
        self.nomNvaClase = StringVar()
        ttk.Entry(self.parent, textvariable = self.nomNvaClase).grid(row = 1, column = 1)
        
        ttk.Button(self.parent, text = 'Crear Clase', command = self.crearClase).grid(row = 1, column = 2)

        ttk.Button(self.parent, text = "Mover Todo").grid(row = 3, column= 0)
        ttk.Button(self.parent, text = "Eliminar Todo").grid(row = 4, column = 0)
        
    def crearClase(self):
        CrearClase(self.nomNvaClase.get()).efectuarAccion()
        self.cmbClases['values'] = Accion.clases.keys()
        self.nomNvaClase.set("")
         
    def agregarImagenes(self):
        self.logger.info("Agregando imagenes")
        
if __name__ == '__main__':
    root = tk.Tk()
    app = Principal(master=root)
    #root.after(30000, lambda: root.destroy())
    app.mainloop()
