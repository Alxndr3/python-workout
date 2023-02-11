"""Instead of printing just the total rainfall for each city, print the total
rainfall and the average rainfall for reported days. Thus, if you were to enter
30, 20, and 40 for Boston, you would see that the total was 90 and the average
was 30."""


def get_rainfall():
    cities = {}

    while True:
        city = input("Enter name city: ").strip().lower()

        if not city:
            break

        else:
            mm_rain = int(input("How much rain has fallen in the city: "))

            if city not in cities:
                cities[city] = [mm_rain]
            else:
                cities[city].append(mm_rain)

    for k in cities:
        print(k.title())
        print(f"Total rainfall: {sum(cities[k])}mm")
        print(f"Average rainfall: {sum(cities[k]) / len(cities[k])}mm")


get_rainfall()

