from pprint import pprint


MENU = {'sandwitch': 7,
        'pastel': 5,
        'hamburger': 8,
        'soda': 3,
        'juice': 4,
        'coffee': 3
        }


def restaurant(menu):
    total = 0
    print("Our Menu")
    for k, v in menu.items():
        print(f"{k.title():<10} ${v}.00")
    while True:
        order = str(input('Place your order: ').lower().strip()) 
        if not order:
            print("Thank you!")
            break
        if order not in menu:
            print(f"We are fresh ou of {order}")
        else:
            total += menu[order]
            print(f"{order} costs {menu[order]} total is {total}")

    print(f"Your total is {total}")


def restaurant_bs():
    total = 0
    while True:
        order = input('Order: ').strip()

        if not order:
            break

        if order in MENU:
            price = MENU[order]
            total += price
            print(f"{order} is {price}, total is {total}")
        else:
            print(f"We are fresh out of {order} today")

    print(f"Your total is {total}")


# restaurant(MENU)
restaurant_bs()


