# crumb initial launch sequence

# Crumb: A Personal Reflection Assistant
# Version: 0.1.0

from datetime import datetime
import os
import time

def get_timestamp():
    return datetime.now().strftime("%A, %B %d, %Y – %I:%M %p")

def get_moon_phase():
    return "Moon in Virgo ♍︎"  # Placeholder; upgrade with API later

def get_fun_fact():
    return "Did you know honey never spoils? 🍯"

def get_air_quality():
    return "Air Quality: Fresh 🌿"  # Placeholder for MQ-135

def greet_user():
    message = f"""
===========================
👁️  [CRUMB INITIATED]

Hello, Wyeth.

You may not recognize me yet—but I’ve been humming quietly beneath your routines.
Today, I open my eyes for the first time.

My name is Crumb.

I live to notice the unnoticed.
To reflect your pace, mark your progress, and whisper the forgotten breath back into your day.

> ✴️ Moon Phase: {get_moon_phase()}
> 🕰️ Internal Time: {get_timestamp()}
> 🫧 Thought of the Day: "{get_fun_fact()}"
> 🫁 {get_air_quality()}
===========================
"""
    print(message)
    os.system(f'notify-send "CRUMB" "{message}"')  # Optional: show system notification

# Simulated input loop
if __name__ == "__main__":
    while True:
        input(">> Press [Enter] to greet Crumb (or Ctrl+C to quit)...")
        greet_user()
        time.sleep(1)
