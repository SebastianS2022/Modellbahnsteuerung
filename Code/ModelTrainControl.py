from gpiozero import LED
from gpiozero import DigitalInputDevice
#from gpiozero import DigitalOutputDevice

from TrackSwitch import *
from GpioMapping import *

from time import sleep
from signal import pause

# led = LED(14)
switch = DigitalInputDevice(18, True)

# gpio14 = DigitalOutputDevice(14)
print("Press Enter to continue")
print("Button state: " + str(switch.value))
input()

trackSwitch = TrackSwitch("tw1r")
print("Button state: " + str(switch.value))

switch.wait_for_inactive(None) 
print("Button is pressed") 
trackSwitch.switch()

# while True: 
#     if switch.is_pressed: 
#         print("Button is pressed") 
#         gpio14.blink(1,0.1,1,False)
#         break

# while True: 
#     if switch.is_pressed: 
#         led.on()
#         print("Button is pressed") 
#         sleep(1)
#         led.off()
#     else:
#         print("Button is not pressed")
#         sleep(1)

# led.blink(2,1,5,False)
print("Switching track switch terminated")

# while True:
#         led.on()
#         sleep(0.5)
#         led.off()
#         sleep(0.5)