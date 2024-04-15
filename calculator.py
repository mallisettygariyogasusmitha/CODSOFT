from tkinter import *
root=Tk()
root.title("Calculator")
e=Entry(root,width=30,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=15,pady=10)
def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
def button_clear():
    e.delete(0,END)
def button_add():
    first_number=e.get()
    global fnum
    global math
    math="addition"
    fnum=int(first_number)
    e.delete(0,END)
def button_sub():
    first_number=e.get()
    global fnum
    global math
    math="subtraction"
    fnum=int(first_number)
    e.delete(0,END)
def button_mul():
    first_number=e.get()
    global fnum
    global math
    math="multiply"
    fnum=int(first_number)
    e.delete(0,END)
def button_div():
    first_number=e.get()
    global fnum
    global math
    math="division"
    fnum=int(first_number)
    e.delete(0,END)
def button_equal():
    second_number=e.get()
    e.delete(0,END)
    if(math=="addition"):
       e.insert(0,fnum+int(second_number))
    if(math=="subtraction"):
       e.insert(0,fnum-int(second_number))
    if(math=="multiply"):
       e.insert(0,fnum*int(second_number))
    if(math=="division"):
       e.insert(0,fnum/int(second_number))
myButton_1=Button(root,text="1",padx=40,pady=20,command=lambda:button_click(1),bg="black",fg="white")
myButton_2=Button(root,text="2",padx=40,pady=20,command=lambda:button_click(2),bg="black",fg="white")
myButton_3=Button(root,text="3",padx=40,pady=20,command=lambda:button_click(3),bg="black",fg="white")
myButton_4=Button(root,text="4",padx=40,pady=20,command=lambda:button_click(4),bg="black",fg="white")
myButton_5=Button(root,text="5",padx=40,pady=20,command=lambda:button_click(5),bg="black",fg="white")
myButton_6=Button(root,text="6",padx=40,pady=20,command=lambda:button_click(6),bg="black",fg="white")
myButton_7=Button(root,text="7",padx=40,pady=20,command=lambda:button_click(7),bg="black",fg="white")
myButton_8=Button(root,text="8",padx=40,pady=20,command=lambda:button_click(8),bg="black",fg="white")
myButton_9=Button(root,text="9",padx=40,pady=20,command=lambda:button_click(9),bg="black",fg="white")
myButton_0=Button(root,text="0",padx=40,pady=20,command=lambda:button_click(),bg="black",fg="white")
myButton_add=Button(root,text="+",padx=39,pady=20, command=button_add,bg="red",fg="white")
myButton_equal=Button(root,text="=",padx=91,pady=20, command=button_equal,bg="red",fg="white")
myButton_clear=Button(root,text="Clear",padx=80,pady=20, command=button_clear,bg="red",fg="white")
myButton_sub=Button(root,text="-",padx=41,pady=20, command=button_sub,bg="red",fg="white")
myButton_mul=Button(root,text="*",padx=41,pady=20, command=button_mul,bg="red",fg="white")
myButton_div=Button(root,text="/",padx=41,pady=20, command=button_div,bg="red",fg="white")
myButton_1.grid(row=1,column=0)
myButton_2.grid(row=1,column=1)
myButton_3.grid(row=1,column=2)
myButton_4.grid(row=2,column=0)
myButton_5.grid(row=2,column=1)
myButton_6.grid(row=2,column=2)
myButton_7.grid(row=3,column=0)
myButton_8.grid(row=3,column=1)
myButton_9.grid(row=3,column=2)
myButton_0.grid(row=4,column=0)
myButton_add.grid(row=5,column=0)
myButton_clear.grid(row=4,column=1,columnspan=2)
myButton_equal.grid(row=5,column=1,columnspan=2)
myButton_sub.grid(row=6,column=1)
myButton_mul.grid(row=6,column=2)
myButton_div.grid(row=6,column=0)
root.mainloop()
