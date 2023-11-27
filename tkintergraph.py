import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk as NavigationToolbar
import numpy as np
import serial
import struct
import time

class EGRAM:

    def __init__(self, root):
        self.__root = root
        self.__ATR_data = []
        self.__VENT_data = []
        self.__BOTH_data = []
        self.__x_time = []
        self.egram_page()
    def egram_page(self):
        graph_frame = tk.Frame(self.__root)
        ATR_button = tk.Button(self.__root, text="Show ATR EGRAM",
                               command = lambda: self.start_ATR("A"))
        ATR_button.pack(pady = 20)
        graph_frame.pack(pady = 20)
        # self.live_graph(graph_frame)
    def live_graph(self, root):
        """
        This function makes a live graph that integrates with a tkinter GUI.

        Parameters:
        root (tk.Tk): The root window of the tkinter GUI

        Returns:
        None
        """
        # Create a figure and axis for the graph
        fig, ax = plt.subplots()
        x = np.arange(0, 2*np.pi, 0.01)
        y = np.sin(x)
        print(y)
        line, = ax.plot(x, y)

        ax.set_title("Egram Live Graph")
        ax.set_xlabel("Time")
        ax.set_ylabel("Pulse")

        # Create a canvas to display the graph in the tkinter GUI
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        NavigationToolbar(canvas)

        # Update the graph every 100 milliseconds
        def update_graph():
            nonlocal x, y, line
            x += 0.1
            y = np.sin(x)
            line.set_data(x, y)
            ax.relim()
            ax.autoscale_view(True,True,True)
            canvas.draw()
            root.after(50, update_graph)

        # Start updating the graph
        update_graph()

    def start_ATR(self, signal_type):
        # Tell simulink to start sending back egram data
        SYNC = 0x33  # this tells simulink to enter send_egram
        packed_data_send = struct.pack("<B", SYNC)
        ser = serial.Serial("COM3", 115200, timeout=1)  # open serial port
        ser.reset_input_buffer()
        ser.reset_output_buffer()
        ser.write(packed_data_send)
        ser.close()

        # Read the data that is being sent back from simulink
        start_time = time.time()
        self.read_egram(start_time)
        self.plot_egram(signal_type)

    def read_egram(self, time_arg):
        start_time = time_arg
        # open port
        ser = serial.Serial("COM3", 115200, timeout=1)  # open serial port
        while time.time()-start_time < 10:
            proper_data = False
            while proper_data == False:
                ser.reset_input_buffer()
                read_byte = ser.read(16)
                if read_byte == b'':  # held in reading
                    ser.close()  # close and reopen
                    print(str(read_byte) + "cannot read")
                    return self.read_egram(start_time)

                egram_data = struct.unpack("<dd", read_byte)
                if 0 <= egram_data[0] <= 1 and 0 <= egram_data[1] <= 1:
                    proper_data = True
                    print("good: "+ str (egram_data))
                    self.store_data(egram_data, time.time()-start_time)
                if time.time()-start_time > 10:
                    print("timed out")
                    break
        ser.close()

    def store_data(self, egram_data, time):
        self.__x_time.append(time)
        self.__ATR_data.append(egram_data[0])
        self.__VENT_data.append(egram_data[0])
        self.__BOTH_data.append(egram_data)

    def plot_egram(self, signal_type):
        plot_frame = tk.Frame(self.__root)
        plot_frame.pack(pady= 20)
        x = self.__x_time
        y = [0] * len(x)
        if signal_type == "A":
            y = self.__ATR_data
        elif signal_type == "V":
            y = self.__VENT_data
        fig, ax = plt.subplots()
        ax.scatter(x, y)

        ax.set_title("Egram Live Graph")
        ax.set_xlabel("Time")
        ax.set_ylabel("Pulse")

        # Create a canvas to display the graph in the tkinter GUI
        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.clear_data()

    def clear_data(self):
        self.__ATR_data = []
        self.__VENT_data = []
        self.__BOTH_data = []
        self.__x_time = []

# root = tk.Tk()
# root.geometry("500x500")
# EGRAM(root)
# root.mainloop()

# when the e gram pop up is opened, the plot should be blank
# open port
# write to the pacemaker telling it to send egram data, i.e set data[1] = 0x33
# close port
# read data from the pacemaker.
# FOR NON-REAL TIME:
# store data from the past 10 seconds
# get start time
# while (time.time() - start_time < 10):
# read until a good point is properly read, i.e while proper_data = false
    # open port
    # ser.reset_input_buffer()
    # read_byte = ser.read(16)
    # if read_byte == b'':
    #     ser.close()
    #     print(str(read_byte) + "cannot read")
    #     return self.read_egram()
    # egram_data = struct.unpack("<dd", read_byte)

    # if 0 < egram_data[0] < 1 and 0 < egram_data[1] < 1:
        # proper_data = true
        # ATR_data.append(egram_data[0])

# Total 16 bytes. dd corresponds to ATR_SIGNAL(8), VENT_SIGNAL(8)
#

# if the user hits show ATR_SIGNAL button, then the plot shows atrium signal
# if the user hits stop, the plot should stop
# if the user hits show VENT_SIGNAL button, then plot the ventrical signal
