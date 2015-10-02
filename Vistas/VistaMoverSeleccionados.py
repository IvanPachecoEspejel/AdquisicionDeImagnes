'''
Created on 18/09/2015

@author: ivan
'''

import ttk

from Modelo.Accion import Accion
from Modelo.MoverImagen import MoverImagen
import Tkinter as tk
from Utileria import Util


#########################################################################################
logger = Util.getLogger("VistaMoverSeleccionados")
#########################################################################################

class VistaMoverSeleccionados(tk.Toplevel):
    '''
    Ventana en la que se ofrece la posibilidad mover todas las imagenes que han sido seleccionadas
    '''
    #----------------------------------------------------------------------
    def __init__(self, master, claseOrigen, imgsAfectadas):
        '''
        Constructor
        '''
        tk.Toplevel.__init__(self, master)
        self.padre = master
        self.attributes('-topmost', tk.TRUE)
        self.title("Mueve las imagenes")
        self.initUI()
        self.claseOrigen = claseOrigen
        self.imgsAfectadas = imgsAfectadas
        self.hide()
        
    #----------------------------------------------------------------------
    def initUI(self):
        '''
        Crea y empaqueta los windgets de la ventana, tambien se establecen las propiedades
        de la ventana 
        '''
        self.geometry('350x100+300+100')
        self.protocol("WM_DELETE_WINDOW", "onexit")
        self.resizable(0,0)
        
        frmFondo = ttk.Frame(self)
        
        #.....................................................
        frmNorte = ttk.Frame(frmFondo)
        
        ttk.Label(frmNorte, text = 'Clase Destino: ').pack(side = tk.LEFT, padx = 5)
        
        self.selectedClase = tk.StringVar()
        self.selectedClase.set(Accion.nomClaseDefault)
        self.cmbClases = ttk.Combobox(frmNorte, 
                                      textvariable=self.selectedClase, 
                                      state = 'readonly')
        
        self.cmbClases['values'] = Accion.dicClases.keys()
         
        self.cmbClases.pack(side = tk.LEFT, fill = tk.Y, padx = 5)
        
        frmNorte.pack(side = tk.TOP, expand = tk.TRUE, pady = 10, padx = 20)
        #.....................................................
        frmSur = ttk.Frame(frmFondo)
        
        ttk.Button(frmSur, 
                   text = 'Mover',
                   command = self.moverImgs).pack(side = tk.LEFT, padx = 5)
                   
        ttk.Button(frmSur, 
                   text = 'Cancelar', 
                   command = self.hide).pack(side = tk.LEFT,padx = 5)
                   
        frmSur.pack(side = tk.TOP, expand = tk.TRUE, pady = 10, padx = 20)
        #.....................................................
        
        frmFondo.pack(fill = tk.BOTH, expand = tk.TRUE)
        
    #----------------------------------------------------------------------
    def moverImgs(self):
        lstAuxImgs = []
        lstAuxImgs.extend(self.imgsAfectadas)
        accion = MoverImagen(lstAuxImgs, self.claseOrigen.get(), self.selectedClase.get())
        accion.efectuarAccion()
        self.padre.actualizarClase(self.selectedClase.get())
        self.hide()
        
    #----------------------------------------------------------------------
    def hide(self):
        """
        Ocula la ventana 
        """
        self.withdraw()
        
    #----------------------------------------------------------------------
    def show(self):
        """
        Mustra la ventana
        """
        self.update()
        self.deiconify()
        self.selectedClase.set(Accion.nomClaseDefault)
        self.cmbClases['values'] = Accion.dicClases.keys()
        
#########################################################################################
        
if __name__ == "__main__":
    
    class SampleApp(tk.Tk):
        
        def __init__(self,*args, **kwargs):
            root = tk.Tk.__init__(self, *args, **kwargs)

            self.frmTabla = VistaMoverSeleccionados(root, Accion.nomClaseDefault, [])
            
        
    app = SampleApp()
    app.mainloop()
    