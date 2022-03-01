"""Define a dict whose keys are dates (represented by strings) from the most
recent week and whose values are temperatures. Ask the user to enter a date,
and display the temperature on that date, as well as the previous and
subsequent dates, if available."""

day_weather = {
        '02-23': 29,
        '02-24': 31,
        '02-25': 27,
        '02-26': 24,
        '02-27': 25,
        '02-28': 22,
        '02-29': 17,
        '02-30': 15
        }

def temperature():

    date = input('Choose a date: ')

    if date not in day_weather:
        print('Date out of scope.')
    elif date == list(day_weather)[0]:
        print(f'Today: {day_weather[date]}')
        print(f'Tomorrow: {day_weather[list(day_weather)[1]]}')
    elif date == list(day_weather)[-1]:
        print(f'Yesterday: {day_weather[list(day_weather)[-2]]}')
        print(f'Today: {day_weather[date]}')
    else:
        month = int(date.split('-')[0])
        day = int(date.split('-')[1])
        print(f'Yesterday: {day_weather[f"0{month}-{day - 1}"]}')
        print(f'Today: {day_weather[date]}')
        print(f'Tommorrow: {day_weather[f"0{month}-{day + 1}"]}')


temperature()

