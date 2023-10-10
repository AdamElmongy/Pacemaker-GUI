import tkinter
import functions


AOO = tkinter.Tk()
AOO.geometry("500x500")
AOO.title("AOO Mode")

# Parameters to be displayed and modified
# Lower rate limit, Upper rate limit, Atrial Amplitude, Atrial Pulse Width


data = functions.openFile("AOO"+"parameters")

p1_entry = tkinter.Entry(AOO)
p2_entry = tkinter.Entry(AOO)
p3_entry = tkinter.Entry(AOO)
p4_entry = tkinter.Entry(AOO)

entryList = [p1_entry, p2_entry, p3_entry, p4_entry]

def updatepar():
    error_lbl.config(text="")
    for e in range(len(entryList)):
        try:
            float(entryList[e].get())
        except ValueError:  # did not enter a number
            error_lbl.config(text="Invalid entry for "+ data[e][0] + ". Enter as number!")
        if data[e][1][0] <= float(entryList[e].get()) <= data[e][1][1]:
            data[e][1][3] = float(entryList[e].get())
        else:
            error_lbl.config(text="Entry is out of range for "+ data[e][0] + ".")

    functions.writeToFile("AOO"+"parameters", data)
    print(data)

for i in range(len(entryList)):
    par_lbl = tkinter.Label(AOO, text="Parameter: " + data[i][0])
    par_lbl.grid(row=i, column=0)

    entryList[i].insert(0, data[i][1][3])
    entryList[i].grid(row=i, column=1)

    value_range = str(data[i][1][0]) + "-" + str(data[i][1][1]) + data[i][1][4]
    par_range = tkinter.Label(AOO, text="Value range is "+value_range)
    par_range.grid(row=i, column=2)

error_lbl = tkinter.Label(AOO, text="")
updateBtn = tkinter.Button(AOO, text= "Update", command = lambda: updatepar())
updateBtn.grid(row=len(entryList)+1, columnspan=2)
error_lbl.grid(row=len(entryList)+2, columnspan=2)

AOO.mainloop()