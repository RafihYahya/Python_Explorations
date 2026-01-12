"""Fifth Docstring Module"""


def ft_count_harvest_recursive():
    """Counts down days to harvest recursively."""
    days_harv: int = int(input("Days until harvest: "))

    def ft_count_harvest_rec_helper(current_day: int, days_harv: int):
        """Helper function for ft_count_harvest_recursive."""
        if current_day == days_harv:
            print("Harvest time!")
        else:
            print(f"Day {current_day + 1}")
            ft_count_harvest_rec_helper(current_day + 1, days_harv)
    ft_count_harvest_rec_helper(0, days_harv)
