def main():
    money = 0

    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    print("Write items to get sum of prices or enter empty string to stop program.")

    while True:
        try:
            a = input("Item: ").title()
            if not a:
                print(f"The sum is {money}")
                break
            else:
                if a in menu:
                    money += menu[a]
                    print(f"The sum is {money}")
        except:
            break

main()