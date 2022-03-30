"""Specifically, write a function, get_rainfall, that tracks rainfall in a number of cities. Users of your program will enter the name of a city; if the city name is blank, then the function prints a report (which I’ll describe) before exiting.

If the city name isn’t blank, then the program should also ask the user how much rain has fallen in that city (typically measured in millimeters). After the user enters the quantity of rain, the program again asks them for a city name, rainfall amount, and so on--until the user presses Enter instead of typing the name of a city.

When the user enters a blank city name, the program exits--but first, it
reports how much total rainfall there was in each city."""

def get_rainfall():
    cities = {}

    while True:
        city = input("Enter name city: ").strip().lower()

        if not city:
            for k, v in cities.items():
                print(f"{k.title()}: {v}")
            break

        else:
            hm_rain = input("How much rain has fallen in the city: ")

            cities[city] = hm_rain


def get_rainfall():
    rainfall = {}

    while True:
        city_name = input('Enter city name: ')
        if not city_name:
            break

        mm_rain = input('Enter mm rain: ')
        rainfall[city_name] = rainfall.get(city_name,
                        0) + int(mm_rain)

    for city, rain in rainfall.items():
        print(f'{city}: {rain}')


get_rainfall()
