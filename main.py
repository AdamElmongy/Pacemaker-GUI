from tkinter import *
from utils.Navigation import navigator

def Welcome():
    # Make root window
    root = Tk()
    # root window title and dimension
    root.title("Welcome to Test")
    # getting screen width and height of display
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    # setting tkinter window size
    root.geometry("%dx%d" % (width, height))
    root.configure(bg='#FFFFFF')
    navigator.main_app = root
    # Make the frame and set it to current frame
    welcome = Frame(root, bg='#000000')
    welcome.pack(fill='both', expand=True)
    navigator.current_frame = welcome

    welcome_label = Label(welcome, text="Welcome to the Pacemaker", font=("Arial", 25), bg='#000000', fg='#FFFFFF')
    welcome_label.place(relx=.5, rely=.5, anchor="center")

    # After 5000 milliseconds (5 seconds), switch to the login/register page
    welcome.after(5000, lambda: navigator.navigate_to_page("SignIn"))  # (welcome.pack_forget(), signin()))

    # Execute Tkinter
    root.mainloop()


navigator.register_page("Welcome", Welcome)
Welcome()




