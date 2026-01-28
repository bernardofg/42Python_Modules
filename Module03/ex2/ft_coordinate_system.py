import math


def parsing(str_cords: str):
    parts = str_cords.split(",")

    try:
        if len(parts) != 3:
            raise ValueError("Expected 3 coordinates")

        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])

        coords = (x, y, z)
        return coords

    except ValueError as error:
        print("Error parsing coordinates:", error)
        print(
            f"Error details - Type: ValueError, Args: {error.args}")
        return


def distance_calc(pos1, pos2):
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    result = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return result


def main():
    print("=== Game Coordinate System ===")
    pos = (10, 20, 5)
    origin = (0, 0, 0)
    print(f"\nPosition created: {pos}")
    res = distance_calc(pos, origin)
    print(f"Distance between {origin} and {pos}: {res:.2f}")

    print('\nParsing coordinates: "3,4,0"')
    pos_str = parsing("3,4,0")
    print(f"Parsed position: {pos_str}")
    res = distance_calc(pos_str, origin)
    print(f"Distance between {origin} and {pos_str}: {res}")

    pos_error = "abc,def,ghi"
    print(f'\nParsing invalid coordinates: "{pos_error}"')
    parsing(pos_error)

    print("\nUnpacking demonstration:")
    x, y, z = pos_str
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
