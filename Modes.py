import tkinter
from tkinter import ttk
from utils.Navigation import navigator
from utils.functions import writeToFile, openFile, getCurrentUser
from tkinter import messagebox


class Modes:

    def __init__(self, root):
        self.root = root
        self.notebook = ttk.Notebook(root)

        # Frame for each mode
        self.AOO_frame = tkinter.Frame(self.notebook)
        self.VOO_frame = tkinter.Frame(self.notebook)
        self.AAI_frame = tkinter.Frame(self.notebook)
        self.VVI_frame = tkinter.Frame(self.notebook)

        navigator.register_page("Modes", Modes)

        self.createTabs()

    def createTabs(self):
        self.notebook.pack(side='top', fill='both', expand=True)

        self.notebook.add(self.AOO_frame, text='AOO')
        self.__modePage("AOO", self.AOO_frame)

        self.notebook.add(self.VOO_frame, text='VOO')
        self.__modePage("VOO", self.VOO_frame)

        self.notebook.add(self.AAI_frame, text='AAI')
        self.__modePage("AAI", self.AAI_frame)

        self.notebook.add(self.VVI_frame, text='VVI')
        self.__modePage("VVI", self.VVI_frame)

    def __updatepar(self, mode, data, entryList):
        user = getCurrentUser()
        user_file_path = f"Users/{user}"
        user_data = openFile(user_file_path)
        for i, entry in enumerate(data):
            try:
                float(entryList[i].get())  # did the user enter a float?
            except ValueError:  # did not enter a number as digits
                messagebox.showerror("Error", "Invalid entry for " + entry + ". Enter as number!")
            if data[entry][0] <= float(entryList[i].get()) <= data[entry][1]:  # check if valid parameter value
                data[entry][3] = float(entryList[i].get())  # store in file
                user_data['mode-values'][mode][entry] = float(entryList[i].get())

            else:
                messagebox.showerror("Error", f"Entry is out of range for {entry}.")

        writeToFile(user_file_path, user_data)
        print(data)

    def __modePage(self, mode, page):
        # configure the frame to space out the columns
        page.columnconfigure(0, weight=1)
        page.columnconfigure(1, weight=1)
        page.columnconfigure(2, weight=1)

        # open the user's parameter file
        data = openFile("data/ModeParameters")[mode]
        # data looks like: ["parameter": [min, max, default, set by user, "units"]]

        data = openFile("data/ModeParameters")[mode]
        user = getCurrentUser()
        user_file_path = f"Users/{user}"
        user_mode_data = openFile(user_file_path)['mode-values'][mode]
        # data looks like: ["parameter", [min, max, default, set by user, "units"]]

        # number of placeholders for parameters, matches the max # in num_par
        p1 = tkinter.Entry(page)
        p2 = tkinter.Entry(page)
        p3 = tkinter.Entry(page)
        p4 = tkinter.Entry(page)
        p5 = tkinter.Entry(page)

        entry_list = [p1, p2, p3, p4, p5]

        for i, entry in enumerate(data):  # for every parameter for the mode
            par_lbl = tkinter.Label(page, text=f"Parameter: {entry}")
            par_lbl.grid(row=i, column=0, sticky="we", pady=2)

            entry_list[i].insert(0, user_mode_data[entry])
            entry_list[i].grid(row=i, column=1)

            value_range = str(data[entry][0]) + "-" + str(data[entry][1]) + data[entry][4]
            par_range = tkinter.Label(page, text="Value range is " + value_range)
            par_range.grid(row=i, column=2, sticky="we", pady=2)

        # Update File with the new parameter values
        updateBtn = tkinter.Button(page, text="Update",
                                   command=lambda:
                                   self.__updatepar(mode, data, entry_list))
        updateBtn.grid(row=len(data) + 2, column=0, columnspan=3, pady=20, ipadx=100)


