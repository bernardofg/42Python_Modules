def garden_operations() -> None:
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as error:
        print("Caught ValueError:", error)

    print("\nTesting ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError as error:
        print("caught ZeroDivisionError:", error)

    print("\nTesting FileNotFoundError...")
    try:
        raise FileNotFoundError("No such file 'missing.txt'")
    except FileNotFoundError as error:
        print("Caught FileNotFoundError:", error)

    print("\nTesting KeyError...")
    try:
        plants = {"rose": "red", "tulip": "yellow"}
        plants["missing_plant"]
    except KeyError as error:
        print("Caught KeyError:", error)


def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
