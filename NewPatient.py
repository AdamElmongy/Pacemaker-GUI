import tkinter as tk
from functions import openFile, writeToFile
from Navigation import navigator


def NewPatient():

    def switch_to_new_patient():
        newPatient.destroy()
        NewPatient()

    def save():
        ModelNumber = model_number_entry.get()
        DCMNumber = dcm_number_entry.get()
        Institution = institution_entry.get()
        data = openFile('global')

        data['ModelNumber'] = ModelNumber
        data['DCMNumber'] = DCMNumber
        data['Institution'] = Institution
        print(data)
        
        print(writeToFile('global', data))

    newPatient = tk.Tk()

    # Frame for Main Menu
    new_patient_frame = tk.Frame(newPatient)
    new_patient_frame.pack(fill='both', expand=True)

    model_number_label = tk.Label(new_patient_frame, text="Model Number:")
    model_number_label.pack()
    model_number_entry = tk.Entry(new_patient_frame)
    model_number_entry.pack()

    dcm_number_label = tk.Label(new_patient_frame, text="DCM Number:")
    dcm_number_label.pack()
    dcm_number_entry = tk.Entry(new_patient_frame)
    dcm_number_entry.pack()

    institution_label = tk.Label(new_patient_frame, text="Institution:")
    institution_label.pack()
    institution_entry = tk.Entry(new_patient_frame)
    institution_entry.pack()

    back_button = tk.Button(new_patient_frame, text="Back", command=lambda: navigator.navigate_to_page("Main"))
    back_button.pack()

    save_button = tk.Button(new_patient_frame, text="Save", command=save)
    save_button.pack()

    newPatient.mainloop()

navigator.register_page("NewPatient", NewPatient)

if __name__ == "__main__":
    NewPatient()


