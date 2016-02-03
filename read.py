import serial
import time
import datetime
import atexit
import re
import os
ser = serial.Serial('COM6', 9600, timeout=0)

filepath = "temperature.data"
f = open(filepath, 'a+') # creates if file does not exist, appends if it does

 
while True:
    try:
        data = ser.readline()
        if data != '':
            timestamp = time.time()
            formatted_timestamp = datetime.datetime.fromtimestamp(timestamp).strftime('%Y%m%d%H%M%S')

            # log the new entry
            print data + ',' + formatted_timestamp + '\n'

            # write the new entry to file
            f.write(data + ',' + formatted_timestamp + '\n')
            

            # commit the file for continuous updates without exiting program
            f.flush()
            os.fsync(f)

        time.sleep(1)
        
    except serial.SerialTimeoutException:
        print('Data could not be read')
        time.sleep(1)

def closeFile():
    f.close()

atexit.register(closeFile)
