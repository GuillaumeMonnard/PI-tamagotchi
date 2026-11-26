from random import randint
import time

# setup
hunger = randint(50,100)
mood = randint(50,100)
energy = randint(50,100)

COOLDOWN = 15
# TICK_INTERVAL = I
# LOW_THRESHOLD = L = 33
# GAUGE_MAX = 100
# GAUGE_MIN = 0

last_tick = time.monotonic()
last_press = time.monotonic() - COOLDOWN

print(last_tick)
print(last_press)
