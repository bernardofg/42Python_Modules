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
        self.trunk_diamter = trunk_diameter

    def produce_shade(self):
        print ("Oak provides 78 square meters of shade")

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


def ft_plant_types() -> None:
    rose = Flower("Rose", 25, 30, "red")
    cactus = Flower("Cactus", 120, 90, "green")

    oak = Tree("Oak", 500, 1825, 50)
    spruce = Tree("Spruce", 850, 2000, 60)

    tomato = Vegetable("Tomato", 80, 90, "summer" "vitamin C")
    corn = Vegetable("Corn", 150, 100, "summer" "vitamin B")
