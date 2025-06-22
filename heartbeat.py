import time
import psutil
from gpiozero import PWMLED

def get_heartbeat_interval():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    load = (cpu + ram) / 2

    bpm = 40 + (load / 100) * 120  # Range: 40–160 BPM
    return 60.0 / bpm  # Interval in seconds

def start_heartbeat():
    led = PWMLED(17)
    print("💓 Adaptive Heartbeat Initialized")

    while True:
        interval = get_heartbeat_interval()

        # LUB — Stronger, longer
        led.value = 1.0
        time.sleep(0.07)
        led.value = 0
        time.sleep(0.1)

        # DUB — Softer, quicker
        led.value = 0.5
        time.sleep(0.04)
        led.value = 0

        rest_time = max(interval - 0.21, 0.1)
        time.sleep(rest_time)

