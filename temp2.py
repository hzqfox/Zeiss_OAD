import os
import serial
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

cwd = os.getcwd()
ser = serial.Serial('/dev/ttyAMA0')

arrayCounter = 0

pressure_log = open(cwd + '/logs/pressure','a')
temperature_log = open(cwd + '/logs/temperature', 'a')

unixtimeArray = []
pressureArray = []
temperatureArray = []

#create a figure with two subplots
fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

#define the function for use in matplotlib.animation.funcAnimation
def animate(i):
    #global arrayCounter is to fix: "UnboundLocalError: local variable 'arrayCounter' referenced before assignment"
    global arrayCounter

    #grab preformatted data from serial connection
    data = ser.readline()

    #split data to check which value it is. then log respective value locally and get timestamps
    if data.split(":")[0] == "Pressure":
        timestamp = (time.strftime("%H:%M:%S"))
        pressure_log.write('{0},{1}\n'.format(timestamp, data.split(":")[1]))
        unixtime = time.mktime(time.localtime())
        unixtimeArray.append(float(unixtime))
        pressureArray.append(float(data.split(":")[1].rstrip()))

        #increment arrayCounter to keep the subplots from exceeding 30 displayed values at a time
        arrayCounter=arrayCounter+1
        if(arrayCounter>29):
            unixtimeArray.pop(0)
            pressureArray.pop(0)
    if data.split(":")[0] == "Temperature":
        timestamp = (time.strftime("%H:%M:%S"))
        pressure_log.write('{0},{1}\n'.format(timestamp, data.split(":")[1]))
        unixtime = time.mktime(time.localtime())
        unixtimeArray.append(float(unixtime))
        temperatureArray.append(float(data.split(":")[1].rstrip()))
        arrayCounter=arrayCounter+1
        if(arrayCounter>29):
            unixtimeArray.pop(0)
            temperatureArray.pop(0)

    #populate variables for display in the subplots
    xar = unixtimeArray
    yar = pressureArray
    zar = temperatureArray
    ax1.clear()
    ax1.plot(xar,yar)
    ax2.clear()
    ax2.plot(xar,zar)

while True:
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()
