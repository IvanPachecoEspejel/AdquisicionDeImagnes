'''
Created on 23/08/2015

@author: ivan
'''

from Tkinter import *

from Vistas.Principal import Principal

root = Tk()
app = Principal(master=root)
root.after(30000, lambda: root.destroy())
app.mainloop()
