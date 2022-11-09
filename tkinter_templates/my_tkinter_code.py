from tkinter import *
from playgroung import *

window = Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)

# label
my_label = Label(text=f"Sum is the result", font=("Arial", 24, "bold"))
my_label.pack()

# Input

input1 = Entry(width=10)
input1.pack()

input2 = Entry(width=12)
input2.pack()

# button

def on_button_click1():
    value1 = input1.get()
    value2 = input2.get()
    result = add(int(value1), int(value2))
    my_label["text"] = f"Sum is {result}"
    # or
    # my_label.config(text=f"Sum is {result}")


button = Button(text="Click Me", command=on_button_click1)
button.pack()

window.mainloop()
