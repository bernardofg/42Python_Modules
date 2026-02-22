import alchemy
import alchemy.elements


def main() -> None:
    print("=== Sacred Scroll Mastery ===\n")

    print("Testing direct module acess:")
    print("alchemy.elements.create_fire():"
          f" {alchemy.elements.create_fire()}")
    print("alchemy.elements.create_water():"
          f" {alchemy.elements.create_water()}")
    print("alchemy.elements.create_earth():"
          f" {alchemy.elements.create_earth()}")
    print("alchemy.elements.create_air():"
          f" {alchemy.elements.create_air()}")

    print("\nTesting package-level access (controlled by __init__.py):")
    try:
        print("alchemy.create_fire(): "
              f"{alchemy.create_fire()}")
    except AttributeError:
        print("alchemy.create_fire(): AttributeError - not exposed")
    try:
        print("alchemy.create_water(): "
              f"{alchemy.create_water()}")
    except AttributeError:
        print("alchemy.create_water(): AttributeError - not exposed")
    try:
        print("alchemy.create_earth(): "
              f"{alchemy.create_earth()}")
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")
    try:
        print("alchemy.create_air()): "
              f"{alchemy.create_air()}")
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
