import neopixel
import time

from .utils import wait_for_sleep_time_cm

MIN_REPEATS = 1
CHANGE_CHANCE = 0.1
COLORS = [
    (148, 0, 211),
    (75, 0, 130),
    (0, 0, 255),
    (0, 255, 0),
    (255, 255, 0),
    (255, 127, 0),
    (255, 0, 0)
]


def animate(np: neopixel.NeoPixel) -> None:
    len_colors = len(COLORS)
    len_leds = len(np)
    sleep_time_ns = 10**8
    for i in range(len_colors):
        with wait_for_sleep_time_cm(sleep_time_ns):
            for j in range(len_leds):
                np[j] = COLORS[(i + j) % len_colors]
            np.write()
