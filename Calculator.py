from tkinter import *

def add():
    res=float(e1.get())+float(e2.get())
    res=round(res,4)
    lbl3.config(text=res)



def sub():
    res=float(e1.get())-float(e2.get())
    res=round(res,4)
    lbl3.config(text=res)

    
def mul():
    res=float(e1.get())*float(e2.get())
    res=round(res,4)
    lbl3.config(text=res)

    
def div():
    res=float(e1.get())/float(e2.get())
    res=round(res,4)
    lbl3.config(text=res)
    



window=Tk()
lbl1=Label(window,text="Enter NO1:")
lbl2=Label(window,text="Enter NO2:")
lbl1.grid(row=0,column=0)
lbl2.grid(row=1,column=0)

lbl3=Label(window,text="")
lbl3.grid(row=2,column=0)

e1=Entry(window)
e2=Entry(window)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

btn1=Button(window,text="Add",command=add)
btn2=Button(window,text="Sub",command=sub)
btn3=Button(window,text="Mul",command=mul)
btn4=Button(window,text="Div",command=div)

btn1.grid(row=0,column=2)
btn2.grid(row=0,column=3)
btn3.grid(row=1,column=2)
btn4.grid(row=1,column=3)

window.mainloop()

