import Tkinter as tk
import ttk

# http://tkinter.unpythonic.net/wiki/VerticalScrolledFrame

class ScrolledFrame(ttk.Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame
    * Construct and pack/place/grid normally
    * This frame only allows vertical scrolling

    """
    def __init__(self, parent, *args, **kw):
        ttk.Frame.__init__(self, parent, *args, **kw)

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
        vscrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=False)
         
        hscrollbar = ttk.Scrollbar(self, orient=tk.HORIZONTAL)
        hscrollbar.pack(fill=tk.X, side=tk.BOTTOM, expand=False)
        
        canvas = tk.Canvas(self, bd=0, highlightthickness=0,
                           xscrollcommand = hscrollbar.set,
                           yscrollcommand = vscrollbar.set)
          
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        vscrollbar.config(command=canvas.yview)
        hscrollbar.config(command=canvas.xview) 
 
        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)
  
        # create a frame inside the canvas which will be scrolled with it
        self.interior = ttk.Frame(canvas)        
        self.interior.pack(fill = tk.BOTH, expand = tk.TRUE)
        
        interior_id = canvas.create_window(0, 0, window=self.interior,
                                           anchor=tk.NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (self.interior.winfo_reqwidth(), self.interior.winfo_reqheight())
               
            canvas.config(scrollregion="0 0 %s %s" % size)
            if self.interior.winfo_reqwidth() > canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=self.interior.winfo_reqwidth())
            else:
                canvas.config(width=canvas.winfo_width())
            if self.interior.winfo_reqheight() > canvas.winfo_height():
                # update the canvas's heigth to fit the inner frame
                canvas.config(height=self.interior.winfo_reqheight())
            else:
                canvas.config(height=canvas.winfo_height())
        self.interior.bind('<Configure>', _configure_interior)
   
        def _configure_canvas(event):
            if self.interior.winfo_reqwidth() > canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=self.interior.winfo_reqwidth())
            else:
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
            if self.interior.winfo_reqheight() > canvas.winfo_height():
                # update the inner frame's height to fill the canvas
                canvas.itemconfigure(interior_id, height=self.interior.winfo_reqheight())
            else:
                canvas.itemconfigure(interior_id, height=canvas.winfo_height()) 
        canvas.bind('<Configure>', _configure_canvas)

if __name__ == "__main__":

    class SampleApp(tk.Tk):
        def __init__(self, *args, **kwargs):
            root = tk.Tk.__init__(self, *args, **kwargs)

            self.frame = ScrolledFrame(root)
            self.frame.pack(fill = tk.BOTH, expand = True)
            self.label = ttk.Label(text="Shrink the window to activate the scrollbar.")
            self.label.pack()
            buttons = []
            for i in range(30):
                buttons.append(ttk.Button(self.frame.interior, text="Button " + str(i)))
                buttons[-1].grid(row = i, column =i)

    app = SampleApp()
    app.geometry('600x500+200+200')
    app.mainloop()