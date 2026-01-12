"""
This module contains functions that demonstrate raising
different types of errors.
"""


def check_plant_health(plant_name, water_level, sunlight_hours):
    """
    Checks the health of a plant based on its name, water level,
    and sunlight hours.

    Args:
        plant_name (str): The name of the plant.
        water_level (int): The current water level for the plant (0-10).
        sunlight_hours (int): The number of sunlight hours the
        plant receives (0-12).

    Raises:
        ValueError: If plant_name is empty, water_level is out of range,
        or sunlight_hours is out of range.
    """
    if plant_name == "":
        raise ValueError("Empty Name")
    if 0 < water_level > 10:
        raise ValueError("Negative Water Level")
    if 0 < sunlight_hours > 12:
        raise ValueError("Negative Sunlight Hours")
    print(f"Plant '{plant_name}' is healthy!")
