import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from MainMenu import main_menu
from utils.functions import openFile, writeToFile, setCurrentUser
from utils.Navigation import navigator


user_default_values = {
    "AAI": {
        "LRL": 60,
        "URL": 120,
        "AAmp": 3.5,
        "APW": 0.4,
        "ARP": 250
    },
    "AOO": {
        "LRL": 60,
        "URL": 120,
        "AAmp": 3.5,
        "APW": 0.4,
    }, 
    "VOO": {
        "LRL": 60,
        "URL": 120,
        "VAmp": 3.5,
        "VPW": 0.4,
    },
    "VVI": {
        "LRL": 60,
        "URL": 120,
        "VAmp": 3.5,
        "VPW": 0.4,
        "VRP": 250
    }
}

def signin(tab=None):

    def login():
        ID = login_username_entry.get()
        password = login_password_entry.get()
        users = openFile('data/users')
        for user in users:
            if ID == user[0] and password == user[1]:
                setCurrentUser(ID)
                navigator.navigate_to_page("Menu")
                return
        messagebox.showerror("Error", "Invalid username or password")

    def register():
        ID = register_username_entry.get()
        password = register_password_entry.get()
        users = openFile('data/users')
        print(users)
        if len(users) >= 10:
            messagebox.showerror("Error", "No more users can be registered")
            return
        else:
            for user in users:
                if user[0] == ID:
                    messagebox.showerror("Error", "A user with this username already exists")
                    return
            users.append([ID, password])

            user_file_data = {
                "username": ID,
                "mode-values": user_default_values
            }
            writeToFile('data/users', users)  # Assuming writeToFile function writes the data to a file
            writeToFile(f'Users/{ID}', user_file_data)
            setCurrentUser(ID)
            navigator.navigate_to_page("Menu")

    # Function for switching to the Main Menu page
    # def show_main_menu():
    #     # Hide the login and register tabs
    #     signin.pack_forget()
    #     # Call the main_menu function to populate the frame
    #     main_menu()

    signin = tk.Frame(navigator.main_app, bg='#000000')
    navigator.current_frame = signin
    # signin.title("Login/Register Form")
    # signin.geometry("500x500")

    # Create a Notebook (tabbed interface) for login and register
    notebook = ttk.Notebook(signin)
    notebook.pack(fill='both', expand=True)

   # Frame for Login tab
    login_frame = ttk.Frame(notebook)
    notebook.add(login_frame, text='Login')

    # Login Tab
    login_username_label = tk.Label(login_frame, text="Username:")
    login_username_label.pack(anchor='center', padx=10)
    login_username_entry = tk.Entry(login_frame)
    login_username_entry.pack(anchor='center', padx=10)

    login_password_label = tk.Label(login_frame, text="Password:")
    login_password_label.pack(anchor='center', padx=10)
    login_password_entry = tk.Entry(login_frame, show="*")
    login_password_entry.pack(anchor='center', padx=10)

    login_button = tk.Button(login_frame, text="Login", command=login)
    login_button.pack(anchor='center', padx=10)

    # Frame for Register tab
    register_frame = ttk.Frame(notebook)
    notebook.add(register_frame, text='Register')

    # Register Tab
    register_username_label = tk.Label(register_frame, text="Username:")
    register_username_label.pack(anchor='center', padx=10)
    register_username_entry = tk.Entry(register_frame)
    register_username_entry.pack(anchor='center', padx=10)

    register_password_label = tk.Label(register_frame, text="Password:")
    register_password_label.pack(anchor='center', padx=10)
    register_password_entry = tk.Entry(register_frame, show="*")
    register_password_entry.pack(anchor='center', padx=10)

    register_button = tk.Button(register_frame, text="Register", command=register)
    register_button.pack(anchor='center', padx=10)


    # Run the Tkinter main loop
    notebook.select(register_frame) if tab == "Register" else notebook.select(login_frame)
    signin.pack(fill='both', expand=True)

navigator.register_page("SignIn", signin)




