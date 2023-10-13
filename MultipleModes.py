import tkinter
from functions import writeToFile, openFile, getCurrentUser
from tkinter import messagebox


def updatepar(mode, data, entryList):
    user = getCurrentUser()
    user_file_path = f"Users/{user}"
    user_data = openFile(user_file_path)
    for i, entry in enumerate(data):
        try:
            float(entryList[i].get())  # did the user enter a float?
        except:  # did not enter a number as digits
            messagebox.showerror("Error", "Invalid entry for " + entry + ". Enter as number!")
        if data[entry][0] <= float(entryList[i].get()) <= data[entry][1]:  # check if valid parameter value
            data[entry][3] = float(entryList[i].get())  # store in file
            user_data['mode-values'][mode][entry] = float(entryList[i].get())

        else:
            messagebox.showerror("Error", f"Entry is out of range for {data[entry][0]}.")

    writeToFile(user_file_path, user_data)
    writeToFile(mode + "parameters", data)
    print(data)


def modePage(mode, page):
    data = openFile("ModeParameters")[mode]
    user = getCurrentUser()
    user_file_path = f"Users/{user}"
    user_mode_data = openFile(user_file_path)['mode-values'][mode]
    # data looks like: ["parameter", [min, max, default, set by user, "units"]]

    # placeholders for parameters, matches the max # in num_par
    p1 = tkinter.Entry(page)
    p2 = tkinter.Entry(page)
    p3 = tkinter.Entry(page)
    p4 = tkinter.Entry(page)
    p5 = tkinter.Entry(page)

    entry_list = [p1, p2, p3, p4, p5]

    for i, entry in enumerate(data):  # for every parameter for the mode
        par_lbl = tkinter.Label(page, text=f"Parameter: {entry}")
        par_lbl.grid(row=i, column=0)

        entry_list[i].insert(0, user_mode_data[entry])
        entry_list[i].grid(row=i, column=1)

        value_range = str(data[entry][0]) + "-" + str(data[entry][1]) + data[entry][4]
        par_range = tkinter.Label(page, text="Value range is " + value_range)
        par_range.grid(row=i, column=2)

    updateBtn = tkinter.Button(page, text="Update",
                               command=lambda:
                               updatepar(mode, data, entry_list))
    updateBtn.grid(row=len(data) + 1, columnspan=2)


# uncomment this to test this file alone (without Modes.py)
# state = tkinter.Tk()
# state.geometry("500x500")
# #modePage("VVI", state)
# state.mainloop()
