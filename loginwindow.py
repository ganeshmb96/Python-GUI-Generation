from tkinter import *

root=Tk()
label1=Label(root,text="Name")
label2=Label(root,text="Password")
entry1=Entry(root)
entry2=Entry(root)

label1.grid(row=0,sticky=E)
label2.grid(row=1,sticky=E)
entry1.grid(row=0,column=1,ipadx=10)
entry2.grid(row=1,column=1,ipadx=10)

c=Checkbutton(root,text="keep me logged in")
c.grid(columnspan=2)
root.mainloop()
