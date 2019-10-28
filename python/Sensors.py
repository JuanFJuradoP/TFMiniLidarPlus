#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import serial
import time
import csv
import queue

from tabulate import tabulate

ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

# Data Queue used to store all the data received from Serial Port
dataQueue = queue.Queue()

# Put the data frame received from serial port into the 'dataQueue'
def dataFrameEnqueue(dataFrame):
    for i in range(len(dataFrame)):
        dataQueue.put_nowait(dataFrame[i])

def analyseDataQueue():
    while True:
        # if the data stored in queue are less than one frame(9 bytes), stop analysing
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

                print(tabulate(
                    [[Frame_header_1, Frame_header_2, Dist_L, Dist_H, Strength_L, Strength_H, Temp_L, Temp_H, Checksum]],
                    headers=['Header1', 'Header2', 'Dist_L', 'Dist_H', 'Strength_L', 'Strength_H', 'Temp_L', 'Temp_H',
                            'Checksum']))
            else:
                continue
        else:
            continue

def getData():
    # Get the number of bytes received from serialport
    numBytesRead = ser.inWaiting()
    # Read data frame from serial port
    raw_data = ser.read(numBytesRead)
    # Put new data frame into 'dataQueue'
    dataFrameEnqueue(raw_data)
    # Analyse and print data
    analyseDataQueue()

# Read Sensor
if __name__ == "__main__":
    while True:
        getData()