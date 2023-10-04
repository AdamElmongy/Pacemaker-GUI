from tkinter import *

# create root window
root = Tk()
 
# root window title and dimension
root.title("Welcome to Test")
#getting screen width and height of display
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
#setting tkinter window size
root.geometry("%dx%d" % (width, height))
# root.configure(background='black')
 


welcome_label = Label(root, text = "Welcome to the Pacemaker", font=("Arial", 25))
welcome_label.place(relx=.5, rely=.5, anchor="center")
# button widget with red color text
# inside
# btn = Button(root, text = "Click me" ,
#              fg = "red", command=clicked)
# # set Button grid
# btn.grid(column=2, row=2)
# btn.place(x=50, y=100)
# Execute Tkinter
root.mainloop()

