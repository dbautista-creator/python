def main():
    while True:
        try:
            hotdogs = int(input("How many hotdogs:  "))
            break
        except ValueError:
            hotdogs = 0
            print("Invalid input")

    while True:
        try:
            chips = int(input("How many bags of chips: "))
            break
        except ValueError:
            chips = 0
            print("Invalid input")

    while True:
        try:
            sodas = int(input("How many cans of sodas:  "))
            if sodas >= 0:
                break
            else:
                print("Invalid input")
        except ValueError:
            print("Invalid input")

    total = (hotdogs * 2.50) + (chips * 1.5) + (sodas * 1.25)
    print("Please pay $%.2f" % (total))


if __name__ == "__main__":
    main()
