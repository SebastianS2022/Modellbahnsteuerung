from gpiozero import DigitalOutputDevice
from GpioMapping import *

class TrackSwitch(DigitalOutputDevice):
    def __init__(self, name):
        self.trackSwitchName = name
        self.trackSwitchGpio = DigitalOutputDevice(GPIOMapper.gpioOutputDictionary[name])

    def __del__(self):
        print("Destructor called for " + self.trackSwitchName)

    def switch(self):
        print("Track switch invoked for " + self.trackSwitchName + ": GPIO " + str(GPIOMapper.gpioOutputDictionary[self.trackSwitchName])) 
        self.trackSwitchGpio.blink(1,0,1,False)

