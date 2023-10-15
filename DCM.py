import tkinter as tk
from tkinter import ttk
from utils.Navigation import navigator
from tkinter import messagebox
from utils.functions import openFile, writeToFile, setCurrentUser
from Modes import Modes
from MenuBar import MenuBar
from SetMode import SetMode


class DCM:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome to Test")
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry("%dx%d" % (self.width, self.height))
        self.root.configure(bg='#FFFFFF')

        navigator.main_app = self.root
        navigator.current_frame = self.root

        navigator.register_page("Welcome", self.__welcome)
        navigator.register_page("SignIn", self.__signin)
        navigator.register_page("MainMenu", self.__mainmenu)

        self.user_default_values = {
            "AAI": {"LRL": 60, "URL": 120, "AAmp": 3.5, "APW": 0.4, "ARP": 250},
            "AOO": {"LRL": 60, "URL": 120, "AAmp": 3.5, "APW": 0.4},
            "VOO": {"LRL": 60, "URL": 120, "VAmp": 3.5, "VPW": 0.4},
            "VVI": {"LRL": 60, "URL": 120, "VAmp": 3.5, "VPW": 0.4, "VRP": 320}
        }

        self.__welcome()

    def __welcome(self):
        welcome = tk.Frame(self.root, bg='#000000')
        welcome.pack(fill='both', expand=True)
        navigator.current_frame = welcome

        welcome_label = tk.Label(welcome, text="Welcome to the Pacemaker", font=("Arial", 25), bg='#000000',
                                 fg='#FFFFFF')
        welcome_label.place(relx=.5, rely=.5, anchor="center")

        # After 5000 milliseconds (5 seconds), switch to the login/register page
        welcome.after(5000, lambda: navigator.navigate_to_page("SignIn"))

    def __signin(self, tab=None):
        signin = tk.Frame(navigator.main_app, bg='#000000')
        navigator.current_frame = signin

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

        login_button = tk.Button(login_frame, text="Login",
                                 command=lambda:
                                 self.__login(login_username_entry, login_password_entry))
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

        register_button = tk.Button(register_frame, text="Register",
                                    command=lambda:
                                    self.__register(register_username_entry, register_password_entry))
        register_button.pack(anchor='center', padx=10)

        # Run the Tkinter main loop
        notebook.select(register_frame) if tab == "Register" else notebook.select(login_frame)
        signin.pack(fill='both', expand=True)

    def __login(self, username, password):
        ID = username.get()
        key = password.get()
        users = openFile('data/users')
        for user in users:
            if ID == user[0] and key == user[1]:
                setCurrentUser(ID)
                navigator.navigate_to_page("MainMenu")
                return
        messagebox.showerror("Error", "Invalid username or password")

    def __register(self, username, password):
        ID = username.get()
        key = password.get()
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
            users.append([ID, key])

            user_file_data = {
                "username": ID,
                "mode-values": self.user_default_values
            }
            writeToFile('data/users', users)  # Assuming writeToFile function writes the data to a file
            writeToFile(f'Users/{ID}', user_file_data)
            setCurrentUser(ID)
            navigator.navigate_to_page("MainMenu")

    def __mainmenu(self):
        menu = tk.Frame(navigator.main_app)
        menu.pack(side='top', fill='both', expand=True)
        navigator.current_frame = menu

        # Create a menu bar at the top as a frame
        menu_bar = tk.Frame(menu)
        MenuBar(menu_bar)

        # Create a frame for the modes
        modes_frame = tk.Frame(menu)
        Modes(modes_frame)

        # New Patient button to return to login page
        newpatient_btn = tk.Button(menu, text="New Patient- return to Login",
                                   command=lambda:
                                   navigator.navigate_to_signin("MainMenu", "Register"))

        # Create frame for Set Mode
        set_mode_frame = tk.Frame(menu)
        SetMode(set_mode_frame)

        # Pack frames and buttons to the screen
        menu_bar.pack(pady=5, fill="x")
        modes_frame.pack(pady=10, padx=10, fill="both")
        set_mode_frame.pack(pady=10)
        newpatient_btn.pack(pady=10)


window = tk.Tk()
DCM(window)
window.mainloop()
