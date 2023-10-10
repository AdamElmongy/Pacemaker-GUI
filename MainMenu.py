import tkinter

menu = tkinter.Tk()
menu.geometry("500x500")
menu.title("Main Menu")

aboutBtn = tkinter.Button(menu, text = "About")  # command would be to open About page
aboutBtn.pack(padx=10, pady=10)

setclockBtn = tkinter.Button(menu, text = "Set Clock")  # command would be to open SetClock page
setclockBtn.pack(padx=10, pady=10)

newpatientBtn = tkinter.Button(menu, text = "New Patient")  # command would be to open New Patient
newpatientBtn.pack(padx=10, pady=10)

modeBtn = tkinter.Button(menu, text = "Modes")  # command would be to open the Mode page
modeBtn.pack(padx=10, pady=10)

menu.mainloop()

