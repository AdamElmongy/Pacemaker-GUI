import tkinter as tk
from About import About
from utils.Navigation import navigator
from Modes import Modes
from utils.SetClock import SetClock
from utils.SetMode import SetMode


def main_menu():
    menu = tk.Frame(navigator.main_app)
    menu.pack(side='top', fill='both', expand=True)
    navigator.current_frame = menu

    # Create a menu bar at the top as a frame
    menu_bar = tk.Frame(menu)
    menu_bar.columnconfigure(0, weight=1)
    menu_bar.columnconfigure(1, weight=1)
    menu_bar.columnconfigure(2, weight=1)

    aboutBtn = tk.Button(menu_bar, text="About", command=lambda: About())
    aboutBtn.grid(row=0, column=0, ipadx=10, sticky="w")

    date_lbl = tk.Label(menu_bar, text="DD/MM/YYYY 00:00:00")
    date_lbl.grid(row=0, column=1,)
    setclockBtn = tk.Button(menu_bar, text="Set Clock", command=lambda: SetClock(date_lbl))
    setclockBtn.grid(row=0, column=2, ipadx=10, sticky="e")

    # Create a frame for the modes
    modes_frame = tk.Frame(menu)
    Modes(modes_frame)

    # New Patient button to return to login page
    newpatientBtn = tk.Button(menu, text="New Patient- return to Login", command=lambda: navigator.navigate_to_signin("Menu", "Register"))  # command would be to open New Patient

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
