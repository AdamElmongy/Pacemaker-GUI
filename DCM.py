import os
import tkinter as tk
from tkinter import ttk
from time import sleep
from utils.Navigation import navigator
from tkinter import messagebox
from utils.functions import openFile, writeToFile, setCurrentUser, getCurrentUser
from utils.PacemakerDetector import check_usb_device
from tkintergraph import EGRAM
# from temporary_graph import live_graph
from Modes import Modes
from MenuBar import MenuBar
from SetMode import SetMode


class DCM:
    def __init__(self, root):
        self.__root = root
        self.__root.title("Welcome to Test")
        width = self.__root.winfo_screenwidth()
        height = self.__root.winfo_screenheight()
        self.__root.geometry("%dx%d" % (width, height))
        self.__root.configure(bg='#FFFFFF')
        self.delete_popup = None
        self.egram_popup = None
        self.__confirm_egram_popup_open = False
        self.__confirm_deletion_popup_open = False

        navigator.set_main_app(self.__root)
        navigator.set_current_frame(self.__root)

        navigator.register_page("Welcome", self.welcome)
        navigator.register_page("SignIn", self.signin)
        navigator.register_page("MainMenu", self.mainmenu)
        navigator.register_page("Connect", self.connect)

        self.__user_default_values = {
            "AAI": {"LRL": 60, "URL": 120, "AAmp": 3.5, "APW": 0.4, "ARP": 250},
            "AOO": {"LRL": 60, "URL": 120, "AAmp": 3.5, "APW": 0.4},
            "VOO": {"LRL": 60, "URL": 120, "VAmp": 3.5, "VPW": 0.4},
            "VVI": {"LRL": 60, "URL": 120, "VAmp": 3.5, "VPW": 0.4, "VRP": 320},
            "AAIR": {"LRL": 60, "URL": 120, "AAmp": 3.5, "APW": 0.4, "ARP": 250,
                     "Reaction Time": 30, "Response Factor": 8, "Recovery Time": 5, "MSR": 120},
            "AOOR": {"LRL": 60, "URL": 120, "AAmp": 3.5, "APW": 0.4,
                     "Reaction Time": 30, "Response Factor": 8, "Recovery Time": 5, "MSR": 120},
            "VOOR": {"LRL": 60, "URL": 120, "VAmp": 3.5, "VPW": 0.4,
                     "Reaction Time": 30, "Response Factor": 8, "Recovery Time": 5, "MSR": 120},
            "VVIR": {"LRL": 60, "URL": 120, "VAmp": 3.5, "VPW": 0.4, "VRP": 320,
                     "Reaction Time": 30, "Response Factor": 8, "Recovery Time": 5, "MSR": 120},
        }

        self.welcome()

    def welcome(self):
        welcome = tk.Frame(self.__root, bg='#000000')
        welcome.pack(fill='both', expand=True)
        navigator.set_current_frame(welcome)

        welcome_label = tk.Label(welcome, text="Welcome to the Pacemaker", font=("Arial", 25), bg='#000000',
                                 fg='#FFFFFF')
        welcome_label.place(relx=.5, rely=.5, anchor="center")

        # After 5000 milliseconds (5 seconds), switch to the login/register page
        welcome.after(500, lambda: navigator.navigate_to_page("SignIn"))

    def center_content(self, frame):
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(2, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(2, weight=1)

    def signin(self, tab=None):
        user_count = len(openFile('data/users'))
        signin = tk.Frame(navigator.get_main_app(), bg='#000000')
        navigator.set_current_frame(signin)
        default_font = ("Helvetica", 13)

        # Create a Notebook (tabbed interface) for login and register
        notebook = ttk.Notebook(signin)
        notebook.pack(fill='both', expand=True)

        # Frame for Login tab
        login_frame = ttk.Frame(notebook)
        notebook.add(login_frame, text='Login')

        # Login Tab
        login_username_label = tk.Label(login_frame, text="Username:", font=default_font)
        login_username_label.pack(anchor='center', padx=10, pady=(300, 0))
        login_username_entry = tk.Entry(login_frame, font=default_font)
        login_username_entry.pack(anchor='center', padx=10)

        login_password_label = tk.Label(login_frame, text="Password:", font=default_font)
        login_password_label.pack(anchor='center', padx=10)
        login_password_entry = tk.Entry(login_frame, show="*", font=default_font)
        login_password_entry.pack(anchor='center', padx=10)

        login_button = tk.Button(login_frame, text="Login", padx=10, font=default_font,
                                 command=lambda:
                                 self.login(login_username_entry, login_password_entry))
        login_button.pack(anchor='center', padx=10, pady=10)
        user_count_login_label = tk.Label(login_frame, text=f"Current number of registered users: {user_count}", font=default_font)
        user_count_login_label.pack(anchor='center', padx=10, pady=10)

        # Frame for Register tab
        register_frame = ttk.Frame(notebook)
        notebook.add(register_frame, text='Register')

        # Register Tab
        register_username_label = tk.Label(register_frame, text="Username:", font=default_font)
        register_username_label.pack(anchor='center', padx=10, pady=(300, 0))
        register_username_entry = tk.Entry(register_frame, font=default_font)
        register_username_entry.pack(anchor='center', padx=10)

        register_password_label = tk.Label(register_frame, text="Password:", font=default_font)
        register_password_label.pack(anchor='center', padx=10)
        register_password_entry = tk.Entry(register_frame, show="*", font=default_font)
        register_password_entry.pack(anchor='center', padx=10)

        register_button = tk.Button(register_frame, text="Register", font=default_font,
                                    command=lambda:
                                    self.register(register_username_entry, register_password_entry))
        register_button.pack(anchor='center', padx=10, pady=10)
        print(user_count)
        user_count_register_label = tk.Label(register_frame, text=f"Current number of registered users: {user_count}", font=default_font)
        user_count_register_label.pack(anchor='center', padx=10, pady=10)

        # Run the Tkinter main loop
        notebook.select(register_frame) if tab == "Register" else notebook.select(login_frame)
        signin.pack(side='top', fill='both', expand=True)

    def connect(self):

        connect_frame = tk.Frame(navigator.get_main_app())
        navigator.set_current_frame(connect_frame)

        connect_button = tk.Button(connect_frame, text="Connected", command=self.connect_pacemaker, font=("Helvetica", 25))
        connect_button.pack(side='top', pady=(350, 20))

        label = tk.Label(connect_frame, text="Please connect a pacemaker, then press the button to continue.", font=("Helvetica", 12))
        label.pack(side='top', pady=10)

        connect_frame.pack(side='top', fill='both', expand=True)

    def connect_pacemaker(self):
        if check_usb_device():
            navigator.navigate_to_page("MainMenu")
        else:
            messagebox.showerror("Error", "No pacemaker detected. Please connect a pacemaker to continue.")

    def check_pacemaker_connection(self):
        if check_usb_device():
            self.check_pacemaker_connection()
        else:
            messagebox.showerror("Error", "Pacemaker has been disconnected, please reconnect the pacemaker to continue.")
            navigator.navigate_to_page("SignIn")

    def login(self, username, password):
        ID = username.get()
        key = password.get()
        users = openFile('data/users')
        for user in users:
            if ID == user[0] and key == user[1]:
                setCurrentUser(ID)
                navigator.navigate_to_page("MainMenu")
                return
        messagebox.showerror("Error", "Invalid username or password")


    def register(self, username, password):
        ID = username.get()
        key = password.get()
        users = openFile('data/users')
        print(users)
        if len(users) >= 10:
            messagebox.showerror("Error", "No more users can be registered")
            return
        else:
            if ID == "" or password == "":
                messagebox.showerror("Error", "User and Password string cannot be empty")
                return
            for user in users:
                if user[0] == ID:
                    messagebox.showerror("Error", "A user with this username already exists")
                    return
            users.append([ID, key])

            user_file_data = {
                "username": ID,
                "mode-values": self.__user_default_values
            }
            writeToFile('data/users', users)  # Assuming writeToFile function writes the data to a file
            writeToFile(f'Users/{ID}', user_file_data)
            setCurrentUser(ID)
            navigator.navigate_to_page("Connect")

    def delete_user(self, userID):
        users_path = os.path.join(os.getcwd(), "Users")
        users = openFile('data/users')
        for user in users:
            if user[0] == userID:
                print(user)
                users.remove(user)
                writeToFile('data/users', users)
                break
        os.remove(f'{users_path}/{userID}.json')
        self.close_confirm_delete_popup()
        navigator.navigate_to_signin("MainMenu")
        return

    def confirm_deletion_popup(self):
        if self.__confirm_deletion_popup_open:
            return

        self.__confirm_deletion_popup_open = True
        self.delete_popup = tk.Toplevel()
        self.delete_popup.geometry("260x180")
        self.delete_popup.title("Confirm Deletion")

        warning_lbl = tk.Label(self.delete_popup, text="Warning: Are you sure you'd like to \n delete your account?")
        warning_lbl.grid(row=0, column=0, columnspan=4, padx=20, pady=20, sticky='w')

        button_font = ('Arial', 14)  # Font for the buttons

        def on_enter(event):
            event.widget.config(bg='lightblue')

        # Function to change button color back to default
        def on_leave(event):
            event.widget.config(bg='SystemButtonFace')

        yes_button = tk.Button(self.delete_popup, text="Yes", font=button_font,
                               command=lambda: self.delete_user(getCurrentUser()))
        yes_button.grid(row=1, column=1, pady=10)
        yes_button.bind('<Enter>', on_enter)
        yes_button.bind('<Leave>', on_leave)

        no_button = tk.Button(self.delete_popup, text="No", font=button_font,
                              command=self.close_confirm_delete_popup)
        no_button.grid(row=1, column=2, pady=10)
        no_button.bind('<Enter>', on_enter)
        no_button.bind('<Leave>', on_leave)

        # Bind the close button to the window close event to handle closing the popup
        self.delete_popup.protocol("WM_DELETE_WINDOW", self.close_confirm_delete_popup)

    def close_confirm_delete_popup(self):
        self.__confirm_deletion_popup_open = False
        self.delete_popup.destroy()

    def EgramPopUp(self):
        if self.__confirm_egram_popup_open:
            return

        self.__confirm_egram_popup_open = True
        self.egram_popup = tk.Toplevel()
        self.egram_popup.geometry("750x750")
        self.egram_popup.title("Egram")
        EGRAM(self.egram_popup)
        #live_graph(self.egram_popup)

        x = self.__root.winfo_x()
        y = self.__root.winfo_y()
        self.egram_popup.geometry("+%d+%d" % (x + 350, y + 30))
        # Bind the close button to the window close event to handle closing the popup
        self.egram_popup.protocol("WM_DELETE_WINDOW", self.close_egram_popup)

    def close_egram_popup(self):
        self.__confirm_egram_popup_open = False
        self.egram_popup.destroy()

    def mainmenu(self):
        menu = tk.Frame(navigator.get_main_app())
        menu.pack(side='top', fill='both', expand=True)
        navigator.set_current_frame(menu)

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

        # New Patient button to return to login page
        egram_btn = tk.Button(menu, text="View Egram",
                              command=lambda:
                              self.EgramPopUp())

        # Create frame for Set Mode
        set_mode_frame = tk.Frame(menu)
        SetMode(set_mode_frame)

        # Pack frames and buttons to the screen
        menu_bar.pack(pady=5, fill="x")
        modes_frame.pack(pady=10, padx=10, fill="both")
        set_mode_frame.pack(pady=10)
        newpatient_btn.pack(pady=10)
        egram_btn.pack(pady=10)

        self.check_pacemaker_connection()

        delete_user_button = tk.Button(menu, text="Delete Account", command=lambda:
        self.confirm_deletion_popup())
        delete_user_button.pack(pady=10)


window = tk.Tk()
DCM(window)
window.mainloop()
