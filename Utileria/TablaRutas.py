'''
Created on 07/09/2015

@author: ivan
'''

import Tkinter as tk
from Utileria.ScrolledFrame import ScrolledFrame
import Utileria.Util as Util
from Utileria.Imagen import Imagen
import ttk
from PIL import Image
import ImageTk
import re
from Modelo.Accion import Accion
from Modelo.AgregarImagen import AgregarImagen

class TablaRutas (ttk.Frame):
    '''
    Clase que crea una tabla en un Frame con scrolls, 
    especifica para agrear filas con a base de la clase Imagen
    '''
    
    def __init__(self,  parent, *args, **kw):
        '''
        Inicializa un frame con scroll y crea la cabezera de la tabla
        '''
        ttk.Frame.__init__(self, parent, *args, **kw)
        
        #Se tiene un diccionario que tiene las mismas clases que se 
        #tiene en la clase Accion como llaves con diferencia de que 
        #este diccionario contendra las filas ya procesadas como 
        #widgets para la tablay poder agilizar la app
        self.clases = {} 
        self.filterFilas = [] 
        
        self.expRegBusqueda = tk.StringVar()
        ttk.Entry(parent, textvariable=self.expRegBusqueda).pack(fill = tk.X)

        self.iconoBusqueda = Image.open("../Imgs/iconoBusqueda.png")
        self.iconoBusqueda.thumbnail((20,20), Image.ANTIALIAS)
        self.iconoBusqueda = ImageTk.PhotoImage(self.iconoBusqueda)
        tk.Button(parent, image=self.iconoBusqueda, command=self.buscar).pack(fill = tk.X)
        
        self.frame = ScrolledFrame(parent)
        self.frame.pack(fill = tk.BOTH, expand = True)
            
        self.cambiarDeClase(Accion.nomClaseDefault)    
    
    def cambiarDeClase(self, nombreClase):
        '''
        Cambia de clase actualizando la tabla con las rutas de la clase
        '''
        self.nomClaseActual = nombreClase
        
        self.cargarClase(nombreClase)
        
        self.empaquetarFilas()
         
        
    def cargarClase(self, nombreClase):
        '''
        Crea las filas de la tabla cargando los datos que se tiene en la clase Accion
        @param nombreClase: clase que se cargara localmente
        @return: Regresa una lista de objetos Fila que tiene los dato 
                procesados de la clase pasada en los parametros
        '''
        
        if self.clases.get(nombreClase) is None:
            
            clase = Accion.clases.get(nombreClase)
            self.filas = []
            
            for img in clase.values():
                self.filas.append(Fila(img, self.frame.interior))
                
            self.clases[nombreClase] = self.filas
                
        else:
            self.filas = self.clases.get(nombreClase)
        
        self.limpiarRegistroFiltro() 
        for img in self.filas : self.filterFilas.append(img)
            
    
    def empaquetarFilas(self):
        '''
        Agrega todas los widgets de los objetos fila que se encuentran en la lista filterFilas
        al frame de la tabla
        '''
        self.limpiarTabla()
        
        i = 1
        for fila in self.filterFilas:
            fila.lblRuta.grid(column = 0, row = i)
            fila.lblImg.grid(column = 1, row = i)
            i = i+1
            
    def limpiarTabla(self):
        '''
        Elimina todos los widgets del frame
        '''
        for a in self.frame.interior.winfo_children(): a.grid_forget()
        
        cabezera = Util.getMnsjConf("TablaRutas", "cabezera").split(",")
        for i in range(len(cabezera)):
            ttk.Label(self.frame.interior, text = cabezera[i]).grid(row = 0, column = i, sticky = tk.W+tk.E, padx = 10)
        
    def limpiarRegistroFiltro(self):
        '''
        Limpia la lista de filas que se utiliza para realizar la busqueda
        '''
        while len(self.filterFilas) > 0 : del self.filterFilas[0]
        
    def buscar(self):
        '''
        Busca utilizando expresiones regulares, todos los objetos Imgen de todos los objetos
        Fila que se encuentran en la lista filas
        '''
        
        if self.expRegBusqueda.get() is None :
            raise Exception(Util.getMnsjIdioma("TablaRutas", "Error_Exp_Reg_None"))
        
        self.limpiarRegistroFiltro()
        
        try:
            for fila in self.filas:
                if(re.search(self.expRegBusqueda.get(),fila.img.source) is not None):
                    self.filterFilas.append(fila)
        except Exception:
            raise Exception(Util.getMnsjIdioma("TablaRutas", "Error_Exp_Reg_Inv"))
                
        self.empaquetarFilas()
        
class Fila(object):
    '''
    Cada instancia tiene dos objetos widgets que representan columnas en la tabla
    uno para mostrar la url de la imagen y otro para previsualizar la imagen
    '''
    
    def __init__(self, imagen, tabla):
        '''
        Crea los widgets correspondientes a imagen que estaran contenidos en tabla que 
        se pasa como parametro
        '''
        self.lblRuta = tk.Text(tabla,height=int(Util.getMnsjConf("TablaRutas", "altoCeldaRuta")))
        
        self.lblRuta.insert(1.0, imagen.source)
        self.iconoImg = Image.open(imagen.source)
        self.iconoImg.thumbnail((
                int(Util.getMnsjConf("TablaRutas", "altoImgMuestra")),
                int(Util.getMnsjConf("TablaRutas", "anchoImgMuestra"))
                ), Image.ANTIALIAS)
        self.iconoImg = ImageTk.PhotoImage(self.iconoImg)
        self.lblImg = ttk.Label(tabla, image = self.iconoImg)
        self.img = imagen
    
if __name__ == "__main__":
    
    class SampleApp(tk.Tk):
        
        def __init__(self,*args, **kwargs):
            root = tk.Tk.__init__(self, *args, **kwargs)

            self.frame = TablaRutas(root)
            self.frame.pack(fill = tk.BOTH, expand = True)

    img1 = Imagen("/home/ivan/Imagenes/fondos/02E3A832D.jpg")
    img2 = Imagen("/home/ivan/Imagenes/fondos/1_rajathilaknatarajan-redsky.jpg")
    a = (img1, img2)
     
    agregarImgs = AgregarImagen(a)
    agregarImgs.efectuarAccion()
        
    app = SampleApp()
    app.geometry('800x500+200+200')
    app.mainloop()