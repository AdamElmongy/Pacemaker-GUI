import serial
import struct

class SerialComm:
    def __init__(self,data):
        self.__COM = "COM3"
        self.__baudrate = 115200
        self.__endian = "<"  # little endian
        self.__data = data
        # see endian string format here: https://docs.python.org/3/library/struct.html
        self.send()

    def send(self):
        SYNC = 16
        FN_CODE = 55
        self.__data.insert(0, SYNC)
        self.__data.insert(1, FN_CODE)

        format_str = self.generate_format()
        print(format_str)
        packed_data = struct.pack(format_str, *self.__data)

        ser = serial.Serial(self.__COM, self.__baudrate)  # open serial port
        ser.write(packed_data)
        ser.close()

    def generate_format(self):
        string = self.__endian
        for i in self.__data:
            if type(i) == float:  # is a single
                string = string + "f"
            elif type(i) == int:
                if i > 255:  # is a uint16
                    string = string + "H"
                else:  # is a uint8
                    string = string+"B"
        return string
