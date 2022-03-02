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
