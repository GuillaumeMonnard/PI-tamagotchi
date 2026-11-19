from gpiozero import Button, LED, TonalBuzzer
from signal import pause
from time import sleep

# Récupération du bon PIN sur le PI pour chaque élément
led = LED(14)
button = Button(4)
buzzer = TonalBuzzer(17)

# Mélodie
MELODY = [("C4", 0.15), ("E4", 0.15), ("G4", 0.15), ("C5", 0.3)]
def play_melody():
  led.on()
  for note, duration in MELODY:
    buzzer.play(note)
    sleep(duration)
  buzzer.stop()
  led.off()


button.when_pressed = play_melody

pause()