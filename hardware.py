from gpiozero import Button
from signal import pause

manger = Button(4)
jouer = Button(17)
dormir = Button(22)

def button_test_press():
  print("Button pressed")

def button_test_release():
  print("Button released")

manger.when_pressed = button_test_press
manger.when_released = button_test_release

jouer.when_pressed = button_test_press
jouer.when_released = button_test_release

dormir.when_pressed = button_test_press
dormir.when_released = button_test_release

pause()