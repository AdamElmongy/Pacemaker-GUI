import tkinter
import datetime
from Navigation import navigator

def SetClock():
    def getdate():
        date = datetime.datetime.now()
        date_str = date.strftime("%m/%d/%Y, %H:%M:%S")
        displaylabel(date_str)

    def displaylabel(string):
        date_lbl.configure(text=string)

    Setclock = tkinter.Tk()
    Setclock.geometry("500x500")
    Setclock.title("SetClock")

    date_lbl = tkinter.Label(Setclock, text="hit update")
    date_lbl.pack(padx=20, pady=20)

    updatetimeBtn = tkinter.Button(Setclock, text="Update Date and Time", command=getdate)
    updatetimeBtn.pack(padx=10, pady=10)

    Setclock.mainloop()


navigator.register_page("SetClock", SetClock)
