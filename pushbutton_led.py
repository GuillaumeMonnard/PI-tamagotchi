from gpiozero import Button, LED
from signal import pause
from time import sleep

led = LED(14)
button = Button(4)

button.when_pressed = led.on

button.when_released = led.off

pause()