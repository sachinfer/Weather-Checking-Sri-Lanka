from utils.weather_api import fetch_weather_data

def main():
    api_key = "your_openweathermap_api_key"  # Replace with your API key
    city = "Colombo"
    weather_data = fetch_weather_data(api_key, city)
    
    # Display weather information
    print(f"Weather in {city}:")
    print(f"Temperature: {weather_data['main']['temp']}°C")
    print(f"Humidity: {weather_data['main']['humidity']}%")
    print(f"Weather: {weather_data['weather'][0]['description']}")

if __name__ == "__main__":
    main()