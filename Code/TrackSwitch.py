from gpiozero import DigitalOutputDevice
from GpioMapping import *

class TrackSwitch(DigitalOutputDevice):
    # trackSwitchName = ""
    # trackSwitchGpio = 0

    def __init__(self, name):
        self.trackSwitchName = name
        self.trackSwitchGpio = DigitalOutputDevice(gpioDictionary[name])

    def __del__(self):
        print("Destructor called for " + self.trackSwitchName)

    def switch(self):
        print("Track switch invoked for " + self.trackSwitchName + ": GPIO " + str(gpioDictionary[self.trackSwitchName])) 
        self.trackSwitchGpio.blink(1,0.1,1,False)

