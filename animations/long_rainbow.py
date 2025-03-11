import neopixel

from .utils import wait_for_sleep_time_cm, write_colors

MIN_REPEATS = 1
CHANGE_CHANCE = 0.5
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
    colors = []
    for i in range(len_colors):
        colors += [COLORS[i]]*len_leds
    colors += [COLORS[0]]*len_leds
    sleep_time_ns = 50*10**6
    for i in range(len_colors):
        for j in range(len_leds):
            with wait_for_sleep_time_cm(sleep_time_ns):
                write_colors(np, colors[((i*len_leds)+j):(((i+1)*len_leds)+j)])
