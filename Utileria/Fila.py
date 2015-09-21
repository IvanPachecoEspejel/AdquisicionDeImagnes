from Utileria import Util
from PIL import Image

import Tkinter as tk
import ttk
import ImageTk

log = Util.getLogger("Fila") 

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
        
        self.strVarEstaSelecccionado = tk.StringVar()
        self.chekbImg = ttk.Checkbutton(tabla.frame.interior, variable = self.strVarEstaSelecccionado, command = self.checarSeleccion)
        
        self.lblRuta = tk.Text(tabla.frame.interior,height=int(Util.getMnsjConf("TablaRutas", "altoCeldaRuta")))
        self.lblRuta.insert(1.0, imagen.source)
        self.lblRuta.config(state = tk.DISABLED)
        
        self.iconoImg = Image.open(imagen.source)
        self.iconoImg.thumbnail((
                int(Util.getMnsjConf("TablaRutas", "altoImgMuestra")),
                int(Util.getMnsjConf("TablaRutas", "anchoImgMuestra"))
                ), Image.ANTIALIAS)
        self.iconoImg = ImageTk.PhotoImage(self.iconoImg)
        self.lblImg = ttk.Label(tabla.frame.interior, image = self.iconoImg)
        
        self.img = imagen
        self.tabla = tabla
        
    def checarSeleccion(self):
        '''
        Verifica se el checkButton esta seleccionado o no, y dependiendo de su estado
        efectua una accion
        '''
        if self.strVarEstaSelecccionado.get() == '0':
            self.tabla.desseleccionarFila(self)
        elif self.strVarEstaSelecccionado.get() == '1':
            self.tabla.seleccionarFila(self)
        else:
            log.error("Error al chekar la seleecion de la imagen "+self.img.source+" valor: "+self.strVarEstaSelecccionado.get())
            
    def empaquetar(self, numFila):
        '''
        Empaquete todos los widgets de esta fila en la tabla que se paso en los parametros
        del constructor
        '''
        self.chekbImg.grid(column = 0, row = numFila)
        self.lblRuta.grid(column = 1, row = numFila)
        self.lblImg.grid(column = 2, row = numFila)