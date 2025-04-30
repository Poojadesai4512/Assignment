import requests

def fetch_weather(city, api_key):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        temp = data['main']['temp']
        weather = data['weather'][0]['description']

        print(f"Current weather in {city}:\nTemperature: {temp}°C\nCondition: {weather.capitalize()}")
    except requests.exceptions.HTTPError as e:
        print("HTTP error occurred:", e)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    city = input("Enter city name: ")
    api_key = "your_api_key_here"  # Replace with your actual OpenWeatherMap API key
    fetch_weather(city, api_key)
