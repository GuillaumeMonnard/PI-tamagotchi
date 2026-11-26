from gpiozero import Button
from signal import pause

manger = Button(4)

def button_test_press():
  print("Button pressed")

def button_test_release():
  print("Button released")

manger.when_pressed = button_test_press
manger.when_released = button_test_release

pause()