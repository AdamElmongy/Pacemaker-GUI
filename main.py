from tkinter import *
import json

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
 
def save(variable, value):
    variable = value

with open('users.json') as file:
    users = json.load(file)
    print(users)


def login(ID, password):
    for user in users:
        if ID == user[0] and password == user[1]:
            return True
    
    return False

def register(ID, password):    
    if len(users) == 10:
        return "No more users can be registered"
    else:
        for user in users:
            if user[0] == ID:
                return "This user already exists"
    
        users.append([ID, password])
        with open('users.json', 'w') as file:
            json.dump(users, file)
    return True


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