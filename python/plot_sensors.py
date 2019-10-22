#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import serial
import time
import csv

ser = serial.Serial('/dev/ttyUSB0', 115200)

plt.ion() # set plot to animated

ydata = [0] * 50
ax1=plt.axes()

# make plot
line, = plt.plot(ydata)
plt.ylim([10,40]) # set the y-range to 10 to 40

"""
# Set up Parameters
data = []
#command="\x5A\x04\x01"
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


# Read Sensor and start data collection
while True:    
    raw_data = ser.read(9)
    out = ord(raw_data[3])
    #print(out)
    ydata.append(out)
    del ydata[0]
    line.set_xdata(np.arange(len(ydata)))
    line.set_ydata(ydata) # update the data
    plt.draw() # update the plot[/python]



#start_time = time.time()
#print("--- %s seconds ---" % (time.time() - start_time))





