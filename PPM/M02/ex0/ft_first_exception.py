"""Module providing a basic first exception handling example."""
def check_temperature(temp_str):
    """Checks if the given string represents a valid temperature.

    Args:
        temp_str (str): The string to be checked for temperature validity.

    Returns:
        bool: True if the string is a valid temperature, False otherwise.
    """
    print(f"Testing Temperature: {temp_str}")
    try:
        temp = int(temp_str)
        if temp > 40 or temp < 0:
            print("Invalid temperature")
        else:
            print("Valid temperature")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
if __name__ == "__main__":
    check_temperature("42")
    check_temperature("abc")
