#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import serial
import time
import csv
import queue
import os
import binascii

from tabulate import tabulate

ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

# Constructor - Data Queue used to store all the data received from Serial Port
dataQueue = queue.Queue()

# Put the data frame received from serial port into the 'dataQueue'
def data_frame_enqueue(dataFrame):
    for i in range(len(dataFrame)):
        # Agregar un dato de 'dataFrame' en la lista de 'dataQueue' 
        dataQueue.put_nowait(dataFrame[i])

def analyse_data_Queue():
    while True:
        # if the data stored in queue are less than one frame(9 bytes), 
        # stop analysing
        if dataQueue.qsize() < 9:
            return False

        # Parse and print data frame
        Frame_header_1 = dataQueue.get_nowait()
        if Frame_header_1 == 0x59:
            Frame_header_2 = dataQueue.get_nowait()
            if Frame_header_2 == 0x59:
                Dist_L = dataQueue.get_nowait()
                Dist_H = dataQueue.get_nowait()
                Strength_L = dataQueue.get_nowait()
                Strength_H = dataQueue.get_nowait()
                Temp_L = dataQueue.get_nowait()
                Temp_H = dataQueue.get_nowait()
                Checksum = dataQueue.get_nowait()

                print(tabulate([[
                        Frame_header_1, 
                        Frame_header_2, 
                        Dist_L, 
                        Dist_H, 
                        Strength_L, 
                        Strength_H, 
                        Temp_L,
                        Temp_H, 
                        Checksum]],
                    headers=[
                        'Header1',
                        'Header2', 
                        'Dist_L', 
                        'Dist_H',
                        'Strength_L', 
                        'Strength_H', 
                        'Temp_L', 
                        'Temp_H',
                        'Checksum']))
            else:
                continue
        else:
            continue

def analyse_data_Queue2():
    while True:
        # if the data stored in queue are less than one frame(9 bytes), 
        # stop analysing
        if dataQueue.qsize() < 7:
            return False

        # Parse and print data frame
        Frame_header_1 = dataQueue.get_nowait()
        if Frame_header_1 == 0x59:
            byte1 = dataQueue.get_nowait()
            byte2 = dataQueue.get_nowait()
            byte3 = dataQueue.get_nowait()
            byte4 = dataQueue.get_nowait()
            byte5 = dataQueue.get_nowait()
            byte6 = dataQueue.get_nowait()
            Checksum2 = dataQueue.get_nowait()

            print(tabulate([[
                    byte1, 
                    byte2, 
                    byte3, 
                    byte4, 
                    byte5, 
                    byte6, 
                    Checksum2]],
                headers=[
                    'Resp1',
                    'Resp2', 
                    'Resp3', 
                    'Resp4',
                    'Resp5', 
                    'Resp6', 
                    'Checksum2']))
        else:
            continue

def get_data():
    # Get the number of bytes received from serialport
    numBytesRead = ser.inWaiting()
    #print(numBytesRead)
    # Read data frame from serial port
    raw_data = ser.read(numBytesRead)
    # Put new data frame into 'dataQueue'
    data_frame_enqueue(raw_data)
    # Analyse and print data
    analyse_data_Queue()

def get_firmware():
    # Byte 0
    # Head: frame header(0x5A)
    HEAD=0x5A
    # Byte 1
    # Len: the total length of the frame(include Head and Checksum,unit: byte) 
    LEN=0x04
    # Byte 2
    # ID: identifier code of command
    ID=0x02
    # Byte 3 - N-2
    # Data: data segment. Little endian format
    DATA=0x5F
    # Byte N-1
    # Checksum: sum of all bytes from Head to payload. Lower 8 bits
    Checksum=None
    ser.write(serial.to_bytes([HEAD, LEN, ID, DATA]))

    # Get the number of bytes received from serialport
    numBytesRead2 = ser.inWaiting()
    # Read data frame from serial port
    raw_data2 = ser.read(numBytesRead2)
    # Put new data frame into 'dataQueue'
    data_frame_enqueue(raw_data2)
    # Analyse and print data
    analyse_data_Queue2()

# Read Sensor
if __name__ == "__main__":
    while True:
        get_firmware()

    #while True:
    #    get_data()
