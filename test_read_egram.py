import serial
import struct
import time
import matplotlib.pyplot as plt

def read_egram(start_time):
    start = start_time
    success = False
    ser = serial.Serial("COM3", 115200, timeout=1)  # open serial port
    while success == False:
        ser.reset_input_buffer()
        read_byte = ser.read(8)
        if read_byte == b'':
            ser.close()
            print(str(read_byte) + "cannot read")
            return read_egram(start)

        retrieved_data = struct.unpack("<d", read_byte)
        if 0.5 < retrieved_data[0] < 2:
            data_array.append(retrieved_data[0])
            time_array.append(time.time()-start)
            print(retrieved_data[0])
            ser.close()
            initiate_egram_sending()
            ser = serial.Serial("COM3", 115200, timeout=1)  # open serial port
        # else:
        #     print("data is no good")
        if time.time()- start > 30:
            print("timed out")
            break
def initiate_egram_sending():
    SYNC = 0x33
    data = [0]*29
    data[0] = SYNC
    str = "<"
    for i in range(len(data)):
        str = str+"B"
    print(str)
    packed_data = struct.pack(str, *data)
    ser = serial.Serial("COM3", 115200)  # open serial port
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    ser.write(packed_data)
    ser.close()
    print("sent")


ser = serial.Serial("COM3", 115200, timeout=1)  # open serial port
data_array = []
time_array = []
ser.close()

initiate_egram_sending()
read_egram(time.time())
print(data_array)
y = data_array
x = time_array
# for i in range(len(y)):
#     x.append(i)
# # Create the plot
plt.plot(x, y)

# Customize the plot (optional)
plt.title('X-Y Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Display the plot
plt.show()