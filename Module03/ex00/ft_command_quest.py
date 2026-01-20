import sys


def main():
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
        for i in range(1, argc):
            print(f"Argument {i}: {argv[i]}")
        print(f"Total arguments: {argc}")


if __name__ == "__main__":
    main()
