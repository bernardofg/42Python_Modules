class Plant:

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def aging(self) -> None:
        self.age += 1

    def grow(self) -> None:
        self.height += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_plant_growth() -> None:
    time: int = 7
    plants = [
        Plant("Rose", 25, 30),
        Plant("Cactus", 80, 40)
        ]
    initial_height = {}
    print("=== Day 1 ===")
    for plant in plants:
        plant.get_info()
        initial_height[plant] = plant.height
    for plant in plants:
        day: int = 1
        while day < time:
            plant.grow()
            plant.aging()
            day += 1
    print("=== Day 7 ===")
    for plant in plants:
        plant.get_info()
        growth = (plant.height - initial_height[plant])
        print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    ft_plant_growth()
