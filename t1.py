#Create a window with a "click me" buttton.when we press the button  so on the label print "Hello eklavya".
from tkinter import*
win=Tk()
win.geometry("900x500")
def python():
    lb.config(text="Hello Eklavya")


btn=Button(win,text="Click me",font=("Times New Roman",30,"bold"),command=python,bg="yellow")
btn.place(x=200,y=200,height=200,width=200)


lb=Label(win,text="",font=("Times New Roman",30,"bold"))
lb.place(x=500,y=100,height=500,width=500)


win.mainloop()