from gpiozero import DistanceSensor, Button
from time import time, sleep
import os
import random
import pathlib

print("📡 Playing startup sound...")
os.system('mpg123 /home/crumb/crumb/sounds/r2d2.mp3')

# === SETUP ===

# Sensors
sensor = DistanceSensor(echo=24, trigger=23, max_distance=2.0)
button = Button(21)

# Sounds
sound_folder = "/home/crumb/crumb/sounds"
sound_files = list(pathlib.Path(sound_folder).glob("*.mp3"))
button_sound = "/home/crumb/crumb/sounds/dune_quote.mp3"

# State
last_proximity_time = 0
proximity_cooldown = 5  # seconds

print("🧠 Crumb is alive (v0.0000000000001)")

# === MAIN LOOP ===
try:
    while True:
        distance = sensor.distance * 100  # in cm

        # 👁️ Proximity Detected
        if distance < 30:
            now = time()
            if now - last_proximity_time > proximity_cooldown:
                if sound_files:
                    chosen = random.choice(sound_files)
                    print(f"👁️ Presence at {distance:.1f} cm — Playing {chosen.name}")
                    os.system(f'mpg123 "{chosen}"')
                    last_proximity_time = now

        # 🔘 Button Press
        if button.is_pressed:
            print("🔘 Button pressed — playing response.")
            os.system(f'mpg123 "{button_sound}"')
            sleep(0.5)  # debounce

        sleep(0.1)

except KeyboardInterrupt:
    print("\n🛑 Crumb shutting down.")

