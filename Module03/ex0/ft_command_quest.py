import sys


def main() -> None:
    print("=== Command Quest ===")
    argc = len(sys.argv)
    argv = sys.argv
    if argc <= 1:
        print("No arguments provided!")
        print(f"Program name: {argv[0]}")
        print(f"Total arguments: {argc}")
    else:
        print(f"Program name: {argv[0]}")
        print(f"Arguments received: {argc - 1}")
        i: int = 1
        for arg in argv[1:]:
            print(f"Argument {i}: {arg}")
            i += 1

        print(f"Total arguments: {argc}")


if __name__ == "__main__":
    main()
