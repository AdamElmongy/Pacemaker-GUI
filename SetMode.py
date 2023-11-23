import tkinter as tk
from utils.functions import writeToFile, openFile, getCurrentUser


class SetMode:
    def __init__(self, frame):
        self.__frame = frame
        self.__selection = tk.StringVar()
        self.__default_mode = "AOO"
        self.__modes = ["AOO", "VOO", "AAI", "VVI", "AOOR", "VOOR", "AAIR", "VVIR"]
        self.interface()


    def interface(self):
        # set default selection to default mode
        self.__selection.set(self.__default_mode)

        # Labels, Drop down menu and Configure button
        set_lbl = tk.Label(self.__frame, text="Select a mode:")
        drop = tk.OptionMenu(self.__frame, self.__selection, *self.__modes)  # * for every string in []
        complete_btn = tk.Button(self.__frame, text="Configure Pacemaker", bg="light blue",
                                 command=lambda: self.SaveParameters())

        # Layout on the frame
        set_lbl.grid(row=0, column=0)
        drop.grid(row=0, column=1, ipadx=20)
        complete_btn.grid(row=0, column=2, padx=20, ipadx=50, ipady=10)

    def SaveParameters(self):
        user = getCurrentUser()
        mode = self.__selection.get()
        user_file_path = f"Users/{user}"
        user_mode_data = openFile(user_file_path)['mode-values'][mode]

        data = [mode]
        for i in user_mode_data:
            data.append(user_mode_data[i])

        writeToFile('data/send', data)

        print("sending "+str(data)+" to pacemaker")
        return


# def SetMode(frame):
#     # Allow user to select a mode from an option menu
#     set_lbl = tk.Label(frame, text="Select a mode:")
#
#     selection = tk.StringVar()
#     selection.set("AOO")  # set default mode to AOO
#
#     drop = tk.OptionMenu(frame, selection, "AOO", "VOO", "AAI", "VVI")
#     set_lbl.grid(row=0, column=0)
#     drop.grid(row=0, column=1, ipadx=20)
#
#     # Set pacemaker button
#     complete_btn = tk.Button(frame, text="Configure Pacemaker", bg="light blue",
#                              command=lambda: SaveParameters(selection))
#     complete_btn.grid(row=0, column=2, padx=20, ipadx=50, ipady=10)
#
# # uncomment this to test this file alone (without MainMenu.py)
# # root = tk.Tk()
# # root.geometry("500x500")
# # SetMode(root)
# # root.mainloop()
