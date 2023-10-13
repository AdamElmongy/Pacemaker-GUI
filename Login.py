import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from MainMenu import main_menu
from functions import openFile, writeToFile
from Navigation import navigator


def signin(tab=None):

    def login():
        ID = login_username_entry.get()
        password = login_password_entry.get()
        users = openFile('users')
        for user in users:
            if ID == user[0] and password == user[1]:
                # show_main_menu()  # Switch to the main menu page
                switch_to_main_menu()
                return
        messagebox.showerror("Error", "Invalid username or password")

    def register():
        ID = register_username_entry.get()
        password = register_password_entry.get()
        users = openFile('users')
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
            writeToFile('users', users)  # Assuming writeToFile function writes the data to a file
            writeToFile(f'Users/{ID}', users)
            # show_main_menu()  # Switch to the main menu page
            switch_to_main_menu()

    # Function for switching to the Main Menu page
    # def show_main_menu():
    #     # Hide the login and register tabs
    #     notebook.pack_forget()
    #     # Show the main menu frame
    #     main_menu_frame.pack(fill='both', expand=True)
    #     # Call the main_menu function to populate the frame
    #     main_menu(signin)

    def switch_to_main_menu():
        signin.destroy()
        main_menu()

    signin = tk.Tk()
    signin.title("Login/Register Form")
    signin.geometry("500x500")

    # Create a Notebook (tabbed interface) for login and register
    notebook = ttk.Notebook(signin)
    notebook.pack(fill='both', expand=True)

    # Frame for Login tab
    login_frame = ttk.Frame(notebook)
    notebook.add(login_frame, text='Login')

    # Frame for Register tab
    register_frame = ttk.Frame(notebook)
    notebook.add(register_frame, text='Register')

    # Frame for Main Menu
    main_menu_frame = ttk.Frame(signin)

    # Login Tab
    login_username_label = tk.Label(login_frame, text="Username:")
    login_username_label.pack()
    login_username_entry = tk.Entry(login_frame)
    login_username_entry.pack()

    login_password_label = tk.Label(login_frame, text="Password:")
    login_password_label.pack()
    login_password_entry = tk.Entry(login_frame, show="*")
    login_password_entry.pack()

    login_button = tk.Button(login_frame, text="Login", command=login)
    login_button.pack()

    # Register Tab
    register_username_label = tk.Label(register_frame, text="Username:")
    register_username_label.pack()
    register_username_entry = tk.Entry(register_frame)
    register_username_entry.pack()

    register_password_label = tk.Label(register_frame, text="Password:")
    register_password_label.pack()
    register_password_entry = tk.Entry(register_frame, show="*")
    register_password_entry.pack()

    register_button = tk.Button(register_frame, text="Register", command=register)
    register_button.pack()

    # Run the Tkinter main loop
    notebook.select(register_frame) if tab == "Register" else notebook.select(login_frame)
    signin.mainloop()

navigator.register_page("SignIn", signin)

if __name__ == "__main__":
    signin()


