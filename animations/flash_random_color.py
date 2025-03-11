import time
import random
import neopixel

from .utils import wait_for_sleep_time_cm

MIN_REPEATS = 5
CHANGE_CHANCE = 0.1
MASKS = [
    (0, 0, 1),
    (0, 1, 0),
    (1, 0, 0),
    (0, 1, 1),
    (1, 0, 1),
    (1, 1, 0)
]


def animate(np: neopixel.NeoPixel) -> None:
    mask = random.choice(MASKS)

    for i in range(255):
        sleep_time_ns = 1000 + i * 10000
        with wait_for_sleep_time_cm(sleep_time_ns):
            np.fill((i*mask[0], i*mask[1], i*mask[2]))
            np.write()

    for i in range(255):
        sleep_time_ns = 1000 + i * 10000
        with wait_for_sleep_time_cm(sleep_time_ns):
            np.fill(((255-i)*mask[0], (255-i)*mask[1], (255-i)*mask[2]))
            np.write()
