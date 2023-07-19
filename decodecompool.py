#!/bin/env python3

import serial
import time

def find_sync_byte(ser, timeout):
    sync_bytes = bytearray([0xFF, 0xAA])
    buffer = bytearray()
    
    start_time = time.time()
    
    while True:
        byte = ser.read(1)
        
        if byte:
            buffer += byte
            
            if buffer[-2:] == sync_bytes:
                return buffer
        
        elapsed_time = time.time() - start_time
        if elapsed_time >= timeout:
            return None

def find_OpCode(ser, timeout):
    controller_broadcast = bytearray([0x0F, 0x1B, 0x02])
    buffer = ser.read(3)
    if buffer[:3] == controller_broadcast:
        decode_broadcast(ser.read(19))
    else:
        print("No Opcode 0x02 match")

def decode_broadcast(packet_bytes):
    #field_labels = [
    #    "Destination Address",
    #    "Version",
    field_labels = [
        "Info Field Length",
        "Minutes",
        "Hours",
        "Primary Equipment",
        "Secondary Equipment",
        "Delay/Heat Source",
        "Water Temp",
        "Solar Temp",
	"Spa Water Temp",
	"Spa Solar Temp",
	"Desired Pool Temp",
	"Desired Spa Temp",
	"Air Temp",
	"UNK 1",
	"UNK 2",
        "Equip Status",
        "Product Type",
        "Hi Byte of Checksum",
        "Lo Byte of Checksum"
    ]

    for byte, label in zip(packet_bytes, field_labels):
        readable = byte
        if label.find('Temp') != -1:
            readable = float(byte)*0.25*9.0/5.0+32.0
        if label.find('Version') != -1:
            readable = float(byte)*0.1
        print(f"Byte: 0x{byte:02X}, {label}: {readable}")


# Open the serial port
ser = serial.Serial('/dev/ttyUSB0')

try:
    timeout = 120
    
    # Discard everything before the sync byte
    while True:
        byte = ser.read(1)
        
        if byte and byte[0] == 0xFF:
            next_byte = ser.read(1)
            
            if next_byte and next_byte[0] == 0xAA:
                break
    
    while True:
        sync_data = find_sync_byte(ser, timeout)
        
        if sync_data:
            print("Synchronization byte found:", sync_data.hex())
            
       #     remaining_bytes = ser.read(27)
       #     print("Remaining bytes:", remaining_bytes.hex())
            find_OpCode(ser,timeout)
            
            # Reset the buffer for the next iteration
            buffer = bytearray()
        else:
            print("Timeout: Synchronization byte not found.")
            break
finally:
    # Close the serial port
    ser.close()
