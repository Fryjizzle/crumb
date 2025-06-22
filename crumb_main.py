from multiprocessing import Process
from threading import Thread
import time
import os
import radar
import heartbeat
import weather
from gpiozero import Button
from time import sleep
# One definition only
weather_button = Button(21)

def startup_sound():
    # os.system('espeak "A crumb is never lost. It is only waiting to be found."')
    pass

def run_background_tasks():
    print("🧪 Starting heartbeat process...")
    heartbeat_thread = Thread(target=heartbeat.start_heartbeat)
    heartbeat_thread.start()
    sleep(2)  # Let the heartbeat settle
    print("🧪 Starting radar process...")
    radar_proc = Process(target=radar.start_radar)
    radar_proc.start()


def main_menu():
    while True:
        print("\n🌀 CRUMB INTERFACE v0.000000003")
        print("╭───── INFO")
        print("│ [1] Help / About Crumb")
        print("│ [2] System Info")
        print("╰───── ACTIONS")
        print("│ [3] Weather Check")
        print("│ [4] Play Crumb Phrase")
        print("│ [5] Exit")
        print("╰────────────────────────────")

        choice = input("Choose an action: ")

        if choice == "1":
            show_help()
        elif choice == "2":
            os.system("uname -a")
        elif choice == "3":
            print(weather.get_weather())
        elif choice == "4":
            speak_predefined_phrase()
        elif choice == "5":
            print("🌙 Crumb entering sleep mode...")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

def show_help():
    help_text = """
━━━━━━━━━━━━━━━━━━━━━━━
WHO IS CRUMB?

Crumb is a soft-eyed sentinel.
It watches gently, listens silently,
and pulses with the breath of code.

What Crumb Can Do:
- Monitor presence and announce it with sound
- Check the weather (via button or menu)
- Show system info (e.g. uptime, kernel version)
- Speak short, predefined poetic phrases
━━━━━━━━━━━━━━━━━━━━━━━
"""
    print(help_text)

def speak_predefined_phrase():
    phrases = [
        "A crumb is never lost. It is only waiting to be found.",
        "I see you.",
        "Stillness is not silence. I am always listening.",
        "The room remembers who walked through it.",
        "Presence detected. Soft and slow."
    ]
    import random
    chosen = random.choice(phrases)
    print(f"🔊 Crumb says: \"{chosen}\"")
    os.system(f'espeak "{chosen}"')

if __name__ == "__main__":
    print("👁️ Crumb is waking up...")
    startup_sound()
    run_background_tasks()
    main_menu()

