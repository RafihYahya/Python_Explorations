"""Third DocString Module"""


def ft_harvest_total():
    """Simple Harvest Calculating Function"""
    total: int = int(input("Day 1 harvest: "))
    total = total + int(input("Day 2 harvest: "))
    total = total + int(input("Day 3 harvest: "))
    print(f"Total harvest: {total}")
