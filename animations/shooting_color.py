import time
import random
import neopixel
from .utils import write_colors, wait_for_sleep_time_cm

MIN_REPEATS = 1
CHANGE_CHANCE = 1.0
THRESHOLD = 0.03
DEFAULT_WHITE_BRIGHTNESS = 30
DEFAULT_COLOR = (DEFAULT_WHITE_BRIGHTNESS, DEFAULT_WHITE_BRIGHTNESS, DEFAULT_WHITE_BRIGHTNESS)
COLORS = [
    (DEFAULT_WHITE_BRIGHTNESS, DEFAULT_WHITE_BRIGHTNESS, 255),
    (DEFAULT_WHITE_BRIGHTNESS, 255, DEFAULT_WHITE_BRIGHTNESS),
    (255, DEFAULT_WHITE_BRIGHTNESS, DEFAULT_WHITE_BRIGHTNESS),
    (DEFAULT_WHITE_BRIGHTNESS, 255, 255),
    (255, DEFAULT_WHITE_BRIGHTNESS, 255),
    (255, 255, DEFAULT_WHITE_BRIGHTNESS)
]


def animate(np: neopixel.NeoPixel) -> None:
    current_colors = [DEFAULT_COLOR for _ in range(len(np))]

    sleep_time_ns = 20*10**6
    for i in range(1000):
        with wait_for_sleep_time_cm(sleep_time_ns):
            if random.random() < THRESHOLD:
                new_pixel = random.choice(COLORS)
            else:
                current_pixel = current_colors[0]
                if max(current_pixel) > DEFAULT_WHITE_BRIGHTNESS:
                    new_pixel = (max(current_pixel[0]-10, DEFAULT_WHITE_BRIGHTNESS),
                                 max(current_pixel[1]-10, DEFAULT_WHITE_BRIGHTNESS),
                                 max(current_pixel[2]-10, DEFAULT_WHITE_BRIGHTNESS))
                else:
                    new_pixel = DEFAULT_COLOR

            current_colors = [new_pixel] + current_colors[:-1]

            write_colors(np, current_colors)
