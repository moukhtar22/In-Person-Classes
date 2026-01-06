from gpiozero import LED
from time import sleep

led = LED(17)  # GPIO17

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)

