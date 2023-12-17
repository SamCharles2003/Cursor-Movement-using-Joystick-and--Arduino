import time

import serial.tools.list_ports
import pywinauto
import pyautogui

pyautogui.PAUSE = 0.001
# Function to read data from USB port
def read_usb_port(device_name):
    try:
        ports = list(serial.tools.list_ports.comports())
        for port, desc, hwid in ports:
            if device_name in desc:
                ser = serial.Serial(port=port, baudrate=115200, timeout=1, write_timeout=1)
                ser.reset_input_buffer()  # Clear any existing data in the buffer
                print(f"Connected to USB port: {port} ({desc})")
                while True:
                    data = ser.read(ser.in_waiting or 1).decode().strip()  # Read data from USB port
                    if data:
                        string_split(data)
                break
        else:
            print(f"No USB device with name '{device_name}' found.")
    except Exception as e:
        print(f"Error: {e}")

def string_split(data):
    values_list = data.split()
    mouse_control(values_list[0], values_list[1],values_list[2])
    print(values_list)
    data=""

def mouse_control(xaxis_raw, yaxis_raw,button):
    real_xaxis = int(xaxis_raw)
    real_yaxis = int(yaxis_raw)
    pyautogui.moveTo(real_xaxis, real_yaxis)
    if button=='0':
        pyautogui.click()
        time.sleep(0.1)
# Main function
if __name__ == "__main__":
    device_name = "USB-SERIAL CH340"  # Specify the device name
    try:
        read_usb_port(device_name)  # Try reading from USB port with the specified name
    except serial.SerialException:
        print(f"Error: Unable to read data from USB port with name '{device_name}'.")
