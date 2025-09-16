import requests

def get_weather(city="London"):
    """
    Fetches and prints the weather for a given city.

    :param city: The city to fetch the weather for (default: London)
    :return: None
    :raises: Exception: If there is an error fetching the weather
    """
    API = "https://wttr.in/{}?format=j1".format(city)
    try:
        res = requests.get(API)
        data = res.json()
        current = data["current_condition"][0]
        print(f"Weather in {city}: {current['temp_C']}°C, {current['weatherDesc'][0]['value']}")
        # Save to file
        with open("weather.csv", "w") as file:
            file.write("City,Temperature (°C),Description\n")
            file.write(f"{city},{current['temp_C']},{current['weatherDesc'][0]['value']}\n")
    except Exception as e:
        print("Error fetching weather:", e)


if __name__ == "__main__":
    get_weather("Maputo")