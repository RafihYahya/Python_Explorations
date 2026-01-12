"""
This module demonstrates the use of a `finally` block in Python.

It includes examples of how `finally` blocks ensure code execution
regardless of whether an exception occurs in the `try` block.
"""


def water_plants(plant_list):
    """
    Simulates watering a list of plants.

    This function iterates through a list of plants and "waters" each one.
    It's designed to demonstrate resource management in a `finally` block,
    even if an error occurs during the watering process.

    Args:
        plant_list (list): A list of plant names (strings) to be watered.
    """
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("None value found in list")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: Cannot water {e} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """
    Tests the water_plants function with various scenarios.

    This function demonstrates how the `finally` block ensures cleanup
    even when exceptions occur during the `try` block's execution.
    """
    print("Testing normal watering...")
    water_plants(["Tomato", "Potato", "Dotato"])
    print("Watering completed successfully!\n")
    print("Testing with error...")
    water_plants(["Tomato", "Potato", None])
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
