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
from Utileria.Fila import Fila
import ImageTk
import re
from Modelo.Accion import Accion
from Modelo.AgregarImagen import AgregarImagen

log = Util.getLogger("TablaRutas")

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
        
        #Se tiene un diccionario que tiene las mismas dicClases que se 
        #tiene en la clase Accion como llaves con diferencia de que 
        #este diccionario contendra las filas ya procesadas como 
        #widgets para la tablay poder agilizar la app
        self.dicClases = {} 
        self.lstFilasFiltradas = [] 
        self.lstFilasSeleccionadas = []
        
        self.expRegBusqueda = tk.StringVar()
        ttk.Entry(self, textvariable=self.expRegBusqueda).pack(fill = tk.X)

        self.iconoBusqueda = Image.open("../Imgs/iconoBusqueda.png")
        self.iconoBusqueda.thumbnail((20,20), Image.ANTIALIAS)
        self.iconoBusqueda = ImageTk.PhotoImage(self.iconoBusqueda)
        ttk.Button(self, image=self.iconoBusqueda, command=self.buscar).pack(fill = tk.X)
        
        self.frame = ScrolledFrame(self)
        self.frame.pack(fill = tk.BOTH, expand = True)
            
        self.cambiarDeClase(Accion.nomClaseDefault)    
    
    def cambiarDeClase(self, nombreClase):
        '''
        Cambia de clase actualizando la tabla con las rutas de la clase
        '''
        self.nomClaseActual = nombreClase
        
        self.cargarClase(nombreClase)
        
        self.empaquetarWidgetsTabla()
         
        
    def cargarClase(self, nombreClase):
        '''
        Crea las filas de la tabla cargando los datos que se tiene en la clase Accion
        @param nombreClase: clase que se cargara localmente
        @return: Regresa una lista de objetos Fila que tiene los dato 
                procesados de la clase pasada en los parametros
        '''
        
        if self.dicClases.get(nombreClase) is None:
            
            clase = Accion.dicClases.get(nombreClase)
            self.filas = []
            
            for img in clase.values():
                self.filas.append(Fila(img, self))
                
            self.dicClases[nombreClase] = self.filas
                
        else:
            self.filas = self.dicClases.get(nombreClase)
            
        self.limpiarLstFilasSeleccionadas()
        self.limpiarLstFilasFiltradas() 
        for img in self.filas : self.lstFilasFiltradas.append(img)
        
    def buscar(self):
        '''
        Busca utilizando expresiones regulares, todos los objetos Imgen de todos los objetos
        Fila que se encuentran en la lista filas
        '''
        
        if self.expRegBusqueda.get() is None :
            raise Exception(Util.getMnsjIdioma("TablaRutas", "Error_Exp_Reg_None"))
        
        self.limpiarLstFilasSeleccionadas()
        self.limpiarLstFilasFiltradas()
        
        try:
            for fila in self.filas:
                if(re.search(self.expRegBusqueda.get(),fila.img.source) is not None):
                    self.lstFilasFiltradas.append(fila)
        except Exception:
            raise Exception(Util.getMnsjIdioma("TablaRutas", "Error_Exp_Reg_Inv"))
                
        self.empaquetarWidgetsTabla()
            
    
    def empaquetarWidgetsTabla(self):
        '''
        Agrega todas los widgets de los objetos fila que se encuentran en la lista lstFilasFiltradas
        al frame de la tabla y tambien crea los widgets y los empequeta de la cabezera
        '''
        self.limpiarTabla()
        
        self.empaquetarCabezeraTabla()
        
        i = 1
        for fila in self.lstFilasFiltradas:
            fila.empaquetar(i)
            i = i+1
            
    def empaquetarCabezeraTabla(self):
        '''
        Crea los widgets de la cabezera de la tabla y los empaqueta en ella
        '''
        cabezera = Util.getMnsjConf("TablaRutas", "cabezera").split(",")
        self.strVarEstanSelecTodos = tk.StringVar()
        self.strVarEstanSelecTodos.set('0')
        ttk.Checkbutton(self.frame.interior, 
                        variable = self.strVarEstanSelecTodos, 
                        command = self.seleccionarDeseleccionarTodo,).grid(row = 0, 
                                                                           column = 0,
                                                                           padx = 5)
        
        for i in range(len(cabezera)):
            ttk.Label(self.frame.interior, 
                      text = cabezera[i]).grid(row = 0, 
                                                 column = i+1,
                                                 padx = 5)
        
        self.frame.interior.grid_columnconfigure(0, weight = 1)    
        self.frame.interior.grid_columnconfigure(1, weight = 2)
        self.frame.interior.grid_columnconfigure(2, weight = 1)

    def limpiarTabla(self):
        '''
        Elimina todos los widgets del frame
        '''
        for a in self.frame.interior.winfo_children(): a.grid_forget()
        
    def limpiarLstFilasFiltradas(self):
        '''
        Limpia la lista de filas que se utiliza para realizar la busqueda
        '''
        while len(self.lstFilasFiltradas) > 0 : del self.lstFilasFiltradas[0]
        
    def limpiarLstFilasSeleccionadas(self):
        '''
        Limpia la lista de imagenes que hayan sido seleccionadas
        '''
        while len(self.lstFilasSeleccionadas) > 0 :
            self.lstFilasSeleccionadas[0].strVarEstaSelecccionado.set('0')
            del self.lstFilasSeleccionadas[0]
            
    def seleccionarDeseleccionarTodo(self):
        '''
        Verifica si el checkBox que se utiliza para seleccionar todos esta seleccionado
        y dependiendo de su estado efectua cierta tarea
        '''
        self.limpiarLstFilasSeleccionadas()
        if self.strVarEstanSelecTodos.get() == '0':
            for fila in self.lstFilasFiltradas: fila.strVarEstaSelecccionado.set('0')
            log.info("Todas las filas deseleccionadas")
        elif self.strVarEstanSelecTodos.get() == '1':
            for fila in self.lstFilasFiltradas:
                self.lstFilasSeleccionadas.append(fila) 
                fila.strVarEstaSelecccionado.set('1')
                
            log.info("Todas las filas seleccionadas")
        else:
            log.error("Seleccionar todos, Valor desconocido "+self.strVarEstanSelecTodos.get())
            
    
    def seleccionarFila(self, fila):
        '''
        Agrea el objeto fila de los parametros a la lista lstFilasSeleccionadas
        '''
        self.lstFilasSeleccionadas.append(fila)
        log.info("Fila "+fila.img.source+" seleccionada")
    
    def desseleccionarFila(self, fila):
        '''
        Trata de eliminar el objeto fila de los parametros de la lista lstFilasSeleccionadas
        '''
        try:
            self.lstFilasSeleccionadas.remove(fila)
            log.info("Fila "+fila.img.source+" deseleccionada")
        except ValueError:
            log.error("Error interno al seleccionar fila no previamente seleccionada: "+fila.img.source)
        
    
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