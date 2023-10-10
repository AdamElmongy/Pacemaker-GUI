import tkinter
import datetime

SetClock = tkinter.Tk()
SetClock .geometry("500x500")
SetClock.title("SetClock")

date_lbl = tkinter.Label(SetClock, text="hit update")
date_lbl.pack(padx=20, pady=20)
def getdate():
    date = datetime.datetime.now()
    date_str = date.strftime("%m/%d/%Y, %H:%M:%S")
    displaylabel(date_str)
def displaylabel(string):
    date_lbl.configure(text=string)


updatetimeBtn = tkinter.Button(SetClock, text="Update Date and Time", command=getdate)
updatetimeBtn.pack(padx=10, pady=10)

SetClock.mainloop()