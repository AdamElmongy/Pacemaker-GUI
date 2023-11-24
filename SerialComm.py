import serial
import struct

class SerialComm:
    def __init__(self,data, parameters):
        self.__COM = "COM3"
        self.__baudrate = 115200
        self.__endian = "<"  # little endian
        self.__data = data
        self.__parameters = parameters
        # see endian string format here: https://docs.python.org/3/library/struct.html
        self.send()

    def send(self):
        SYNC = 0x16
        FN_CODE = 0x55
        self.__data = self.generate_data()
        self.__data.insert(0, SYNC)
        self.__data.insert(1, FN_CODE)

        format_str = self.generate_format()

        print(format_str)
        packed_data = struct.pack(format_str, *self.__data)

        # ser = serial.Serial(self.__COM, self.__baudrate)  # open serial port
        # ser.write(packed_data)
        # ser.close()

    def generate_format(self):
        endian = self.__endian
        format_str = "BBBBffffHHBBBBBB"
        string = endian + format_str
        return string

    def generate_data(self):
        param_order = ["Mode","LRL", "URL","VAmp","AAmp",
                       "VPW","APW","VRP","ARP","Reaction Time",
                       "Response Factor","Recovery Time","MSR",
                       "Rate Smoothing","Activity Threshold"]
        d = 0
        full_data = [0] * len(param_order)
        for index in range(len(full_data)):
            for j in self.__parameters:
                if param_order[index] == j:
                    full_data[index] = self.__data[d]
                    d += 1
                    break
        return full_data


