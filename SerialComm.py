import serial
import struct
import time
from utils.PacemakerDetector import check_usb_device
from tkinter import messagebox

class SerialComm:
    def __init__(self,data, parameters):
        self.__COM = "COM3"
        self.__baudrate = 115200
        self.__endian = "<"  # little endian
        self.__data = data
        self.__parameters = parameters
        self.__SYNCED = 0x16
        # see endian string format here: https://docs.python.org/3/library/struct.html
        self.send()


    def send(self):
        SYNC = 0x16
        GO_AHEAD = 0x55  # (false) this means do not set the simulink model parameters yet, check them first
        self.__data = self.generate_data()
        self.__data.insert(0, SYNC)
        self.__data.insert(1, GO_AHEAD)

        format_str = self.generate_format()
        data_send = self.__data
        print(format_str, self.__data)
        packed_data = struct.pack(format_str, *data_send)

        # if (check_usb_device()):
        ser = serial.Serial(self.__COM, self.__baudrate, timeout=1)  # open serial port
        ser.reset_input_buffer()
        ser.reset_output_buffer()
        ser.write(packed_data)
        ser.close()
        print("sent")

        # check that the parameters sent properly
        # First read back the data that was sent from simulink
        matched = self.check_param(time.time())

        time.sleep(3)
        ser = serial.Serial(self.__COM, self.__baudrate, timeout=1)  # open serial port
        ser.reset_input_buffer()
        ser.reset_output_buffer()
        ser.write(packed_data)
        ser.close()
        matched = self.check_param(time.time())
        print("check complete" + str(matched))
        # If the data from simulink matches the data that was originally sent then set GO_AHEAD to true (0x22)
        if matched == True:
            GO_AHEAD = 0x22  # True
            self.__data[1] = GO_AHEAD
            packed_data_checked = struct.pack(format_str, *self.__data)
            ser = serial.Serial(self.__COM, self.__baudrate)  # open serial port
            ser.write(packed_data_checked)
            ser.close()
            # display on GUI that sending was successful
        else:
            GO_AHEAD = 0x55
            # display to the user that sending failed

    def check_param(self, time_called):
        print("checking parameters")
        start_time = time_called
        ser = serial.Serial("COM3", 115200, timeout=1)  # open serial port
        compare_list = self.__data
        print(compare_list)
        success = False
        while success == False:
            matched = True
            ser.reset_input_buffer()
            read_byte = ser.read(27)
            if read_byte == b'':
                ser.close()
                print(str(read_byte) + "cannot read")
                return self.check_param(start_time)

            retrieved_data = struct.unpack("<BBBffffHHBBBB", read_byte)
            print(retrieved_data)

            for i in range(len(retrieved_data)):
                if retrieved_data[i] != compare_list[i+2]:
                    if (abs(retrieved_data[i] - compare_list[i + 2])) > 0.01:
                        print(retrieved_data[i], compare_list[i+2])
                        print(type(retrieved_data[i]), type(compare_list[i + 2]))
                        matched = False
                        break

            if matched == True:
                success = True

            if (time.time() - start_time) > 5:
                print("Data did not match")
                matched = False
                break

        ser.close()
        return matched

        # else: 
        #     messagebox.showerror("Error", "Can't configure pacemaker because no device is detected.")

    def generate_format(self):
        endian = self.__endian
        format_str = "BBBffffHHBBBB"
        string = endian + "BB" + format_str
        return string

    def generate_data(self):
        param_order = ["Mode","LRL", "URL","VAmp","AAmp",
                       "VPW","APW","VRP","ARP","Reaction Time",
                       "Response Factor","Recovery Time","MSR"]
        d = 0
        full_data = [0] * len(param_order)
        for index in range(len(full_data)):
            for j in self.__parameters:
                if param_order[index] == j:
                    full_data[index] = self.__data[d]
                    d += 1
                    break
        return full_data





