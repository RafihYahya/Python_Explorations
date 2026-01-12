"""
This module defines different types of plants using an enumeration.
"""


class Plant:
    """
    Base class for all plant types.
    """

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def print_info(self):
        """
        Prints information about the plant.
        """
        print(
            f"Name: {self.name}({self.__class__.__name__}),"
            f" Height: {self.height}, Age: {self.age}"
        )


class Flower(Plant):
    """
    Represents a flower, inheriting from Plant.
    """

    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def print_info(self):
        """
        Prints information about the flower.
        """
        super().print_info()
        print(f"Color: {self.color}")

    def bloom(self):
        """
        Simulates the blooming of the flower, with a dramatic message.
        """
        print(
            "The Scarlet flower is blooming once more, "
            "you will witness true horror\n"
        )


class Tree(Plant):
    """
    Represents a tree, inheriting from Plant.
    """

    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def print_info(self):
        """
        Prints information about the tree.
        """
        super().print_info()
        print(f"Trunk Diameter: {self.trunk_diameter}")

    def produce_shade(self):
        """
        Producing shade
        """
        print("The tree is producing a shade of green\n")


class Vegetable(Plant):
    """
    Represents a vegetable, inheriting from Plant.
    """

    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def print_info(self):
        """
        Prints information about the vegetable.
        """
        super().print_info()
        print(
            f"Harvest Season: {self.harvest_season}, Nutritional Value: "
            f"{self.nutritional_value}\n"
        )


if __name__ == "__main__":
    flower1 = Flower("Rose", 10, 5, "Red")
    flower2 = Flower("Sunflower", 5, 2, "Yellow")
    tree1 = Tree("Oak", 20, 10, 15)
    tree2 = Tree("Pine", 15, 8, 12)
    vegetable1 = Vegetable("Broccoli", 3, 1, "Summer", "Vitamin C")
    vegetable2 = Vegetable("Carrots", 2, 0.5, "Fall", "Vitamin A")
    flower1.print_info()
    flower1.bloom()
    flower2.print_info()
    flower1.bloom()
    tree1.print_info()
    tree1.produce_shade()
    tree2.print_info()
    tree1.produce_shade()
    vegetable1.print_info()
    vegetable2.print_info()
