import tkinter as tk
import datetime
from utils.functions import openFile


class MenuBar:
    def __init__(self, menu_frame):
        # create menu frame and button/labels
        self.menu_bar = menu_frame
        self.aboutBtn = tk.Button(self.menu_bar, text="About", command=lambda: self.__About())
        self.date_lbl = tk.Label(self.menu_bar, text="DD/MM/YYYY 00:00:00")
        self.setclockBtn = tk.Button(self.menu_bar, text="Set Clock",
                                     command=lambda: self.__SetClock())

        # Attributes for About() method
        self.about_popup_open = False  # Flag variable to track if the About popup is open
        self.data = openFile("data/global")

        self.__layout()

    def __layout(self):
        self.menu_bar.columnconfigure(0, weight=1)
        self.menu_bar.columnconfigure(1, weight=1)
        self.menu_bar.columnconfigure(2, weight=1)

        # About button in the top left corner
        self.aboutBtn.grid(row=0, column=0, ipadx=10, sticky="w")

        # Header with date and time at the top center
        self.date_lbl.grid(row=0, column=1)

        # Set Clock Button in the top right corner
        self.setclockBtn.grid(row=0, column=2, ipadx=10, sticky="e")

    def __SetClock(self):
        date = datetime.datetime.now()
        date_str = date.strftime("%m/%d/%Y, %H:%M:%S")
        self.date_lbl.configure(text=date_str)

    def __About(self):
        if self.about_popup_open:
            return

        self.about = tk.Toplevel()
        self.about_popup_open = True
        self.about.geometry("250x250")
        self.about.title("About")

        model_number_lbl = tk.Label(self.about, text=f"Model Number: H00140")
        model_number_lbl.pack(padx=20, pady=20, anchor='w')

        DCM_lbl = tk.Label(self.about, text=f"DCM SN: 3K04-L04-GR4")
        DCM_lbl.pack(padx=20, pady=20, anchor='w')

        institution_lbl = tk.Label(self.about, text=f"Institution: McMaster University")
        institution_lbl.pack(padx=20, pady=20, anchor='w')

        close_button = tk.Button(self.about, text="Close", command=self.__close_about_popup)
        close_button.pack(pady=20)

        # Bind the close button to the window close event to handle closing the popup
        self.about.protocol("WM_DELETE_WINDOW", self.__close_about_popup)

    def __close_about_popup(self):
        self.about_popup_open = False
        self.about.destroy()




