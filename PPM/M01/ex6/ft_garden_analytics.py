"""
This module provides analytics functionalities for the ft_garden project.
"""


class Plant:
    """
    Represents a plant in the garden.
    """
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def display_info(self):
        """
        Displays the information about the prize plant.
        """
        print(f"- {self.name}, Age: {self.age}")


class FloweringPlant(Plant):
    """
    Represents a flowering plant in the garden.
    """
    def __init__(self, name, age, color, height):
        super().__init__(name, age, height)
        self.color = color

    def display_info(self):
        """
        Displays the information about the prize plant.
        """
        print(f"- {self.name}, Age: {self.age}, {self.color} flower")


class PrizePlant(Plant):
    """
    Represents a fruit-bearing plant in the garden.
    """
    def __init__(self, name, age, color, prize, height):
        super().__init__(name, age, height)
        self.color = color
        self.prize = prize

    def display_info(self):
        """
        Displays the information about the prize plant.
        """
        print(f"- {self.name}, Age: {self.age}, {self.color} "
              f"flower, Prize: {self.prize}")


class Garden:
    """
    Represents a garden in the garden management system.
    """
    def __init__(self, name, stats, score=0):
        self.name = name
        self.plants = []
        self.stats = stats
        self.score = score

    def add_plant(self, plant):
        """
        Adds a plant to the garden.
        """
        self.plants.append(plant)
        self.stats.plant_added += 1
        print(f"Added {plant.name} to {self.name}")

    def grow_height(self, num):
        """
        Increases the height of all plants in the garden by a given number.
        """
        for plant in self.plants:
            plant.height += num
            self.stats.total_growth += num
            print(f"Increased height of {plant.name} by {num}cm")

    def display_all_plants(self):
        """
        Displays all plants in the garden.
        """
        for plant in self.plants:
            plant.display_info()


class GardenManager:
    """
    Manages the garden's plants, operations, and analytics.
    """
    def __init__(self):
        self.gardens = {}
        self.stats = GardenStats(self)

    def add_garden(self, garden):
        """
        Adds a new garden to the system.
        """
        self.gardens[garden.name] = garden
        self.stats.num_garden += 1

    @classmethod
    def create_garden_network(cls):
        """
        Creates a network of gardens.
        """
        garden_network = cls()
        return garden_network

    @staticmethod
    def statis_helper():
        """
        Helper function for statistical calculations.
        """


class GardenStats:
    """
    Calculates and stores statistics for the garden.
    """
    plant_added = 0
    total_growth = 0
    num_garden = 0

    def __init__(self, garden_manager):
        self.garden_manager = garden_manager

    def print_plant_types(self, garden):
        """
        Prints the number of each type of plant in the garden.
        """
        plant_counts = {
           "Plant": 0,
           "FloweringPlant": 0,
           "PrizePlant": 0
        }
        for plant in garden.plants:
            plant_type = plant.__class__.__name__
            if plant_type in plant_counts:
                plant_counts[plant_type] += 1
        print(f"Plant types: {plant_counts['Plant']} regular, "
              f"{plant_counts['FloweringPlant']} flowering, "
              f"{plant_counts['PrizePlant']} prize flowers")

    def validate_height(self):
        """
        Validates the height of plants in the garden.
        """
        for garden in self.garden_manager.gardens.values():
            for plant in garden.plants:
                if plant.height < 1:
                    return False
        return True

    def calculate_score(self):
        """
        Calculates the score for each garden.
        """
        plant_score = {
            "Plant": 1,
            "FloweringPlant": 2,
            "PrizePlant": 3
        }
        for garden in self.garden_manager.gardens.values():
            score = 0
            for plant in garden.plants:
                score += plant_score[plant.__class__.__name__]
            garden.score = score


def main():
    """
    Main function to run the garden analytics dashboard.
    """
    print("=== Garden Management System Demo ===\n")
    garden = GardenManager()
    garden.add_garden(Garden("Alices Garden", garden.stats))
    garden.add_garden(Garden("Bobs Garden", garden.stats))
    alice_garden = garden.gardens["Alices Garden"]
    alice_garden.add_plant(Plant("Oak Tree", 1, 10))
    alice_garden.add_plant(FloweringPlant("Rose", 1, "Blue", 5))
    alice_garden.add_plant(PrizePlant("Apple", 10, "Red", 10, 7))
    print("\nAlice is helping all plants grow...")
    alice_garden.grow_height(1)
    print("\n=== Alice's Garden Report ===")
    print("Plants in garden")
    alice_garden.display_all_plants()
    print(f"\nPlants added: {garden.stats.plant_added}, "
          f"Total growth: {garden.stats.total_growth}")
    garden.stats.print_plant_types(alice_garden)
    print(f"\nHeight validation test: {garden.stats.validate_height()}")
    garden.stats.calculate_score()
    print(f"Garden scores - Alice: {garden.gardens['Alices Garden'].score}, "
          f"Bob: {garden.gardens['Bobs Garden'].score}")
    print(f"Total gardens managed: {garden.stats.num_garden}")


if __name__ == "__main__":
    main()
