import tkinter as tk
import functions

def SetMode(frame):
    # Allow user to select a mode from an option menu
    set_lbl = tk.Label(frame, text="Set pacemaker mode:")
    set_lbl.grid(row=0, column=0)