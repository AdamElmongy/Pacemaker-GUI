import tkinter as tk
from functions import openFile
from NewPatient import NewPatient
from Navigation import navigator

data = openFile("global")

def About():
    about = tk.Tk()
    about .geometry("250x250")
    about.title("About")

    model_number_lbl = tk.Label(about, text=f"Model Number: H00140")  # {data['ModelNumber']}
    model_number_lbl.pack(padx=20, pady=20, anchor='w')

    DCM_lbl = tk.Label(about, text=f"DCM SN: 3K04-L04-GR4")  # {data['DCMNumber']}
    DCM_lbl.pack(padx=20, pady=20, anchor='w')

    institution_lbl = tk.Label(about, text=f"Institution: McMaster University")  # {data['Institution']}
    institution_lbl.pack(padx=20, pady=20, anchor='w')

    about.mainloop()

