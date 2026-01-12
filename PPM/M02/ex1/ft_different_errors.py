"""
This file contains examples of different types of errors in Python.
It's meant for educational purposes to demonstrate common mistakes and
how they manifest.
"""


def garden_operations():
    """Demonstrates various common Python errors."""
    try:
        print("Testing ValueError...")
        int("avxc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    try:
        print("Testing ZeroDivisionError...")
        print(1 / 0)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    try:
        print("Testing KeyError...")
        tmp1 = {"key1": "value1", "key2": "value2"}
        tmp1["key1"] = tmp1["key3"]
    except KeyError:
        print("Caught KeyError: 'key3' not found in dictionary")
    try:
        print("Testing multiple errors together...")
        tmp1 = {"key1": "value1", "key2": "value2"}
        tmp1["key1"] = tmp1["key3"]
        print(1 / 0)
    except (ValueError, ZeroDivisionError, KeyError, FileNotFoundError):
        print("Caught an error, but program continues!")


if __name__ == "__main__":
    garden_operations()
