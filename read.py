import serial
import time
import datetime
import atexit
import re
import os
ser = serial.Serial('COM6', 9600, timeout=0)

filepath = "temperature.data"
f = open(filepath, 'a+') # creates if file does not exist, appends if it does

start = time.time()
 
while True:
    try:
        data = ser.readline()
        if data != '':
            data = data.strip()
            now = time.time()
            timestamp = now - start
            #formatted_timestamp = datetime.datetime.fromtimestamp(timestamp).strftime('%Y%m%d%H%M%S')
            
            # log the new entry
            entry = data + ',' + str(timestamp) + '\n'

            # sometimes two readings come in at once - throw these out
            # we expect:
            # ##.## degrees (5 chars)
            # a comma (1 char)
            # yyyymmddHHMMSS (14 chars)
            # a total of 20 chars, and we can allow some room for variance in decimal places
            #if (entry[2] == '.' and entry[5] == ','):
            print entry

            # write the new entry to file
            
            f.write(entry)
            

            # commit the file for continuous updates without exiting program
            f.flush()
            os.fsync(f)
            #else:
               #    print "Skipped entry: " + entry
        time.sleep(1)
        
    except serial.SerialTimeoutException:
        print('Data could not be read')
        time.sleep(1)

def closeFile():
    f.close()

atexit.register(closeFile)
