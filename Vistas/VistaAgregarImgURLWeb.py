'''
Created on 18/09/2015

@author: ivan
'''

import ttk

import Tkinter as tk


#########################################################################################
class VistaAgregarImgURLWeb(tk.Toplevel):
    '''
    Ventana en la que se ofrece la posibilidad de ingresar la url de una pagina web
    '''
    
    def __init__(self, master = None, comando = None):
        '''
        Constructor
        '''
        tk.Toplevel.__init__(self, master)
        self.padre = master
        self.attributes('-topmost', tk.TRUE)
        self.comandoAgregarImg = comando
        self.title("URL WEB")
        self.initUI()
        self.hide()
        
    #----------------------------------------------------------------------
    
    def initUI(self):
        '''
        Crea y empaqueta los windgets de la ventana, tambien se establecen las propiedades
        de la ventana 
        '''
        self.geometry('700x90+300+100')
        self.protocol("WM_DELETE_WINDOW", "onexit")
        self.resizable(0,0)
        
        frmFondo = ttk.Frame(self)
        
        frmNorte = ttk.Frame(frmFondo)
        
        ttk.Label(frmNorte, text = 'URL: ').pack(side = tk.LEFT)
        self.nomNvaImg = tk.StringVar()
        ttk.Entry(frmNorte, 
                  textvariable = self.nomNvaImg,
                  width = 70).pack(side = tk.LEFT, expand = tk.TRUE)
        
        frmNorte.pack(side = tk.TOP, expand = tk.TRUE, pady = 10, padx= 20)
        
        frmSur = ttk.Frame(frmFondo)
        
        ttk.Button(frmSur, 
                   text = 'Agregar Imagen',
                   command = self.comandoAgregarImg).pack(side = tk.LEFT, padx = 5)
                   
        ttk.Button(frmSur, 
                   text = 'Cancelar', 
                   command = self.hide).pack(side = tk.LEFT,padx = 5)
                   
        frmSur.pack(side = tk.TOP, expand = tk.TRUE, pady = 10)
        
        frmFondo.pack(fill = tk.BOTH, expand = tk.TRUE)
        
    #----------------------------------------------------------------------
    def hide(self):
        """
        Ocula la ventana 
        """
        self.withdraw()
        self.padre.show()
        
    #----------------------------------------------------------------------
    def show(self):
        """
        Mustra la ventana
        """
        self.update()
        self.deiconify()
        self.padre.hide()
        
        
#########################################################################################
        
if __name__ == "__main__":
    
    class SampleApp(tk.Tk):
        
        def __init__(self,*args, **kwargs):
            root = tk.Tk.__init__(self, *args, **kwargs)

            self.frmTabla = VistaAgregarImgURLWeb(root)
            
        
    app = SampleApp()
    app.mainloop()
        
        
    
        
