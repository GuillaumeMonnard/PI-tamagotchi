from gpiozero import TonalBuzzer
from time import sleep

buzzer = TonalBuzzer(17)

buzzer.play("C5")
sleep(1)
buzzer.stop()
sleep(2)
buzzer.play("F5")
sleep(1)
buzzer.stop()