"""
This module defines custom exceptions for the PPM M02 ex2 project.
"""
class GardenError(Exception):
    """
    Base exception for all errors in the Garden project.
    """
    def __init__(self, message = "Garden error"):
        super().__init__(message)
class PlantError(GardenError):
    """
    Exception for errors related to plants.
    """
    def __init__(self, message = "Plant error"):
        super().__init__(message)
class WaterError(GardenError):
    """
    Exception for errors related to water.
    """
    def __init__(self, message = "Water error"):
        super().__init__(message)
if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        raise PlantError()
    except PlantError:
        print("Caught PlantError: The tomato plant is wilting!")
    try:
        print("Testing WaterError...")
        raise WaterError()
    except WaterError:
        print("Caught WaterError: Not enough water in the tank!\n")
    try:
        print("Testing catching all garden errors...")
        raise PlantError()
    except PlantError:
        print("Caught PlantError: The tomato plant is wilting!")
    try:
        raise WaterError()
    except WaterError:
        print("Caught WaterError: Not enough water in the tank!\n")
    print("All custom error types work correctly!")
