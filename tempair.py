import requests
from bs4 import BeautifulSoup
import logging
logging.getLogger("requests").setLevel(logging.ERROR)


def fetch_weather(location):
    url = f"https://wttr.in/{location}?format=%t%20%w%20%l"

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup=BeautifulSoup(response.text, 'html.parser')
        # weather_info = response.text.strip().split()
        weather_info = soup.get_text().strip()

        temperature = int(weather_info[:3])
        wind = weather_info[9:]

        print(f"Temperature is {temperature}°C and wind is {wind}")

        if temperature > 40:
            print("It's too hot!!")
        elif 30 < temperature < 40:
            print("It's hot!!")
        elif 20 < temperature < 30:
            print("It's warm!!")
        elif 10 < temperature < 20:
            print("It's cool!!")
        elif temperature < 10:
            print("It's cold!!")

    except requests.exceptions.RequestException as e:
        print("An error occurred while retrieving weather data:", e)

def main():
    location = input("Enter city name or location query: ")
    fetch_weather(location)

if __name__ == "__main__":
    main()