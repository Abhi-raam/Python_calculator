from tkinter import *

window=Tk()
window.title("Calculator")
window.geometry("350x600+100+200")
window.resizable(False,False)
window.configure(bg="#1F1919")

equation=""
def display(value):
    global equation
    equation=str(equation)+str(value)
    label_result.config(text=equation)

def clear():
    global equation
    equation=""
    label_result.config(text=equation)


def persent():
    global equation
    equation=float(equation)/100
    label_result.config(text=equation)
    
def delet():
    global equation
    equation=str(equation)[:-1]
    label_result.config(text=equation)

def equal():
    global equation
    result=""
    if equation!="":
        try:
            result=eval(equation)
            equation=result
        except:
            result="Error"
            equation=""
    label_result.config(text=result)


label_result=Label(window,width=25,height=2,text="",bg="#F4E6E6",font=("arial",30),anchor=E)
label_result.pack()


button_clr=Button(window,text="Clr",width=7,height=3,font=("arial",10,"bold"),bd=3,bg="#F8F8F8",command=lambda:clear()).place(x=10,y=100)
button_del=Button(window,text="Del",width=7,height=3,font=("arial",10,"bold"),bd=3,bg="#F8F8F8",command=lambda:delet()).place(x=90,y=100)
button_present=Button(window,text="%",width=7,height=3,font=("arial",10,"bold"),bd=3,bg="#F8F8F8",command=lambda:persent()).place(x=170,y=100)
button_div=Button(window,text="/",width=7,height=3,font=("arial",10,"bold"),bd=3,bg="#F8F8F8",command=lambda:display("/")).place(x=250,y=100)

button_7=Button(window,text="7",width=7,height=3,font=("arial",10,"bold"),bd=3,bg="#F8F8F8",command=lambda:display("7")).place(x=10,y=200)
button_8=Button(window,text="8",width=7,height=3,font=("arial",10,"bold"),bd=3,bg="#F8F8F8",command=lambda:display("8")).place(x=90,y=200)
button_9=Button(window,text="9",width=7,height=3,font=("arial",10,"bold"),bd=3,bg="#F8F8F8",command=lambda:display("9")).place(x=170,y=200)
button_mult=Button(window,text="x",width=7,height=3,font=("arial",10,"bold"),bd=3,bg="#F8F8F8",command=lambda:display("*")).place(x=250,y=200)

button_4=Button(window,text="4",width=7,height=3,font=("arial",10,"bold"),bd=3,bg="#F8F8F8",command=lambda:display("4")).place(x=10,y=300)
button_5=Button(window,text="5",width=7,height=3,font=("arial",10,"bold"),bd=3,bg="#F8F8F8",command=lambda:display("5")).place(x=90,y=300)
button_6=Button(window,text="6",width=7,height=3,font=("arial",10,"bold"),bd=3,bg="#F8F8F8",command=lambda:display("6")).place(x=170,y=300)
button_sub=Button(window,text="-",width=7,height=3,font=("arial",10,"bold"),bd=3,bg="#F8F8F8",command=lambda:display("-")).place(x=250,y=300)

button_1=Button(window,text="1",width=7,height=3,font=("arial",10,"bold"),bd=3,bg="#F8F8F8",command=lambda:display("1")).place(x=10,y=400)
button_2=Button(window,text="2",width=7,height=3,font=("arial",10,"bold"),bd=3,bg="#F8F8F8",command=lambda:display("2")).place(x=90,y=400)
button_3=Button(window,text="3",width=7,height=3,font=("arial",10,"bold"),bd=3,bg="#F8F8F8",command=lambda:display("3")).place(x=170,y=400)
button_add=Button(window,text="+",width=7,height=3,font=("arial",10,"bold"),bd=3,bg="#F8F8F8",command=lambda:display("+")).place(x=250,y=400)

button_0=Button(window,text="0",width=7,height=3,font=("arial",10,"bold"),bd=3,bg="#F8F8F8",command=lambda:display("0")).place(x=10,y=500)
button_dot=Button(window,text=".",width=7,height=3,font=("arial",10,"bold"),bd=3,bg="#F8F8F8",command=lambda:display(".")).place(x=90,y=500)
button_equal=Button(window,text="=",width=17,height=3,font=("arial",10,"bold"),bd=3,bg="#F8F8F8",command=lambda:equal()).place(x=170,y=500)
