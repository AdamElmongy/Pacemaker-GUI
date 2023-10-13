from tkinter import *
from Login import signin
from Navigation import navigator

def Welcome():
    # Function to switch to the login/register page
    # def switch_to_login_page():
    #     welcome.pack_forget()
    #     signin()

    # create root window
    root = Tk()
    navigator.main_app = root
    welcome = Frame(root)

    # root window title and dimension
    root.title("Welcome to Test")
    # getting screen width and height of display
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    # setting tkinter window size
    root.geometry("%dx%d" % (width, height))

    welcome_label = Label(welcome, text="Welcome to the Pacemaker", font=("Arial", 25))
    welcome_label.pack(expand=True)
    welcome_label.place(relx=.5, rely=.5, anchor="center")

    # After 5000 milliseconds (5 seconds), switch to the login/register page
    welcome.after(1000, lambda: (welcome.pack_forget(), signin()))

    # Execute Tkinter
    welcome.pack(fill='both', expand=True)
    root.mainloop()



navigator.register_page("Welcome", Welcome)

if __name__ == "__main__":
    Welcome()

# button widget with red color text
# inside
# btn = Button(root, text = "Click me" ,
#              fg = "red", command=clicked)
# # set Button grid
# btn.grid(column=2, row=2)
# btn.place(x=50, y=100)
# Execute Tkinter


