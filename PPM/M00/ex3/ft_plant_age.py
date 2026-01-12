"""Fourth Docstring Module"""


def ft_plant_age():
    """Simple Age Checking Function"""
    harvest_age: int = int(input("Enter harvest age: "))
    if harvest_age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant need more time to grow.")
