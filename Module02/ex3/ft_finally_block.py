def water_plant(plant_list: list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            else:
                print(f"Watering {plant}")
    except ValueError as error:
        print("Error:", error)
    else:
        print("Watering completed successfully!")
    finally:
        print("Closing watering system (cleanup)\n")


def ft_finally_block():
    print("=== Garden Watering System ===\n")
    plant = [
        "tomatto",
        "lettuce",
        "carrots"
    ]
    water_plant(plant)
    print("Testing with error...")
    plant = [
        "tomato",
        None
    ]
    water_plant(plant)
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    ft_finally_block()
