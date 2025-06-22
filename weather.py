import requests
from gpiozero import Button
from signal import pause
import time

# WeatherAPI key and city
API_KEY = "b606d3bed0cb49e49d4130150251206"
CITY = "Wilmington"
last_weather_time = 0
weather_cache = ""

def get_weather():
    global last_weather_time, weather_cache
    now = time.time()

    if now - last_weather_time > 600:  # Only fetch every 10 minutes
        try:
            url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={CITY}&days=1"
            response = requests.get(url)
            data = response.json()

            # Current conditions
            current_temp = data["current"]["temp_f"]
            condition = data["current"]["condition"]["text"]

            # Forecast summary
            forecast_day = data["forecast"]["forecastday"][0]["day"]
            high = forecast_day["maxtemp_f"]
            low = forecast_day["mintemp_f"]
            summary = forecast_day["condition"]["text"]
            chance_of_rain = forecast_day.get("daily_chance_of_rain", "N/A")
            wind_speed = forecast_day.get("maxwind_mph", "N/A")
            wind_dir = forecast_day.get("maxwind_dir", "N/A")
            uv_index = forecast_day.get("uv", "N/A")
            humidity = forecast_day.get("avghumidity", "N/A")

            # Astro data
            astro = data["forecast"]["forecastday"][0].get("astro", {})
            sunrise = astro.get("sunrise", "N/A")
            sunset = astro.get("sunset", "N/A")

            # Format the forecast string
            weather_cache = (
                f"🌤️ {CITY} Weather\n"
                f"Now: {int(current_temp)}°F, {condition}\n"
                f"High: {int(high)}°F | Low: {int(low)}°F\n"
                f"Forecast: {summary}\n"
                f"💧 Rain chance: {chance_of_rain}%\n"
                f"🌬 Wind: {wind_speed} mph {wind_dir}\n"
                f"🌫 Humidity: {humidity}%\n"
                f"💡 UV Index: {uv_index}\n"
                f"🌅 Sunrise: {sunrise} | 🌇 Sunset: {sunset}"
            )

            last_weather_time = now

        except Exception as e:
            weather_cache = f"Error retrieving weather: {e}"

    return weather_cache

def handle_button_press():
    forecast = get_weather()
    print(f"📡 Weather update:\n{forecast}")
    # TODO: display_on_led(forecast)

# Start listening
print("🌤️ Crumb is watching the skies. Press the button for a forecast.")
if __name__ == "__main__":
    print("🌤️ Crumb is watching the skies. Press the button for a forecast.")
    button = Button(21)
    button.when_pressed = handle_button_press
    pause()
