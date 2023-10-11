import tkinter as tk
from functions import openFile
from NewPatient import NewPatient
from Navigation import navigator

data = openFile("global")

def About():

    def switch_to_new_patient():
        about.destroy()
        NewPatient()

    about = tk.Tk()
    about .geometry("500x500")
    about.title("About")

    mode_lbl = tk.Label(about, text = f"MODE: {data['Mode']}")
    mode_lbl.pack(padx=20, pady=20)

    model_number_lbl = tk.Label(about, text = f"Model Number: {data['ModelNumber']}")
    model_number_lbl.pack(padx=20, pady=20)

    DCM_lbl = tk.Label(about, text = f"DCM ID: {data['DCMNumber']}")
    DCM_lbl.pack(padx=20, pady=20)

    institution_lbl = tk.Label(about, text = f"Institution: {data['Institution']}")
    institution_lbl.pack(padx=20, pady=20)

    new_patient_label = tk.Label(about, text="Enter a New Patient:")
    new_patient_label.pack()
    new_patient_button = tk.Button(about, text="New Patient", command=lambda: navigator.navigate_to_page("NewPatient"))
    new_patient_button.pack()

    about.mainloop()


navigator.register_page("About", About)

if __name__ == "__main__":
    About()

