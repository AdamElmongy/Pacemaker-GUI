import tkinter as tk
from About import About
from Navigation import navigator
from Modes import Modes


def main_menu(root):
    # root = tk.Tk()

    def switch_to_about():
        root.destroy()
        About()

    root.title("Main Menu")
    menu = tk.Frame(root)
    menu.pack(fill='both', expand=True)

    aboutBtn = tk.Button(menu, text = "About", command=lambda: navigator.navigate_to_page("About"))  # command would be to open About page

    # aboutBtn = tk.Button(menu, text="About", command=switch_to_about)  # command would be to open the next window

    aboutBtn.pack(padx=10, pady=10)

    setclockBtn = tk.Button(menu, text = "Set Clock", command=lambda: navigator.navigate_to_page("SetClock"))  # command would be to open SetClock page
    setclockBtn.pack(padx=10, pady=10)

    newpatientBtn = tk.Button(menu, text = "New Patient", command=lambda: navigator.navigate_to_signin("Register"))  # command would be to open New Patient
    newpatientBtn.pack(padx=10, pady=10)

    modeBtn = tk.Button(menu, text = "Modes", command=Modes)  # command would be to open the Mode page
    modeBtn.pack(padx=10, pady=10)


    menu.mainloop()


if __name__ == "__main__":
    main_menu()
