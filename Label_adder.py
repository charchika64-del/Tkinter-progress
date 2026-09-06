from tkinter import *

class my_window(Tk):
    
    def __init__(self):
        super().__init__()
        self.label=Label(self,text="Date-6 Sep 2026 (sun)")
        self.label.pack()
 
def greet():
    label=Label(root,text="Welcome User!") 
    label.pack() 
    label1=Label(root,text="How are you? ")    
    label1.pack()
    
root=my_window()
button=Button(root,text="Click me",command=greet)
button.pack()
root.mainloop()
        
        
   
