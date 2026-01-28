import sys


def main():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    try:
        id: str = input("Input Stream active. Enter archivist ID: ")
        status: str = input("Input Stream active. Enter status report: ")
    except KeyboardInterrupt:
        print("[ERROR] inputs cannot be empty, try again", file=sys.stderr)
    msg = f"\n[STANDARD] Archive status from {id}: {status}"
    sys.stdout.write(msg)
    sys.stderr.write(
        "\n[ALERT] System diagnostic: Communication channels verified"
        )
    sys.stdout.write("\n[STANDARD] Data transmission complete\n")
    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    main()
