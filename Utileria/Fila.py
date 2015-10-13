import cStringIO
import ttk
import urllib

import Image
import ImageTk

import Tkinter as tk
from Utileria import Util

from Vistas.VistaVisualizacionImgs import VistaVisualizacionImgs

################################################################################################
log = Util.getLogger("Fila") 
################################################################################################
class Fila(object):
    '''
    Cada instancia tiene dos objetos widgets que representan columnas en la tabla
    uno para mostrar la url de la imagen y otro para previsualizar la imagen
    '''
    
    #------------------------------------------------------------------------------------
    def __init__(self, img, tabla):
        '''
        Crea los widgets correspondientes a imagen que estaran contenidos en tabla que 
        se pasa como parametro
        '''
        
        self.strVarEstaSelecccionado = tk.StringVar()
        self.chekbImg = ttk.Checkbutton(tabla.frmScrollPane.interior, 
                                        variable = self.strVarEstaSelecccionado, 
                                        command = self.checarSeleccion)
        
        self.lblRuta = tk.Text(tabla.frmScrollPane.interior,
                               height=int(Util.getMnsjConf("TablaRutas", "altoCeldaRuta")))
        
        self.lblRuta.insert(1.0, img.source)
        self.lblRuta.config(state = tk.DISABLED)
        
        self.widgetPrevisualizacion = None
        
        self.tabla = tabla
        self.img = img
    
    #------------------------------------------------------------------------------------    
    def checarSeleccion(self):
        '''
        Verifica se el checkButton de imagen seleccionada esta activado o no, y dependiendo de su estado
        efectua una accion
        '''
        if self.strVarEstaSelecccionado.get() == '0':
            self.tabla.desseleccionarImg(self.img)
        elif self.strVarEstaSelecccionado.get() == '1':
            self.tabla.seleccionarImg(self.img)
        else:
            log.error("Error al chekar la seleecion de la imagen "
                      + self.img.source
                      + " valor: "
                      + self.strVarEstaSelecccionado.get())
            
    #------------------------------------------------------------------------------------            
    def crearWidgetImg(self):
                     
        iconoImg = self.crearIconoImagen()
        
        iconoImg.thumbnail((
                int(Util.getMnsjConf("TablaRutas", "altoImgMuestra")),
                int(Util.getMnsjConf("TablaRutas", "anchoImgMuestra"))
                ), Image.ANTIALIAS)
        
        self.iconoPhotoImg = ImageTk.PhotoImage(iconoImg)
        widgetImg = ttk.Label(self.tabla.frmScrollPane.interior, image = self.iconoPhotoImg)
        
        return widgetImg
    
    #------------------------------------------------------------------------------------
    def crearIconoImagen(self):
        if self.img.tipoRuta == Util.RUTA_LOCAL:
            iconoImg = Image.open(self.img.source)
        else:
            try:
                iconoImg = Image.open(cStringIO.StringIO(urllib.urlopen(self.img.source).read()))
            except IOError as io:
                iconoImg = Image.open(cStringIO.StringIO(urllib.urlopen(Util.rutaImg_ImgNoEncontrada).read()))
                self.img.source = Util.rutaImg_ImgNoEncontrada
                self.img.t
                log.error(io)
        return iconoImg
    #------------------------------------------------------------------------------------
    def crearWidgetBoton(self):
        widgetImg = ttk.Button(self.tabla.frmScrollPane.interior, 
                                    text = 'Ver Imagen',
                                    command = self.visualizarImg)
        
        return widgetImg
        
    #------------------------------------------------------------------------------------            
    def visualizarImg(self):                    
        VistaVisualizacionImgs(self.tabla, self.img)

    #------------------------------------------------------------------------------------            
    def empaquetar(self, numFila):
        '''
        Empaquete todos los widgets de esta fila en la tabla que se paso en los parametros
        del constructor
        '''
        if self.tabla.boolVarVerImgs.get() :
            if self.widgetPrevisualizacion is None or self.widgetPrevisualizacion.__class__ != ttk.Label:
                self.widgetPrevisualizacion = self.crearWidgetImg()
        else:
            if self.widgetPrevisualizacion is None or self.widgetPrevisualizacion.__class__ != ttk.Button:
                self.widgetPrevisualizacion = self.crearWidgetBoton()
            
        self.chekbImg.grid(column = 0, row = numFila)
        self.lblRuta.grid(column = 1, row = numFila)
        self.widgetPrevisualizacion.grid(column = 2, row = numFila)
        
################################################################################################