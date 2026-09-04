from tkinter import *
import random
colours=["plum", "thistle", "orchid", "lavender", "violet", "chartreuse", "yellowgreen", "springgreen", "mediumspringgreen", "seagreen", "olivedrab", "darkolivegreen", "salmon", "coral", "tomato", "goldenrod", "burlywood", "tan", "chocolate", "sienna", "steelblue", "cornflowerblue", "cadetblue", "powderblue", "turquoise", "aquamarine", "hotpink", "deeppink", "lightpink", "palevioletred", "mediumvioletred", "lightgoldenrod", "palegoldenrod", "lemonchiffon", "moccasin", "peachpuff", "gainsboro", "slategray", "lightslategray", "dimgray", "lavenderblush", "mistyrose", "antiquewhite", "navajowhite", "blanchedalmond", "bisque", "wheat", "rosybrown", "sandybrown", "peru", "mediumorchid", "darkorchid", "darkmagenta", "mediumpurple", "blueviolet", "darkviolet", "indigo"]

def change_colour():
    colour=random.choice(colours)
    root.config(bg=colour)
    
root=Tk()
label=Label(root,text="Want to change colour?", font=("Bold",24))
label.pack()
button=Button(root,text="Click me",command=change_colour)
button.pack()
root.mainloop()


