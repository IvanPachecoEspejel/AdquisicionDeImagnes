import Tkinter as tk
import ttk

#######################################################################
class ScrolledFrame(ttk.Frame):
    """A pure Tkinter scrollable frmTabla that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frmTabla
    * Construct and pack/place/grid normally
    * This frmTabla only allows vertical scrolling

    """
    #-------------------------------------------------------------------------------------
    def __init__(self, parent, *args, **kw):
        ttk.Frame.__init__(self, parent, *args, **kw)

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
        vscrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=False)
         
        hscrollbar = ttk.Scrollbar(self, orient=tk.HORIZONTAL)
        hscrollbar.pack(fill=tk.X, side=tk.BOTTOM, expand=False)
        
        self.canvas = tk.Canvas(self, bd=0, highlightthickness=0,
                           xscrollcommand = hscrollbar.set,
                           yscrollcommand = vscrollbar.set)
          
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        vscrollbar.config(command=self.canvas.yview)
        hscrollbar.config(command=self.canvas.xview) 
 
        # reset the view
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)
  
        # create a frmTabla inside the canvas which will be scrolled with it
        self.interior = ttk.Frame(self.canvas)        
        self.interior.pack(fill = tk.BOTH, expand = tk.TRUE)
        
        self.interior_id = self.canvas.create_window(0, 0, window=self.interior,
                                           anchor=tk.NW)

        # track changes to the canvaself.canvasfrmTabla width and sync them,
        # also updating the scrollbar
        self.interior.bind('<Configure>', self._configure_interior) 
        self.canvas.bind('<Configure>', self._configure_canvas)
        
    #-------------------------------------------------------------------------------------
    def _configure_canvas(self, event):
        '''
        Actualiza el tamanio del canvas para que pueda mostrar todos los widgets que contiene
        '''
        if self.interior.winfo_reqwidth() > self.canvas.winfo_width():
            self.canvas.itemconfigure(self.interior_id, width=self.interior.winfo_reqwidth())
        else:
            self.canvas.itemconfigure(self.interior_id, width=self.canvas.winfo_width())
        if self.interior.winfo_reqheight() > self.canvas.winfo_height():
            # update the inner frmTabla's height to fill the canvas
            self.canvas.itemconfigure(self.interior_id, height=self.interior.winfo_reqheight())
        else:
            self.canvas.itemconfigure(self.interior_id, height=self.canvas.winfo_height())
        
    #-------------------------------------------------------------------------------------
    def _configure_interior(self, event):
        '''
        Actualiza los scrollbars para que cuadren con el tamanio del canvas
        '''
        size = (self.interior.winfo_reqwidth(), self.interior.winfo_reqheight())
           
        self.canvas.config(scrollregion="0 0 %s %s" % size)
        if self.interior.winfo_reqwidth() > self.canvas.winfo_width():
            # update the canvas's width to fit the inner frmTabla
            self.canvas.config(width=self.interior.winfo_reqwidth())
        else:
            self.canvas.config(width=self.canvas.winfo_width())
        if self.interior.winfo_reqheight() > self.canvas.winfo_height():
            # update the canvas's heigth to fit the inner frmTabla
            self.canvas.config(height=self.interior.winfo_reqheight())
        else:
            self.canvas.config(height=self.canvas.winfo_height())
    
    #-------------------------------------------------------------------------------------
    def acutalizarScrollPane(self):
        '''
        Actualiza el scroll pane para que se muestren todos los widgets que se 
        encuentran en el canvas
        '''
        self._configure_canvas(None)
        self._configure_interior(None)
#######################################################################
if __name__ == "__main__":

    class SampleApp(tk.Tk):
        def __init__(self, *args, **kwargs):
            root = tk.Tk.__init__(self, *args, **kwargs)

            self.frmTabla = ScrolledFrame(root)
            self.frmTabla.pack(fill = tk.BOTH, expand = True)
            self.label = ttk.Label(text="Shrink the window to activate the scrollbar.")
            self.label.pack()
            buttons = []
            for i in range(30):
                buttons.append(ttk.Button(self.frmTabla.interior, text="Button " + str(i)))
                buttons[-1].grid(row = i, column =i)

    app = SampleApp()
    app.geometry('600x500+200+200')
    app.mainloop()