'''
Created on 04/10/2015

@author: ivan
'''

import ttk
import Image
import Tkinter as tk
from Utileria import Util
import cStringIO
import urllib
import ImageTk

log = Util.getLogger("VistaVisualizacionImgs") 
########################################################################################
class VistaVisualizacionImgs(tk.Toplevel):
    '''
    Vista para poder visualizar una imagen
    '''
    #----------------------------------------------------------------------
    def __init__(self, master, imagen):
        tk.Toplevel.__init__(self, master)
        self.padre = master
        self.img = imagen
        self.attributes('-topmost', tk.TRUE)
        self.resizable(0, 0)
        self.title(imagen.getNomArchivo())
        self.initUI()
        
    #----------------------------------------------------------------------
    def initUI(self):
        fondo = ttk.Frame(self)
                
        if self.img.tipoRuta == Util.RUTA_LOCAL:        
            iconoImg = Image.open(self.img.source)
        else:
            try:
                iconoImg = Image.open(cStringIO.StringIO(urllib.urlopen(self.img.source).read()))
            except IOError as io:
                iconoImg = Image.open(cStringIO.StringIO(urllib.urlopen(Util.rutaImg_ImgNoEncontrada).read()))
                log.error(io)
#                 raise io
             
        iconoImg.thumbnail((
                int(Util.getMnsjConf("TablaRutas", "altoImgPreVis")),
                int(Util.getMnsjConf("TablaRutas", "anchoImgPreVis"))
                ), Image.ANTIALIAS)
        
        self.iconoPhotoImg = ImageTk.PhotoImage(iconoImg)
        ttk.Label(fondo, image = self.iconoPhotoImg).pack(expand = tk.TRUE,
                                                          fill = tk.BOTH)
        
        ttk.Button(fondo, 
                   text = "Aceptar",
                   command = self.close).pack(anchor = tk.NE, 
                                              pady = 10, 
                                              padx = 20)
        
        fondo.pack(expand = tk.TRUE, fill = tk.BOTH)
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
        
    #----------------------------------------------------------------------
    def close(self):
        '''
        Cierra la ventana
        '''
        self.destroy()
        
########################################################################################

if __name__ == "__main__":
    
    from Utileria.Imagen import Imagen
    
    class EjemploApp(tk.Tk):
        
        def __init__(self, *args, **kwargs):
            root = tk.Tk.__init__(self, *args, **kwargs)
#             img = Imagen("/home/ivan/Imagenes/fondos/fondoHapy.jpg")
            img = Imagen("http://asdfasdfadf.jpg")
            VistaVisualizacionImgs(root, img)
            
    app = EjemploApp()
    app.mainloop()