import tkinter
from tkinter import ttk
from utils.functions import writeToFile, openFile, getCurrentUser
from tkinter import messagebox, END


class Modes:

    def __init__(self, root):
        self.__root = root
        self.__notebook = ttk.Notebook(root)
        self.__max_par = 9
        self.createTabs()

    def createTabs(self):

        # Frame for each mode
        AOO_frame = tkinter.Frame(self.__notebook)
        VOO_frame = tkinter.Frame(self.__notebook)
        AAI_frame = tkinter.Frame(self.__notebook)
        VVI_frame = tkinter.Frame(self.__notebook)
        AOOR_frame = tkinter.Frame(self.__notebook)
        VOOR_frame = tkinter.Frame(self.__notebook)
        AAIR_frame = tkinter.Frame(self.__notebook)
        VVIR_frame = tkinter.Frame(self.__notebook)

        self.__notebook.add(AOO_frame, text='AOO')
        self.modePage("AOO", AOO_frame)

        self.__notebook.add(VOO_frame, text='VOO')
        self.modePage("VOO", VOO_frame)

        self.__notebook.add(AAI_frame, text='AAI')
        self.modePage("AAI", AAI_frame)

        self.__notebook.add(VVI_frame, text='VVI')
        self.modePage("VVI", VVI_frame)

        self.__notebook.add(AOOR_frame, text='AOOR')
        self.modePage("AOOR", AOOR_frame)

        self.__notebook.add(VOOR_frame, text='VOOR')
        self.modePage("VOOR", VOOR_frame)

        self.__notebook.add(AAIR_frame, text='AAIR')
        self.modePage("AAIR", AAIR_frame)

        self.__notebook.add(VVIR_frame, text='VVIR')
        self.modePage("VVIR", VVIR_frame)

        self.__notebook.pack(side='top', fill='both', expand=True)

    def updatepar(self, mode, data, entryList, page):
        New_Modes = ["AAIR", "AOOR", "AAIR", "AOOR"]
        user = getCurrentUser()
        user_file_path = f"Users/{user}"
        user_data = openFile(user_file_path)
        print(data)
        for i in range(len(entryList)):
            print("h")
            print(entryList[i].get())
        for i, entry in enumerate(data):
            try:
                float(entryList[i].get())  # did the user enter a float?
            except ValueError:  # did not enter a number as digits
                messagebox.showerror("Error", "Invalid entry for " + entry + ". Enter as number!")
            # print("z")
            # print(entryList[-2].get())
            # print(entryList[0].get())
            # print(entryList[-5].get())
            # print((float(entryList[-2].get()) - float(entryList[0].get())) / float(entryList[-5].get()) <= float(7))
            if not float(entryList[0].get()) < float(entryList[1].get()):
                entryList[0].delete(0, END)
                entryList[0].insert(0, int(user_data['mode-values'][mode]["LRL"]))
                entryList[1].delete(0, END)
                entryList[1].insert(0, int(user_data['mode-values'][mode]["URL"]))
                messagebox.showerror("Error", "Invalid entry: LRL value must be less than URL!")
                return
            elif mode in New_Modes and not float(entryList[0].get()) < float(entryList[-2].get()):
                entryList[0].delete(0, END)
                entryList[0].insert(0, int(user_data['mode-values'][mode]["LRL"]))
                entryList[-2].delete(0, END)
                entryList[-2].insert(0, int(user_data['mode-values'][mode]["MSR"]))
                messagebox.showerror("Error", "Invalid entry: LRL value must be less than MSR!")
                return
            elif mode in New_Modes and not ((float(entryList[-2].get()) - float(entryList[0].get())) / float(entryList[-5].get()) <= 7):
                entryList[0].delete(0, END)
                entryList[0].insert(0, int(user_data['mode-values'][mode]["LRL"]))
                entryList[-2].delete(0, END)
                entryList[-2].insert(0, int(user_data['mode-values'][mode]["MSR"]))
                messagebox.showerror(
                    "Error", "Invalid entry: Parameters cause unsafe pacing conditions. Increase the reaction time or LRL or decrease the MSR to resolve this issue.")
                return

            if data[entry][0] <= float(entryList[i].get()) <= data[entry][1]:  # check if valid parameter value
                if data[entry][4] == "B":
                    try:
                        int(entryList[i].get())  # did the user enter an integer?
                        user_data['mode-values'][mode][entry] = int(entryList[i].get())  # store in file
                    except ValueError:  # did not enter a number as an integer
                        entryList[i].delete(0, END)
                        entryList[i].insert(0, int(user_data['mode-values'][mode][entry]))
                        messagebox.showerror("Error", "Invalid entry for " + entry + ". Enter as Integer!")
                else:
                    user_data['mode-values'][mode][entry] = float(entryList[i].get())
                print(user_data['mode-values'][mode][entry])
                
                print(entryList[i].get())
            else:
                messagebox.showerror("Error", f"Entry is out of range for {entry}.")

        writeToFile(user_file_path, user_data)
        print(user_data)

    def modePage(self, mode, page):
        # configure the frame to space out the columns
        page.columnconfigure(0, weight=1)
        page.columnconfigure(1, weight=1)
        page.columnconfigure(2, weight=1)

        # number of placeholders for parameters, matches the max # in num_par
        entry_list = []
        for i in range(self.__max_par):
            p = tkinter.Entry(page)
            entry_list.append(p)

        # open the user's parameter file
        data = openFile("data/ModeParameters")[mode]
        # data looks like: ["parameter": [min, max, default, "units"]]
        user = getCurrentUser()
        user_file_path = f"Users/{user}"
        user_mode_data = openFile(user_file_path)['mode-values'][mode]
        # user_mode_data looks like: {"parameter": value, "parameter": value ... }

        for i, entry in enumerate(data):  # for every parameter for the mode
            par_lbl = tkinter.Label(page, text=f"Parameter: {entry}")
            par_lbl.grid(row=i, column=0, sticky="we", pady=2)
            print(user_mode_data[entry])
            entry_list[i].insert(0, int(user_mode_data[entry]) if data[entry][4] == "B" else user_mode_data[entry])
            entry_list[i].grid(row=i, column=1)

            value_range = str(data[entry][0]) + "-" + str(data[entry][1]) + data[entry][3]
            par_range = tkinter.Label(page, text="Value range is " + value_range)
            par_range.grid(row=i, column=2, sticky="we", pady=2)

        # Update File with the new parameter values
        updateBtn = tkinter.Button(page, text="Update " + mode + " parameters",
                                   command=lambda:
                                   self.updatepar(mode, data, entry_list, page))
        updateBtn.grid(row=len(data) + 2, column=0, columnspan=3, pady=20, ipadx=100)


