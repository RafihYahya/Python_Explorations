"""This module contains functions to simulate plant growth."""


class Plant:
    """Represents a plant with various attributes."""

    def __init__(self, name, height, age, growth_rate=0):
        self.name = name
        self.height = height
        self.age_v = age
        self.growth = growth_rate

    def get_info(self):
        """Displays the plant's name, height, and age."""
        print(f"{self.name}: {self.height} cm, {self.age_v} days old")

    def age(self):
        """Increases the plant's age by 1 day."""
        self.age_v += 1

    def grow(self):
        """Increases the plant's height by 1 cm."""
        self.height += 1

    def age_growth_in_days(self, days):
        """Simulates plant growth for a specified number of days."""
        original_height = self.height
        for _ in range(days):
            self.age()
            self.grow()
        self.growth = self.height - original_height


def main():
    """Main function to demonstrate Plant class usage."""
    day: int = 6
    plant1 = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    plant1.get_info()
    print(f"=== Day {day + 1} ===")
    plant1.age_growth_in_days(day)
    plant1.get_info()
    print(f"Growth this week: +{plant1.growth}")


if __name__ == "__main__":
    main()
