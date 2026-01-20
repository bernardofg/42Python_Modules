import sys


def main():
    unique_items = len(sys.argv)
    print(f"Unique item types: {unique_items - 1}")


if __name__ == "__main__":
    main()
