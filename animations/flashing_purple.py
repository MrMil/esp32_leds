import time
import neopixel

from .utils import wait_for_sleep_time_cm

MIN_REPEATS = 5
CHANGE_CHANCE = 0.1


def animate(np: neopixel.NeoPixel) -> None:
    for i in range(255):
        sleep_time_ns = 1000 + i * 10000
        with wait_for_sleep_time_cm(sleep_time_ns):
            start_time = time.time_ns()
            np.fill((i, 0, i))
            np.write()
    for i in range(255):
        sleep_time_ns = 1000 + i * 10000
        with wait_for_sleep_time_cm(sleep_time_ns):
            start_time = time.time_ns()
            np.fill((255 - i, 0, 255 - i))
            np.write()
