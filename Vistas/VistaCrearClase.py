'''
Created on 18/09/2015

@author: ivan
'''

import ttk
import Tkinter as tk

#########################################################################################

class VistaCrearClase(tk.Toplevel):
    '''
    Ventana en la que se ofrece la posibilidad de crear una clase
    '''
    
    def __init__(self, master = None, crearClase= None):
        '''
        Constructor
        '''
        tk.Toplevel.__init__(self, master)
        self.padre = master
        self.attributes('-topmost', tk.TRUE)
        self.title("Creacion de una clase")
        self.comandoCrearClase = crearClase
        self.initUI()
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
        
        frmClases = ttk.Labelframe(self,text = "Cracion de una clase")
        
        ttk.Label(frmClases, text = 'Nombre de la nueva clase: ').grid(row = 0, column = 0, pady = 10)
        self.strVarNomNvaClase = tk.StringVar()
        ttk.Entry(frmClases, textvariable = self.strVarNomNvaClase).grid(row = 0, column = 1, pady = 10)
        
        frmSur = ttk.Frame(frmClases)
        
        ttk.Button(frmSur, 
                   text = 'Crear Clase', 
                   command = self.comandoCrearClase).pack(side = tk.LEFT, padx = 5)
                   
        ttk.Button(frmSur, 
                   text = 'Cancelar', 
                   command = self.hide).pack(side = tk.LEFT,padx = 5)
                   
        frmSur.grid(row = 1, 
                    column = 0, 
                    columnspan = 2, 
                    pady = 10)
        
        frmClases.pack(fill = tk.BOTH)
        
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
        
#########################################################################################
        
if __name__ == "__main__":
    
    class SampleApp(tk.Tk):
        
        def crearClase(self):
            print "creando clase"
        
        def __init__(self,*args, **kwargs):
            root = tk.Tk.__init__(self, *args, **kwargs)

            self.frmTabla = VistaCrearClase(root,self.crearClase)
            
        
    app = SampleApp()
    app.mainloop()
        
        
    
        
