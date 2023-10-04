import tkinter

menu = tkinter.Tk()
menu.geometry("500x500")
menu.title("Main Menu")

aboutBtn = tkinter.Button(menu, text = "About")  # command would be to open the next window
aboutBtn.pack(padx=10, pady=10)

setclockBtn = tkinter.Button(menu, text = "Set Clock")
setclockBtn.pack(padx=10, pady=10)

newpatientBtn = tkinter.Button(menu, text = "New  Patient")
newpatientBtn.pack(padx=10, pady=10)

modeBtn = tkinter.Button(menu, text = "Mode")
modeBtn.pack(padx=10, pady=10)

menu.mainloop()

