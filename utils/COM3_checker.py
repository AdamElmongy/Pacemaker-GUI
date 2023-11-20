# import serial
# import time

# def check_com_port():
#     try:
#         # Try to open COM3 port
#         with serial.Serial('COM3', timeout=1) as ser:
#             print("COM3 is open. A device may be connected.")
#             return True
#     except serial.SerialException:
#         print("COM3 cannot be opened. No device detected.")
#         return False

# def main():
#     while True:
#         check_com_port()
#         time.sleep(2)  # Check every 2 seconds

# if __name__ == "__main__":
#     main()


# import ctypes
# import time

# def list_usb_devices():
#     GUID_DEVINTERFACE_USB_DEVICE = "{A5DCBF10-6530-11D2-901F-00C04FB951ED}"

#     # Set up a device interface data structure
#     device_interface_data = ctypes.create_string_buffer(4096)
#     size = ctypes.c_ulong(ctypes.sizeof(device_interface_data))
#     device_interface_data.value = b'\0'

#     # Get information about all devices with a USB interface
#     devices = []
#     index = 0

#     while True:
#         device_info = ctypes.create_string_buffer(4096)
#         device_info.value = b'\0'

#         dev_handle = ctypes.windll.SetupAPI.SetupDiGetClassDevsW(
#             ctypes.byref(ctypes.c_wchar_p(GUID_DEVINTERFACE_USB_DEVICE)),
#             None,
#             None,
#             0x0012  # DIGCF_DEVICEINTERFACE | DIGCF_PRESENT
#         )

#         success = ctypes.windll.SetupAPI.SetupDiEnumDeviceInterfaces(
#             dev_handle,
#             None,
#             ctypes.byref(ctypes.c_wchar_p(GUID_DEVINTERFACE_USB_DEVICE)),
#             index,
#             ctypes.byref(device_interface_data)
#         )

#         if not success:
#             break

#         ctypes.windll.SetupAPI.SetupDiGetDeviceInterfaceDetailW(
#             dev_handle,
#             ctypes.byref(device_interface_data),
#             ctypes.byref(device_info),
#             ctypes.sizeof(device_info),
#             ctypes.byref(size),
#             None
#         )

#         devices.append(device_info.value)
#         index += 1
# # "FlashInfo.txt"
#     for device_path in devices:
#         print(f"Device Path: {device_path.decode('utf-16le')}")

#     ctypes.windll.kernel32.CloseHandle(dev_handle)

# if __name__ == "__main__":
#     list_usb_devices()

#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         pass


import psutil
import time
import os

def check_file_in_d_drive():
    # Define the file name and path
    file_name = "FlashInfo.txt"
    d_drive_path = "D:\\"

    # Construct the full path
    file_path = os.path.join(d_drive_path, file_name)

    # Check if the file exists
    if os.path.exists(file_path):
        print(f"The file {file_name} exists in the D: drive.")
        return True
    else:
        print(f"The file {file_name} does not exist in the D: drive.")
        return False


def check_usb_device():
    # Get the list of connected devices
    connected_devices = psutil.disk_partitions(all=True)

    # Check if any device is a removable USB device
    for device in connected_devices:
        if 'removable' in device.opts:
            if check_file_in_d_drive(): print("USB Device Detected:", device.device)
            return True
    
    print("No USB Device Detected")
    return False

def main():
    while True:
        check_usb_device()
        # Check every 2 seconds
        time.sleep(2)  

if __name__ == "__main__":
    main()

