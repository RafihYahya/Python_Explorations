"""Fourth Docstring"""


def ft_water_reminder():
    """Simple Water Days Check"""
    days: int = int(input("Days since last watering: "))
    if days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
