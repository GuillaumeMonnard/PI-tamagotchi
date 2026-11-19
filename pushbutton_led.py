from gpiozero import Button, LED, TonalBuzzer, PWMOutputDevice
from signal import pause
from time import sleep

# Récupération du bon PIN sur le PI pour chaque élément
led = LED(14)
button = Button(4)

VOLUME = 0.1
FREQUENCE = 880

def play_note():
  led.on()
  buzzer.frequency = FREQUENCE
  buzzer.value = VOLUME *0.5
  sleep(1)
  buzzer.value = 0
  led.off()

button.when_pressed = play_note

pause()