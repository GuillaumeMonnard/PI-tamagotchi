from gpiozero import Button
from signal import pause

btn_eat = Button(4, bounce_time=0.05)
btn_play = Button(17, bounce_time=0.05)
btn_sleep = Button(22, bounce_time=0.05)

# btn_eat test
def btn_eat_press():
  print("eat")

def btn_play_press():
  print("play")

def btn_sleep_press():
  print("sleep")

btn_eat.when_pressed = btn_eat_press

btn_play.when_pressed = btn_play_press

btn_sleep.when_pressed = btn_sleep_press

pause()