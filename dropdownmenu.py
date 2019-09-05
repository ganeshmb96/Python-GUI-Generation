from tkinter import *

def donothing():
    print("hello")

def trythis():
    print("hey")

def exits():
    exit(0)
root = Tk()
menu = Menu(root)
root.config(menu=menu)

submenu = Menu(menu)
menu.add_cascade(label="FILE",menu=submenu)
submenu.add_command(label="NEW",command=donothing)
submenu.add_command(label="OPEN",command=trythis)
submenu.add_separator()
submenu.add_command(label="EXIT",command=exits)

editmenu = Menu(menu)
menu.add_cascade(label="EDIT",menu=editmenu)
editmenu.add_command(label="REDO",command=exits)
root.mainloop()
