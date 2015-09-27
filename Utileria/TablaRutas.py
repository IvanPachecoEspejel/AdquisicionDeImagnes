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

#######################################################################

log = Util.getLogger("TablaRutas")

#######################################################################

class TablaRutas (ttk.Frame):
    '''
    Clase que crea una tabla en un Frame con scrolls, 
    especifica para agrear filas con a base de la clase Imagen
    '''
    #-----------------------------------------------------------------------
    def __init__(self,  parent, *args, **kw):
        '''
        Inicializa un frmTabla con scroll y crea la cabezera de la tabla
        '''
        ttk.Frame.__init__(self, parent, *args, **kw)
        
        self.lstImgsFiltradas = [] 
        self.lstImgsSeleccionadas = []
        
        self.expRegBusqueda = tk.StringVar()
        ttk.Entry(self, textvariable=self.expRegBusqueda).pack(fill = tk.X)

        self.iconoBusqueda = Image.open("../Imgs/iconoBusqueda.png")
        self.iconoBusqueda.thumbnail((20,20), Image.ANTIALIAS)
        self.iconoBusqueda = ImageTk.PhotoImage(self.iconoBusqueda)
        ttk.Button(self, image=self.iconoBusqueda, command=self.buscar).pack(fill = tk.X)
        
        self.frmTabla = ScrolledFrame(self)
        self.frmTabla.pack(fill = tk.BOTH, expand = True)
            
        self.cambiarDeClase(Accion.nomClaseDefault)    
    
    #-----------------------------------------------------------------------
    def cambiarDeClase(self, nombreClase):
        '''
        Cambia de clase actualizando la tabla con las rutas de la clase
        '''
        self.nomClaseActual = nombreClase
        
        self.cargarClase(nombreClase)
        
        self.empaquetarWidgetsTabla()
         
    
    #-----------------------------------------------------------------------
    def cargarClase(self, nombreClase):
        '''
        Crea las filas de la tabla cargando los datos que se tiene en la clase Accion
        @param nombreClase: clase que se cargara localmente
        @return: Regresa una lista de objetos Fila que tiene los dato 
                procesados de la clase pasada en los parametros
        '''
        
        self.imgs = Accion.dicClases.get(nombreClase).values()
            
        self.limpiarLstImgsSeleccionadas()
        self.limpiarLstImgsFiltradas() 
        for img in self.imgs : self.lstImgsFiltradas.append(img)
    
    #-----------------------------------------------------------------------
    def buscar(self):
        '''
        Busca utilizando expresiones regulares, todos los objetos Imgen de todos los objetos
        Fila que se encuentran en la lista filas
        '''
        
        if self.expRegBusqueda.get() is None :
            raise Exception(Util.getMnsjIdioma("TablaRutas", "Error_Exp_Reg_None"))
        
        self.limpiarLstImgsSeleccionadas()
        self.limpiarLstImgsFiltradas()
        
        try:
            for img in self.imgs:
                if(re.search(self.expRegBusqueda.get(),img.source) is not None):
                    self.lstImgsFiltradas.append(img)
        except Exception:
            raise Exception(Util.getMnsjIdioma("TablaRutas", "Error_Exp_Reg_Inv"))
                
        self.empaquetarWidgetsTabla()
            
    #-----------------------------------------------------------------------
    def empaquetarWidgetsTabla(self):
        '''
        Agrega todas los widgets de los objetos fila que se encuentran en la lista lstFilasFiltradas
        al frmTabla de la tabla y tambien crea los widgets y los empequeta de la cabezera
        '''
        self.limpiarTabla()
        
        self.empaquetarCabezeraTabla()
        
        i = 1
        for img in self.lstImgsFiltradas:
            img.widgetFila.empaquetar(i)
            i = i+1
        
        self.update()
    
    #-----------------------------------------------------------------------
    def empaquetarCabezeraTabla(self):
        '''
        Crea los widgets de la cabezera de la tabla y los empaqueta en ella
        '''
        cabezera = Util.getMnsjConf("TablaRutas", "cabezera").split(",")
        self.strVarEstanSelecTodos = tk.StringVar()
        self.strVarEstanSelecTodos.set('0')
        ttk.Checkbutton(self.frmTabla.interior, 
                        variable = self.strVarEstanSelecTodos, 
                        command = self.seleccionarDeseleccionarTodo,).grid(row = 0, 
                                                                           column = 0,
                                                                           padx = 5)
        
        for i in range(len(cabezera)):
            ttk.Label(self.frmTabla.interior, 
                      text = cabezera[i]).grid(row = 0, 
                                                 column = i+1,
                                                 padx = 5)
        
        self.frmTabla.interior.grid_columnconfigure(0, weight = 1)    
        self.frmTabla.interior.grid_columnconfigure(1, weight = 2)
        self.frmTabla.interior.grid_columnconfigure(2, weight = 1)

    #-----------------------------------------------------------------------
    def limpiarTabla(self):
        '''
        Elimina todos los widgets del frmTabla
        '''
        for a in self.frmTabla.interior.winfo_children(): a.grid_forget()
        
        self.update()
    
    #-----------------------------------------------------------------------
    def limpiarLstImgsFiltradas(self):
        '''
        Limpia la lista de filas que se utiliza para realizar la busqueda
        '''
        while len(self.lstImgsFiltradas) > 0 : del self.lstImgsFiltradas[0]
    
    #-----------------------------------------------------------------------
    def limpiarLstImgsSeleccionadas(self):
        '''
        Limpia la lista de imagenes que hayan sido seleccionadas
        '''
        while len(self.lstImgsSeleccionadas) > 0 :
            self.lstImgsSeleccionadas[0].widgetFila.strVarEstaSelecccionado.set('0')
            del self.lstImgsSeleccionadas[0]
    
    #-----------------------------------------------------------------------
    def seleccionarDeseleccionarTodo(self):
        '''
        Verifica si el checkBox que se utiliza para seleccionar todos esta seleccionado
        y dependiendo de su estado efectua cierta tarea
        '''
        self.limpiarLstImgsSeleccionadas()
        if self.strVarEstanSelecTodos.get() == '0':
            for img in self.lstImgsFiltradas: img.widgetFila.strVarEstaSelecccionado.set('0')
            log.info("Todas las filas deseleccionadas")
        elif self.strVarEstanSelecTodos.get() == '1':
            for img in self.lstImgsFiltradas:
                self.lstImgsSeleccionadas.append(img) 
                img.widgetFila.strVarEstaSelecccionado.set('1')
                
            log.info("Todas las filas seleccionadas")
        else:
            log.error("Seleccionar todos, Valor desconocido "+self.strVarEstanSelecTodos.get())
    
    #-----------------------------------------------------------------------
    def seleccionarImg(self, img):
        '''
        Agrea el objeto img de los parametros a la lista lstImgsSeleccionadas
        '''
        self.lstImgsSeleccionadas.append(img)
        log.info("Fila "+img.source+" seleccionada")
    
    #-----------------------------------------------------------------------
    def desseleccionarImg(self, img):
        '''
        Trata de eliminar el objeto fila de los parametros de la lista lstImgsSeleccionadas
        '''
        try:
            self.lstImgsSeleccionadas.remove(img)
            log.info("Fila "+img.source+" deseleccionada")
        except ValueError:
            log.error("Error interno al seleccionar fila no previamente seleccionada: "+img.source)
    
    #-----------------------------------------------------------------------
    def agregarImagen(self, nombreClase, img):
        filas = self.dicClases[nombreClase]
        filas.append(Fila(img, self))

#######################################################################    
if __name__ == "__main__":
    
    class SampleApp(tk.Tk):
        
        def __init__(self,*args, **kwargs):
            root = tk.Tk.__init__(self, *args, **kwargs)

            self.frmTabla = TablaRutas(root)
            self.frmTabla.pack(fill = tk.BOTH, expand = True)
            img1 = Imagen("/home/ivan/Imagenes/fondos/02E3A832D.jpg",self.frmTabla)
            img2 = Imagen("/home/ivan/Imagenes/fondos/1_rajathilaknatarajan-redsky.jpg",self.frmTabla)
            a = (img1, img2)
            agregarImgs = AgregarImagen(a)
            agregarImgs.efectuarAccion()
            self.frmTabla.cambiarDeClase(Accion.nomClaseDefault)
            self.frmTabla.update()
            
    app = SampleApp()
    app.geometry('800x500+200+200')
    app.mainloop()