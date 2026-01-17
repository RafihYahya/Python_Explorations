"""This module provides a class for creating different types of plants."""


class Plant:
    """Base class for all plants."""

    def __init__(self, name, age, height):
        self.name = name
        self.height = height
        self.age = age

    def print_info(self):
        """Displays the plant's name, height, and age."""
        print(f"{self.name}: {self.height} cm, {self.age} days old")


def plant_factory(name, age, height):
    """Factory function to create a new Plant instance."""
    return Plant(name, age, height)


if __name__ == "__main__":
    print("===")
    plant1 = plant_factory("Rose", 30, 25)
    plant1.print_info()
    print("===")
    plant2 = plant_factory("Sunflower", 20, 15)
    plant2.print_info()
    print("===")
    plant3 = plant_factory("Daisy", 15, 10)
    plant3.print_info()
    print("===")
    plant4 = plant_factory("Tulip", 10, 5)
    plant4.print_info()
    print("===")
    plant5 = plant_factory("Orchid", 5, 2)
    plant5.print_info()
