from random import randint
import time
# SETUP

# minimum time in seconds between two accepted button presses
COOLDOWN = 15

# time in seconds between two automatic gauge decreases
TICK_INTERVAL = 10

# a gauge below this value counts as low (used to compute the pet state)
LOW_THRESHOLD = 33

# gauges, each between GAUGE_MIN and GAUGE_MAX
GAUGE_MAX = 100
GAUGE_MIN = 0
hunger = randint(50, 100)
mood = randint(50, 100)
energy = randint(50, 100)

# points added to the correponsding gauge when a button is pressed, between EFFECT_MIN and EFFECT_MAX
EFFECT_MIN = randint(15, 30)
EFFECT_MAX = randint(15, 30)

# current time at launch, used to initialize last_tick and last_press
now = time.monotonic()

# value of the last automatic gauge decrease, starts at the current time when the game launches
last_tick = now
# value of the last accepted button press, starts at now - COOLDOWN so the first press is accepted
last_press = now - COOLDOWN
