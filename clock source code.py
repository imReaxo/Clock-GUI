from tkinter import * 
from tkinter.ttk import *
from time import strftime


root = Tk()
root.title('Clock')

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)

lbl = Label(root, font = ('calibri', 40, 'bold'),
            background = 'white',
            foreground = 'black')
  

lbl.pack(anchor = 'center')
time()
  
mainloop()