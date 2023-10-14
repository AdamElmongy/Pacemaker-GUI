import tkinter as tk
from utils.Navigation import navigator
from Modes import Modes
from Menu import Menu
from utils.SetMode import SetMode


def main_menu():
    menu = tk.Frame(navigator.main_app)
    menu.pack(side='top', fill='both', expand=True)
    navigator.current_frame = menu

    # Create a menu bar at the top as a frame
    menu_bar = tk.Frame(menu)
    Menu(menu_bar)

    # Create a frame for the modes
    modes_frame = tk.Frame(menu)
    Modes(modes_frame)

    # New Patient button to return to login page
    newpatientBtn = tk.Button(menu, text="New Patient- return to Login",
                              command=lambda: navigator.navigate_to_signin("Menu", "Register"))

    # Create frame for Set Mode
    set_mode_frame = tk.Frame(menu)
    SetMode(set_mode_frame)

    # Pack frames and buttons to the screen
    menu_bar.pack(pady=5, fill="x")
    modes_frame.pack(pady=10, padx=10, fill="both")
    set_mode_frame.pack(pady=10)
    newpatientBtn.pack(pady=10)


navigator.register_page("Menu", main_menu)


if __name__ == "__main__":
    main_menu()
