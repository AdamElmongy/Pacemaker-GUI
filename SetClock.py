import tkinter
import datetime

SetClock = tkinter.Tk()
SetClock .geometry("500x500")
SetClock.title("SetClock")

date = datetime.datetime.now()
date_str = date.strftime("%m/%d/%Y, %H:%M")

date_lbl = tkinter.Label(SetClock, text=date_str)
date_lbl.pack(padx=20, pady=20)

SetClock.mainloop()