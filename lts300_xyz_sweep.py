""" Uses Kinesis to control Thorlabs long travel stage in XYZ configuration
"""
import clr
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
import random  # only used for dummy data

from System import String
from System import Decimal
from System.Collections import *

# constants
sys.path.append(r"C:\Program Files\Thorlabs\Kinesis")
serial_x = '45851981'
serial_y = '45851973'
serial_z = '45852301'

# add .net reference and import so python can see .net
clr.AddReference("Thorlabs.MotionControl.Controls")
import Thorlabs.MotionControl.Controls

# print(Thorlabs.MotionControl.Controls.__doc__)

# Add references so Python can see .Net
clr.AddReference("Thorlabs.MotionControl.DeviceManagerCLI")
clr.AddReference("Thorlabs.MotionControl.GenericMotorCLI")
clr.AddReference("Thorlabs.MotionControl.IntegratedStepperMotorsCLI")
from Thorlabs.MotionControl.DeviceManagerCLI import *
# from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.IntegratedStepperMotorsCLI import *


def avg(a):
    return sum(a) / len(a)


def print_positions():
    print('position (x,y,z): ', device_x.Position, device_y.Position, device_z.Position)
    return


def initialize_device(serial):
    device = Thorlabs.MotionControl.IntegratedStepperMotorsCLI.LongTravelStage.CreateLongTravelStage(serial)
    device.Connect(serial)
    motorSettings = device.GetMotorConfiguration(serial)
    # print(motorSettings)
    deviceInfo = device.GetDeviceInfo()
    print(deviceInfo.Name, '  ', deviceInfo.SerialNumber)
    return device


device_list_result = DeviceManagerCLI.BuildDeviceList()
# print(device_list_result)
# setup devices
device_x = initialize_device(serial_x)
device_y = initialize_device(serial_y)
device_z = initialize_device(serial_z)

time.sleep(0.5)

# move to starting position
device_x.MoveTo(Decimal(220), 60000)
device_z.MoveTo(Decimal(224), 60000)
device_y.MoveTo(Decimal(20), 60000)
print_positions()
time.sleep(1)

# sweep up and take data
y_pos = []
voltage = []
endpos = 200
# polling allows us to determin position on the fly
device_y.StartPolling(50)
device_y.MoveTo(Decimal(endpos + 5), 0)
yp = 0
time.sleep(0.5)
while yp < endpos:
    # take data from another instrument
    x = random.random()
    y_dec = device_y.Position
    yp = float(str(y_dec))  # convert system decimal to float
    print(yp, x)
    y_pos.append(yp)
    voltage.append(x)
    time.sleep(0.05)  # delay will determin number of datapoints
device_y.StopPolling()

y_pos = np.array(y_pos)
voltage = np.array(voltage)
time.sleep(2)

# go back to the start
device_y.MoveTo(Decimal(20), 0)

plt.plot(y_pos, voltage)
plt.xlabel('position (mm)')
plt.ylabel('voltage (volts)')
plt.show()

plt.plot(y_pos)  # plot to check position samples are linear
plt.show()
