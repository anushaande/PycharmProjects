from tkinter import *
from playgroung import *

window = Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# label
my_label = Label(text=f"This is the label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

# Input

input = Entry(width=10)
input.grid(column=3, row=1)


# button

def on_button_click1():
    value = input.get()
    # my_label["text"] = "Button is clicked"
    # or
    my_label.config(text=value)


button1 = Button(text="Click Me", command=on_button_click1)
button1.grid(column=2, row=0)

button2 = Button(text="New Button", command=on_button_click)
button2.grid(column=1, row=1)

window.mainloop()
