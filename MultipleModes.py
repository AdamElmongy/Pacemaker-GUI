import tkinter
import functions
from tkinter import messagebox


def updatepar(mode, data, entryList, num_par):
    for e in range(num_par):
        try:
            float(entryList[e].get())  # did the user enter a float?
        except:  # did not enter a number as digits
            messagebox.showerror("Error", "Invalid entry for " + data[e][0] + ". Enter as number!")
        if data[e][1][0] <= float(entryList[e].get()) <= data[e][1][1]:  # check if valid parameter value
            data[e][1][3] = float(entryList[e].get())  # store in file
        else:
            messagebox.showerror("Error", "Entry is out of range for " + data[e][0] + ".")

    functions.writeToFile(mode + "parameters", data)
    print(data)


def modePage(mode, page):
    data = functions.openFile(mode + "parameters")
    # data looks like: ["parameter", [min, max, default, set by user, "units"]]

    # Determine which mode was passed and assign to index to identify mode as a number
    index = 0
    modes = ["AOO", "VOO", "AAI", "VVI"]
    for m in range(len(modes)):
        if modes[m] == mode:
            index = m
            break

    # number of parameters for each mode (order corresponds to "modes" list)
    num_par = [4, 4, 5, 5]  # [AOO, VOO, AAI, VVI]

    # placeholders for parameters, matches the max # in num_par
    p1 = tkinter.Entry(page)
    p2 = tkinter.Entry(page)
    p3 = tkinter.Entry(page)
    p4 = tkinter.Entry(page)
    p5 = tkinter.Entry(page)

    entry_list = [p1, p2, p3, p4, p5]

    for i in range(num_par[index]):  # for every parameter for the mode
        par_lbl = tkinter.Label(page, text="Parameter: " + data[i][0])
        par_lbl.grid(row=i, column=0)

        entry_list[i].insert(0, data[i][1][3])
        entry_list[i].grid(row=i, column=1)

        value_range = str(data[i][1][0]) + "-" + str(data[i][1][1]) + data[i][1][4]
        par_range = tkinter.Label(page, text="Value range is " + value_range)
        par_range.grid(row=i, column=2)

    updateBtn = tkinter.Button(page, text="Update",
                               command=lambda:
                               updatepar(mode, data, entry_list, num_par[index]))
    updateBtn.grid(row=num_par[index] + 1, columnspan=2)


# uncomment this to test this file alone (without Modes.py)
# state = tkinter.Tk()
# state.geometry("500x500")
# #modePage("VVI", state)
# state.mainloop()
