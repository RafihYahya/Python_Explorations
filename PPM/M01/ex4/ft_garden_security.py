"""This module provides functions related to garden security."""


class SecurePlant:
    """Represents a plant in the garden."""

    def __init__(self, name, age, height):
        self.name = name
        self.print_info()
        self.set_age(age)
        self.set_height(height)

    @property
    def height(self):
        """Returns the height of the plant."""
        return self.__height

    @property
    def age(self):
        """Returns the age of the plant."""
        return self.__age

    def set_height(self, value):
        """Sets the height of the plant."""
        if self.validate(value):
            self.__height = value
            print(f"Height updated: {value} [OK]")
        else:
            print(
                f"\nInvalid operation attempted: height {value}cm [REJECTED]"
                )
            print("Security: Negative height rejected")

    def set_age(self, value):
        """Sets the age of the plant."""
        if self.validate(value):
            self.__age = value
            print(f"Age updated: {value} [OK]")
        else:
            print(
                f"\nInvalid operation attempted: age {value} [REJECTED]"
                )
            print("Security: Negative age rejected")

    def validate(self, value):
        """Validates the age of the plant."""
        if value < 0:
            return False
        return True

    def print_info(self):
        """Prints the information of the plant."""
        print("=== Garden Security System ===")
        print("Plant created: Rose")

    def print_curr_info(self):
        """Prints the current information of the plant."""
        print(
            f"\nCurrent plant: {self.name} ({self.height}cm, {self.age} days)"
            )


if __name__ == "__main__":
    plant1 = SecurePlant("Rose", 30, 25)
    plant1.set_height(-5)
    plant1.print_curr_info()
