import tkinter

about = tkinter.Tk()
about .geometry("500x500")
about.title("About")

mode_lbl = tkinter.Label(about, text = "MODE: "+"string fetched from New Patient")
mode_lbl.pack(padx=20, pady=20)

DCM_lbl = tkinter.Label(about, text = "DCM ID: "+"string fetched from New Patient")
DCM_lbl.pack(padx=20, pady=20)

institution_lbl = tkinter.Label(about, text = "Institution: "+"string fetched from New Patient")
institution_lbl.pack(padx=20, pady=20)

about.mainloop()

