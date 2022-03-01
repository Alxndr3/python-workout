import time


def run_timing():
    run_time = list()
    while True:
        runtime = input("Enter 10 Km run time: ")
        if not runtime:
            break
        else:
            run_time.append(float(runtime))
    return f"Average run {sum(run_time) / len(run_time)} over {len(run_time)} runs"


# Book solution.
def run_timing_bs():
    """Asks the user repeatedly for a numeric input. Prints the average timing
    and the number of runs."""


    number_of_runs = 0
    total_time = 0


    while True:
        one_run = input('Enter 10km run time: ')

        if not one_run:
            break

        number_of_runs += 1
        total_time += float(one_run)
        average_time = total_time / number_of_runs

        print(f'Average of {average_time}, over {number_of_runs} runs')


# Beyonde the exercice
from decimal import *


def sum_decimal(value1, value2):
    getcontext().prec = 2
    return Decimal(value1) + Decimal(value2)


print(sum_decimal('1.1234', '1.2'))

