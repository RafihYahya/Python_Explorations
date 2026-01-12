"""
This module provides utilities for managing garden data.
"""


class Plant:
    """Represents a plant with various attributes."""
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def display_info(self):
        """Displays the plant's name, height, and age."""
        print(f"{self.name}: {self.height} cm, {self.age} days old")


def main():
    """Main function to demonstrate Plant class usage."""
    print("=== Garden Plant Registry ===")
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 15, 45)
    plant3 = Plant("Tulip", 18, 20)
    plant1.display_info()
    plant2.display_info()
    plant3.display_info()


if __name__ == "__main__":
    main()
