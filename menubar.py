from tkinter import *
# tkinter is a graphical library of python

window = Tk()
# creating the app window

window.geometry("800x600")
# the width and height of the window

window.title("First Tkinter App")
# title of the window

# give colour to the window
window.config(background = "green")

menubar = Menu(window)

# creates a menu in the window
window.config(menu = menubar)

# creates file menu
file_menu = Menu(menubar, tearoff = 0)

# adds sections into it
menubar.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "Edit", command= None)
file_menu.add_command(label = "Undo", command= None)
file_menu.add_command(label = "Redo", command= None)

window.mainloop()