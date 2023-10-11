import tkinter as tk

def main_menu(root):
    root.title("Main Menu")
    menu = tk.Frame(root)
    menu.pack(fill='both', expand=True)


    aboutBtn = tkinter.Button(menu, text = "About")  # command would be to open About page
    aboutBtn.pack(padx=10, pady=10)

    setclockBtn = tkinter.Button(menu, text = "Set Clock")  # command would be to open SetClock page
    setclockBtn.pack(padx=10, pady=10)

    newpatientBtn = tkinter.Button(menu, text = "New Patient")  # command would be to open New Patient
    newpatientBtn.pack(padx=10, pady=10)

    modeBtn = tkinter.Button(menu, text = "Modes")  # command would be to open the Mode page
    modeBtn.pack(padx=10, pady=10)

    aboutBtn = tk.Button(menu, text="About")  # command would be to open the next window
    aboutBtn.pack(padx=10, pady=10)

    setclockBtn = tk.Button(menu, text="Set Clock")
    setclockBtn.pack(padx=10, pady=10)

    newpatientBtn = tk.Button(menu, text="New Patient")
    newpatientBtn.pack(padx=10, pady=10)

    modeBtn = tk.Button(menu, text="Mode")
    modeBtn.pack(padx=10, pady=10)

    menu.mainloop()


if __name__ == "__main__":
    main_menu()
