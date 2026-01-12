"""Fifth Docstring Module"""


def ft_count_harvest_iterative():
    """Counts down days to harvest iteratively."""
    days_harv: int = int(input("Days until harvest: "))
    for i in range(days_harv):
        print(f"Day {i + 1}")
    print("Harvest time!")
