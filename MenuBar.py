import tkinter as tk
import datetime


class MenuBar:
    def __init__(self, menu_frame):
        # create menu frame, about pop up, and button/labels
        self.__menu_bar = menu_frame
        self.__aboutBtn = tk.Button(self.__menu_bar, text="About", command=lambda: self.About())
        self.__date_lbl = tk.Label(self.__menu_bar, text="DD/MM/YYYY 00:00:00")
        self.__setclockBtn = tk.Button(self.__menu_bar, text="Set Clock",
                                       command=lambda: self.SetClock())
        self.about = None  # container for pop up
        # Attributes for About() method
        self.__about_popup_open = False  # Flag variable to track if the About popup is open
        # self.data = openFile("data/global")

        self.layout()

    def layout(self):
        self.__menu_bar.columnconfigure(0, weight=1)
        self.__menu_bar.columnconfigure(1, weight=1)
        self.__menu_bar.columnconfigure(2, weight=1)

        # About button in the top left corner
        self.__aboutBtn.grid(row=0, column=0, ipadx=10, sticky="w")

        # Header with date and time at the top center
        self.__date_lbl.grid(row=0, column=1)

        # Set Clock Button in the top right corner
        self.__setclockBtn.grid(row=0, column=2, ipadx=10, sticky="e")

    def SetClock(self):
        date = datetime.datetime.now()
        date_str = date.strftime("%m/%d/%Y, %H:%M:%S")
        self.__date_lbl.configure(text=date_str)

    def About(self):
        if self.__about_popup_open:
            return

        self.__about_popup_open = True
        self.about = tk.Toplevel()
        self.about.geometry("250x250")
        self.about.title("About")

        model_number_lbl = tk.Label(self.about, text=f"Model Number: H00140")
        model_number_lbl.pack(padx=20, pady=20, anchor='w')

        DCM_lbl = tk.Label(self.about, text=f"DCM SN: 3K04-L04-GR4")
        DCM_lbl.pack(padx=20, pady=20, anchor='w')

        institution_lbl = tk.Label(self.about, text=f"Institution: McMaster University")
        institution_lbl.pack(padx=20, pady=20, anchor='w')

        close_button = tk.Button(self.about, text="Close", command=self.close_about_popup)
        close_button.pack(pady=20)

        # Bind the close button to the window close event to handle closing the popup
        self.about.protocol("WM_DELETE_WINDOW", self.close_about_popup)

    def close_about_popup(self):
        self.__about_popup_open = False
        self.about.destroy()




