import time
import machine
import neopixel
import random
import sys

NUM_PIXELS = 60
LED_PIN = 23
ANIMATIONS = [
    'flashing_purple',
    'rainbow',
    'long_rainbow',
    'flash_random_color',
    'shooting_color'
]


def init_leds() -> neopixel.NeoPixel:
    np = neopixel.NeoPixel(machine.Pin(LED_PIN), NUM_PIXELS)
    return np


def loop_random_animation(np: neopixel.NeoPixel) -> None:
    animations = [getattr(__import__(f'animations.{name}'), name) for name in ANIMATIONS]
    while True:
        current_animation = random.choice(animations)
        change = False
        loop_count = 0
        while not change:
            current_animation.animate(np)
            loop_count += 1
            if loop_count >= current_animation.MIN_REPEATS:
                change = random.random() < current_animation.CHANGE_CHANCE


def init_animation(np: neopixel.NeoPixel) -> None:
    for i in range(3):
        print(time.time_ns())
        color = [0, 0, 0]
        color[i] = 255
        np.fill(tuple(color))
        np.write()
        time.sleep(1)


def error_animation(np: neopixel.NeoPixel) -> None:
    try:
        for i in range(3):
            np.fill((255, 0, 0))
            np.write()
            time.sleep(0.5)
            np.fill((0, 0, 0))
            np.write()
            time.sleep(0.5)
    except Exception as e:
        pass


def main() -> None:
    np = init_leds()
    init_animation(np)

    while True:
        try:
            loop_random_animation(np)
        except Exception as e:
            print("An error occurred:", e)
            sys.print_exception(e)
            error_animation(np)
            time.sleep(1)
        np = init_leds()


if __name__ == '__main__':
    main()
