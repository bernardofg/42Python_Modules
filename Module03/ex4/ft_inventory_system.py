import sys


def main():
    print("=== Inventory System Analysis ===")
    
    args = sys.argv
    inventory: dict[str, int] = dict()

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

        if not colon:
            continue
        if key == "":
            continue
        if value == "":
            continue

        try:
            qty = int(value)
        except ValueError:
            continue

        if qty < 0:
            continue

        value = int(value)
        actual = inventory.get(key, 0)
        new = actual + value
        inventory[key] = new

    total_items = 0
    for v in inventory.values():
        total_items += v
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")

    print("\n=== Current Inventory ===")

    for key, value in inventory.items():
        percent = (value / total_items) * 100
        print(f"{key}: {value} units ({percent:.1f}%)")

    print("\n=== Inventory Statistics ===")

    most = None
    for value in inventory.values():
        if most is None:
            most = value
        elif value > most:
            most = value

    most_key = None
    for key, value in inventory.items():
        if value == most:
            most_key = key

    least = None
    for value in inventory.values():
        if least is None:
            least = value
        elif value < least:
            least = value

    least_key = None
    for key, value in inventory.items():
        if value == least and least_key is None:
            least_key = key

    print(f"Most abundant: {most_key} ({most})")
    print(f"Least abundant: {least_key} ({least})")

    print("\n=== Item Categories ===")

    moderate = {}
    scarce = {}
    for key, value in inventory.items():
        if value >= 4:
            moderate[key] = value
        else:
            scarce[key] = value
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

    print("\n=== Management Suggestions ===")

    restock = []
    for key, value in inventory.items():
        if value < 2:
            restock = restock + [key]
    print(f"Restock needed: {restock}")

    print("\n === Dictionary Properties Demo ===")

    keys = []
    values = []
    for key, value in inventory.items():
        keys = keys + [key]
        values = values + [value]
    print(f"Dictionary keys: {keys}")
    print(f"Dictionary values: {values}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


if __name__ == "__main__":
    main()
