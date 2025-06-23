import requests
def weather(city):
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=7c2985d3a375901fc6f25eb57c13b39b&units=metric"
    try:
        responses=requests.get(url)
        responses.raise_for_status()

        data=responses.json()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        feels_like = data["main"]["feels_like"]
        wind_speed = data["wind"]["speed"]
        pressure = data["main"]["pressure"]


        print(f"Weather Details for {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Feels like: {feels_like}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Pressure: {pressure} hPa")
        print(f"description: {data["weather"][0]["description"].capitalize()}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data {e}")

city = input("Enter city")
weather(city)