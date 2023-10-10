import tkinter

modes = tkinter.Tk()
modes.geometry("500x500")
modes.title("Modes")


modeFrame = tkinter.Frame(modes)
mode = ["AOO", "VOO", "VVI", "AAI"]

for i in range(len(mode)):
    modeFrame.rowconfigure(i, weight=1)

AOOBtn = tkinter.Button(modeFrame, text="AOO")  # command would be to open AOO page
AOOBtn.grid(row=0, column=0)

VOOBtn = tkinter.Button(modeFrame, text="VOO")  # command would be to open VOO page
VOOBtn.grid(row=1, column=0)

VVIBtn = tkinter.Button(modeFrame, text="VVI")  # command would be to open VVI page
VVIBtn.grid(row=2, column=0)

AAIBtn = tkinter.Button(modeFrame, text="AAI")  # command would be to open  AAI page
AAIBtn.grid(row=3, column=0)

modeFrame.pack(pady=20)
modes.mainloop()
