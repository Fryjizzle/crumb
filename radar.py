from gpiozero import DistanceSensor
from time import sleep
import os
import random
import pathlib

def run_radar():
    print("👁️ Crumb’s radar is scanning...")
    sleep(3)  # ✅ allow GPIO pins to stabilize
    sensor = DistanceSensor(echo=24, trigger=23, max_distance=2.0)
    sound_folder = "/home/crumb/crumb/sounds"
    sound_files = list(pathlib.Path(sound_folder).glob("*.mp3"))



    while True:
        distance = sensor.distance * 100
        if distance < 30:
            if sound_files:
                chosen = random.choice(sound_files)
                print(f"👁️ Presence at {distance:.1f} cm — Playing {chosen.name}")
                os.system(f'mpg123 "{chosen}"')
                sleep(5)
        sleep(0.1)

def start_radar():
    run_radar()


# Only run if executed directly (not when imported)
if __name__ == "__main__":
    run_radar()

