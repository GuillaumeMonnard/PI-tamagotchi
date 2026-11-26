from gpiozero import Button
from signal import pause

btn_eat = Button(4)
btn_play = Button(17)
btn_sleep = Button(22)

def button_test_press():
  print("Button pressed")

def button_test_release():
  print("Button released")

btn_eat.when_pressed = button_test_press
btn_eat.when_released = button_test_release

btn_play.when_pressed = button_test_press
btn_play.when_released = button_test_release

btn_sleep.when_pressed = button_test_press
btn_sleep.when_released = button_test_release

pause()