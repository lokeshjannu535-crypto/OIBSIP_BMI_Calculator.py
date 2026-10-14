import json
import urllib.request
import urllib.parse
import urllib.error


def get_weather(city):
    """Fetch and display current weather for a city."""

    # Encode the city name for use in a URL
    city_name = urllib.parse.quote(city)

    # Free current-weather API
    url = (
        "https://wttr.in/"
        + city_name
        + "?format=j1"
    )

    try:
        # Request weather data from the API
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        with urllib.request.urlopen(request, timeout=15) as response:
            data = json.loads(response.read().decode("utf-8"))

        # Extract current weather information
        current = data["current_condition"][0]
        location = data["nearest_area"][0]

        city_display = location["areaName"][0]["value"]
        country = location["country"][0]["value"]
        temperature = current["temp_C"]
        feels_like = current["FeelsLikeC"]
        humidity = current["humidity"]
        description = current["weatherDesc"][0]["value"]
        wind_speed = current["windspeedKmph"]

        # Display the weather report
        print("\n" + "=" * 35)
        print("        WEATHER REPORT")
        print("=" * 35)
        print(f"City          : {city_display}")
        print(f"Country       : {country}")
        print(f"Temperature   : {temperature} °C")
        print(f"Feels Like    : {feels_like} °C")
        print(f"Humidity      : {humidity}%")
        print(f"Condition     : {description}")
        print(f"Wind Speed    : {wind_speed} km/h")
        print("=" * 35)

    except urllib.error.HTTPError as error:
        print("Unable to get weather data. Please check the city name.")
        print(f"HTTP error: {error.code}")

    except urllib.error.URLError:
        print("Unable to connect to the weather service.")
        print("Please check your internet connection and try again.")

    except (KeyError, IndexError, TypeError, ValueError, json.JSONDecodeError):
        print("Weather data could not be read. Please try again later.")

    except TimeoutError:
        print("The request took too long. Please try again.")

    except Exception as error:
        print("An unexpected error occurred:", error)


def main():
    print("=" * 35)
    print("       PYTHON WEATHER APP")
    print("=" * 35)

    while True:
        city = input(
            "\nEnter a city name (or type 'exit' to quit): "
        ).strip()

        if city.lower() == "exit":
            print("Thank you for using the Weather App!")
            break

        if not city:
            print("City name cannot be empty. Please try again.")
            continue

        get_weather(city)


if __name__ == "__main__":
    main()
