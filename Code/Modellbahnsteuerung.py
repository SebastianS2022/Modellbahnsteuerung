from gpiozero import LED
from time import sleep
from signal import pause

led = LED(14)

led.blink(2,1,5)

# while True:
#         led.on()
#         sleep(0.5)
#         led.off()
#         sleep(0.5)