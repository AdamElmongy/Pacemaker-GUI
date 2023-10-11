import tkinter
from tkinter import ttk
import MultipleModes
from Navigation import navigator


def Modes():
    modes = tkinter.Tk()
    modes.geometry("500x500")
    modes.title("Modes")

    notebook = ttk.Notebook(modes)
    notebook.pack(fill='both', expand=True)

    AOO_frame = tkinter.Frame(notebook)
    notebook.add(AOO_frame, text='AOO')
    MultipleModes.modePage("AOO", AOO_frame)

    VOO_frame = tkinter.Frame(notebook)
    notebook.add(VOO_frame, text='VOO')
    MultipleModes.modePage("VOO", VOO_frame)

    AAI_frame = tkinter.Frame(notebook)
    notebook.add(AAI_frame, text='AAI')
    MultipleModes.modePage("AAI", AAI_frame)

    VVI_frame = tkinter.Frame(notebook)
    notebook.add(VVI_frame, text='VVI')
    MultipleModes.modePage("VVI", VVI_frame)

    modes.mainloop()

Modes()
navigator.register_page("Modes", Modes)