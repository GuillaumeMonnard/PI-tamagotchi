from gpiozero import Button, LED
from signal import pause

# Récupération du bon PIN sur le PI pour chaque élément
led = LED(14)
button = Button(4)


button.when_pressed = led.on
button.when_released = led.off

pause()