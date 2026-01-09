class Plant:

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):

    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            color: str
            ) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def get_info(self):
        print(
            f"{self.name} (Flower): {self.height}cm, {self.age} days, "
            f"{self.color} color"
        )
        self.bloom()


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            trunk_diameter: int
            ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade = round(self.trunk_diameter * 1.5)
        print(f"{self.name} provides {shade} square meters of shade")

    def get_info(self):
        print(
            f"{self.name} (Tree): {self.height}cm, {self.age} days, "
            f"{self.trunk_diameter}cm diameter"
        )
        self.produce_shade()


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            harvest_season: str,
            nutritional_value: str,
            ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nutritional(self):
        print(f"{self.name} is rich in {self.nutritional_value}")

    def get_info(self):
        print(
            f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
            f"{self.harvest_season} harvest"
        )
        self.nutritional()


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===\n")

    rose = Flower("Rose", 25, 30, "red")
    cactus = Flower("Cactus", 120, 90, "green")

    oak = Tree("Oak", 500, 1825, 50)
    spruce = Tree("Spruce", 850, 2000, 60)

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    corn = Vegetable("Corn", 150, 100, "summer", "vitamin B")

    rose.get_info()
    cactus.get_info()
    print()
    oak.get_info()
    spruce.get_info()
    print()
    tomato.get_info()
    corn.get_info()


if __name__ == "__main__":
    ft_plant_types()
