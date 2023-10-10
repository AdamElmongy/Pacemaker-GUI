import tkinter
import functions


def updatepar(mode, data, entryList, error_lbl, num_par):
    error_lbl.config(text="")
    for e in range(num_par):
        try:
            float(entryList[e].get())
        except ValueError:  # did not enter a number
            error_lbl.config(text="Invalid entry for " + data[e][0] + ". Enter as number!")
        if data[e][1][0] <= float(entryList[e].get()) <= data[e][1][1]:
            data[e][1][3] = float(entryList[e].get())
        else:
            error_lbl.config(text="Entry is out of range for " + data[e][0] + ".")

    functions.writeToFile(mode + "parameters", data)
    print(data)


def modePage(mode, page):
    page.title(mode + " Mode")
    data = functions.openFile(mode + "parameters")

    index = 0
    modes = ["AOO", "VOO", "AAI", "VVI"]
    for m in range(len(modes)):
        if modes[m] == mode:
            index = m
            break

    num_par = [4, 4, 5, 5]  # [AOO, VOO, AAI, VVI]

    p1 = tkinter.Entry(page)
    p2 = tkinter.Entry(page)
    p3 = tkinter.Entry(page)
    p4 = tkinter.Entry(page)
    p5 = tkinter.Entry(page)

    entry_list = [p1, p2, p3, p4, p5]

    for i in range(num_par[index]):
        par_lbl = tkinter.Label(page, text="Parameter: " + data[i][0])
        par_lbl.grid(row=i, column=0)

        entry_list[i].insert(0, data[i][1][3])
        entry_list[i].grid(row=i, column=1)

        value_range = str(data[i][1][0]) + "-" + str(data[i][1][1]) + data[i][1][4]
        par_range = tkinter.Label(page, text="Value range is " + value_range)
        par_range.grid(row=i, column=2)

    error_lbl = tkinter.Label(page, text="")
    updateBtn = tkinter.Button(page, text="Update",
                               command=lambda:
                               updatepar(mode, data, entry_list, error_lbl, num_par[index]))
    updateBtn.grid(row=num_par[index] + 1, columnspan=2)
    error_lbl.grid(row=num_par[index] + 2, columnspan=2)


state = tkinter.Tk()
state.geometry("500x500")
modePage("VVI", state)
state.mainloop()
