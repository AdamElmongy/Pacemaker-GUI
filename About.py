import tkinter as tk
from utils.functions import openFile

# Flag variable to track if the About popup is open
about_popup_open = False

data = openFile("data/global")

def About():
    global about_popup_open
    # Check if the popup is already open, if yes, return to avoid opening another one
    if about_popup_open:
        return

    about_popup_open = True
    about = tk.Toplevel()
    about.geometry("250x250")
    about.title("About")

    def close_about_popup():
        global about_popup_open
        about_popup_open = False
        about.destroy()

    model_number_lbl = tk.Label(about, text=f"Model Number: H00140")
    model_number_lbl.pack(padx=20, pady=20, anchor='w')

    DCM_lbl = tk.Label(about, text=f"DCM SN: 3K04-L04-GR4")
    DCM_lbl.pack(padx=20, pady=20, anchor='w')

    institution_lbl = tk.Label(about, text=f"Institution: McMaster University")
    institution_lbl.pack(padx=20, pady=20, anchor='w')

    close_button = tk.Button(about, text="Close", command=close_about_popup)
    close_button.pack(pady=20)

    # Bind the close button to the window close event to handle closing the popup
    about.protocol("WM_DELETE_WINDOW", close_about_popup)



# Example usage
if __name__ == "__main__":
    About()
