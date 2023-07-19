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

def decode_packet(packet_bytes):
    field_labels = [
        "Destination Address",
        "Source Address",
        "OpCode",
        "Info Field Length",
        "Minutes",
        "Hours",
        "Primary Equipment",
        "Secondary Equipment",
        "Heat Source",
        "Desired Pool Temp",
        "Desired Spa Temp",
        "Switch State",
        "Byte Use Enable",
        "Hi Byte of Checksum",
        "Lo Byte of Checksum"
    ]

    for byte, label in zip(packet_bytes, field_labels):
        print(f"Byte: 0x{byte:02X}, {label}: {byte}")


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
            
            remaining_bytes = ser.read(27)
            print("Remaining bytes:", remaining_bytes.hex())
            decode_packet(remaining_bytes)
            
            # Reset the buffer for the next iteration
            buffer = bytearray()
        else:
            print("Timeout: Synchronization byte not found.")
            break
finally:
    # Close the serial port
    ser.close()
