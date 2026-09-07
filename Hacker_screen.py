# please dont take the name seriously and do not think that i am hacker.
# I am just making a gui with 0s and and 1s on a dark screen 
from tkinter import *

window = Tk()
window.config(bg="#212120")

# 1. Create one long row of random-looking code
row_of_code = "1 1 0 1 0 1 1 0 1 0 0 1 0 1 1 0 0 1 0 1"

# 2. Loop to stack multiple rows cleanly down the screen
for num in range(15):
    Label(window, text=row_of_code, bg="#212120", fg="#138a0b", font=("courier", 16)).pack()

window.mainloop()

