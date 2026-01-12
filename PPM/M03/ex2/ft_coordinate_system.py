"""
This module provides functions for 3D coordinate system calculations,
including Euclidean distance between points.
"""
import sys
import math


def distance(a, b):
    """
    Calculates the Euclidean distance between two 3D points.

    Args:
        a (tuple): The first point as a tuple of (x, y, z) coordinates.
        b (tuple): The second point as a tuple of (x, y, z) coordinates.

    Returns:
        float: The Euclidean distance between the two points.
    """
    return math.sqrt(
        (a[0] - b[0]) ** 2 +
        (a[1] - b[1]) ** 2 +
        (a[2] - b[2]) ** 2
    )


def main():
    """
    Main function to demonstrate coordinate system calculations.

    It calculates and prints distances between predefined points
    and a point optionally provided via command-line arguments.
    """
    print("=== Game Coordinate System ===")

    origin = (0, 0, 0)
    point = (10, 20, 5)

    print(f"Position created: {origin}")
    print(
        f"Distance between {origin} and {point}: "
        f"{distance(origin, point):.2f}"
        )

    if len(sys.argv) != 2:
        print("\nError parsing coordinates: missing argument")
        return

    raw = sys.argv[1]
    parts = raw.split(",")

    if len(parts) != 3:
        print("Error parsing coordinates: expected 3 values")
        return

    coords = ()
    try:
        for part in parts:
            coords += (int(part),)
    except ValueError:
        print(f"Parsing invalid coordinates: {raw}")
        return

    print(f"\nParsing coordinates: '{raw}'")
    print(f"Parsed position: {coords}")
    print(
        f"Distance between {origin} and {coords}: "
        f"{distance(origin, coords):.2f}"
        )


if __name__ == "__main__":
    main()
