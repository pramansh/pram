import requests

# Replace YOUR_API_KEY with the actual API key you obtained from OpenWeatherMap
API_KEY = "YOUR_API_KEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather_data(city_name):
    complete_url = BASE_URL + "appid=" + API_KEY + "&q=" + city_name
    response = requests.get(complete_url)
    return response.json()

def display_weather_data(weather_data):
    if weather_data["cod"] != "404":
        main_data = weather_data["main"]
        temperature = main_data["temp"] - 273.15  # Convert from Kelvin to Celsius
        pressure = main_data["pressure"]
        humidity = main_data["humidity"]

        weather_desc = weather_data["weather"][0]["description"]

        print(f"Temperature: {temperature:.1f}°C")
        print(f"Atmospheric Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Weather Description: {weather_desc.capitalize()}")
    else:
        print("City not found.")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    weather_data = get_weather_data(city_name)
    display_