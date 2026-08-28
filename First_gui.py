from tkinter import *
def display():
    my_window=Tk()
    my_window.geometry("420x420")
    my_window.title("First tkinter gui")
    my_window.config(background="#7de1f5")
    my_label=Label(my_window, text="My first tkinter gui" , font=("Courier  New",22,"bold"),bg="#7de1f5",fg="#e66aeb")
    my_label.place(x=0,y=0)
    my_window.mainloop()
    
learning_tkinter=True
if learning_tkinter:
    display() 
