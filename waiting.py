from itertools import cycle
import time

_CHARS = '/-\|'
CHARS = iter(cycle(_CHARS))

def wait(n, delay=0.15):
    for _ in range(n):
        for char in _CHARS:
            print(f'\rLoading {char}', end='')
            time.sleep(delay)

def wait_iter(n, delay=0.15):
    for _ in range(n*len(_CHARS)):
        print(f'\rLoading {next(CHARS)}', end='')
        time.sleep(delay)
