import datetime

def SetClock(date_lbl):
    date = datetime.datetime.now()
    date_str = date.strftime("%m/%d/%Y, %H:%M:%S")
    date_lbl.configure(text=date_str)
