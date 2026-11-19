from gpiozero import Button, LED, TonalBuzzer
from signal import pause
from time import sleep

led = LED(14)
button = Button(4)
buzzer = TonalBuzzer(17)

def press():
  led.on()
  buzzer.play("A4")

def release():
  led.off()
  buzzer.stop()

button.when_pressed = press
button.when_released = release

pause()