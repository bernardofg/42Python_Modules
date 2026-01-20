import sys


def main():

    args = sys.argv
    inventory = {}

    for string in args[1:]:
        key = ""
        value = ""
        colon = False
        for chars in string:
            if chars == ":":
                colon = True
                continue

            if not colon:
                key += chars
            else:
                value += chars
        value = int(value)
        inventory[key] = value

    print(f"Total items in inventory: {value(value)}")
    print(f"Unique item types: {len(inventory)}")


if __name__ == "__main__":
    main()
