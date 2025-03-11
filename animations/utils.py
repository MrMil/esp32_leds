import time
import neopixel
from contextlib import contextmanager


def write_colors(np: neopixel.NeoPixel, colors: list[tuple[int, int, int]]) -> None:
    for i in range(len(np)):
        np[i] = colors[i]
    np.write()


def wait_for_sleep_time(start_time: int, sleep_time_ns: int) -> None:
    while time.time_ns() - start_time < sleep_time_ns:
        pass


@contextmanager
def wait_for_sleep_time_cm(sleep_time_ns: int):
    start_time = time.time_ns()
    yield
    wait_for_sleep_time(start_time, sleep_time_ns)
