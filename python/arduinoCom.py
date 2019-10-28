#!/usr/bin/python3

import serial
import time


ser = serial.Serial('/dev/ttyACM0', 9600)


# Read and record the data
data =[]                       # empty list to store the data




# Read Sensor
while True:
    data = ser.readline()         # read a byte string
    print(data)
    time.sleep(0.01)            # wait (sleep) 0.1 seconds

    # data.append(flt)           # add to the end of data list
    # time.sleep(0.1)            # wait (sleep) 0.1 seconds





   
    #     string_n = b.decode()  # decode byte string into Unicode  
    # string = string_n.rstrip() # remove \n and \r
    # flt = float(string)        # convert string to float
    # print(flt)
    # data.append(flt)           # add to the end of data list
    # time.sleep(0.1)            # wait (sleep) 0.1 seconds

# # Read Sensor
# while True:    
#     raw_data = ser.read(9)
#     out = ord(raw_data[3])
#     print(out)

#start_time = time.time()
#print("--- %s seconds ---" % (time.time() - start_time))



