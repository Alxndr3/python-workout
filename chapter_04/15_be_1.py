def get_rainfall():
    cities = {}

    while True:
        city = input("Enter name city: ").strip().lower()

        if not city:
            break

        else:
            mm_rain = input("How much rain has fallen in the city: ")

            cities[city] = []
            cities[city].append(mm_rain)

    print(cities)



get_rainfall()

