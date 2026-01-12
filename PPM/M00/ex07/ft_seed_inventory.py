"""Final Docstring Module"""


def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    """
    Prints a formatted string indicating the available quantity of a
    seed type based on the given unit.
    Args:
        seed_type (str): The type of seed (e.g., "tomato", "basil").
        quantity (int): The amount of the seed.
        unit (str): The unit of measurement for the quantity
        (e.g., "packets", "grams", "area").
    """
    match unit:
        case "packets":
            custom = f"{quantity} packets available"
        case "grams":
            custom = f"{quantity} grams available"
        case "area":
            custom = f"covers {quantity} square meters"
        case _:
            custom = f"{quantity} Unknown unit type"
    print(f"{seed_type.capitalize()} {custom}")
