# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def show_data():
    txtName= ent.get()
    gender= var_chk.get()
    print(txtName, gender)
    
    
    


from tkinter import *


root =Tk()
root.geometry("300x300")
l1=Label(root, text="Name:")
l2=Label(root,text="Gender:")
ent= Entry(root)
var_chk=IntVar()
rd1= Radiobutton(root, text="Male",variable=var_chk,value=1)
rd2=Radiobutton(root,text="Female",variable=var_chk,value=2)
l1.grid(row=0)
l2.grid(row=1)
ent.grid(row=0, column=1)

rd1.grid(row=1, column=1, sticky=W)
rd2.grid(row=1, column=1 , sticky= E)

btn=Button(root,text="Register",bg="purple", fg="white", command=show_data)
btn.grid(row=2 , columnspan=2)

txt=Text(root, width=25, height =10, wrap =WORD)
txt.grid(row=3, columnspan=2 ,padx=10, pady=10, sticky=W)

root.mainloop()






