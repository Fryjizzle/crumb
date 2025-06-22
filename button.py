from gpiozero import Button
import os
from signal import pause

# GPIO21 (Pin 40)
button = Button(21)  # Let gpiozero handle default pull behavior internally

def on_button_press():
    print("🔘 Button pressed — playing Dune quote...")
    os.system('mpg123 /home/crumb/crumb/sounds/dune_quote.mp3')

print("🖲️ Crumb's button is armed and waiting.")
button.when_pressed = on_button_press

pause()  # Keeps the program running in the background

