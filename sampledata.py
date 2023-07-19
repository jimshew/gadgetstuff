#!/bin/env python3

import serial

# Open the serial port
ser = serial.Serial('/dev/ttyUSB0')

try:
    data = ser.read(500)
    file_path = "sample.bin"
    
    with open(file_path, "wb") as file:
        file.write(data)
    
    print(f"saved {len(data)} bytes to '{file_path}'.")
except Exception as e:
    print("Error:", str(e))

finally:
    # Close the serial port
    ser.close()

