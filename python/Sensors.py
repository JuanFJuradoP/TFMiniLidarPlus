#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import serial
import time
import csv

from tabulate import tabulate

ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)



def getData():
    raw_data = ser.read(9)
    # Here I get the following 9 Bytes

    # here I parse the data according to your description in this table 7
    Frame_header_1 = raw_data[0]
    Frame_header_2 = raw_data[1]
    Dist_L = raw_data[2]
    Dist_H = raw_data[3]
    Strength_L = raw_data[4]
    Strength_H = raw_data[5]
    Temp_L = raw_data[6]
    Temp_H = raw_data[7]
    Checksum = raw_data[8]

    # Here I print the data and I think that are not correspond to the table data
    print(tabulate([[Frame_header_1, Frame_header_2, Dist_L, Dist_H, 
        Strength_L, Strength_H, Temp_L, Temp_H, Checksum]], 
        headers=['Header1', 'Header2', 'Dist_L', 'Dist_H', 'Strength_L', 
            'Strength_H', 'Temp_L', 'Temp_H', 'Checksum']))

            # Dist_H is OK (I am moving my hand to detect)

            # But Checksum is not changing!

            # Thanks :)


while True:
    #writeData()
    # code here

    getData()

















#start_time = time.time()
#print("--- %s seconds ---" % (time.time() - start_time))

# Set up Parameters
# data = []

# command="\x5A\x04\x01"

"""
#ser.write(serial.to_bytes([0x5A,0x04,0x01,0x5F]))

cw = b'0x5A,0x04,0x01'
ser.write(serial.to_bytes(cw))

uplink_frame = ser.read(7)
x_out = ord(uplink_frame[0])

print(uplink_frame)
print(x_out)

# Binary     Hex  Octal  Unsigned   Signed  ASCII
# 0101 1010  5A   132    90         90      Z
"""