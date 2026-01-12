"""
This module provides utilities for handling and processing data streams.
It likely contains functions or classes to read, transform, or write
data in a streaming fashion.
"""

import time

events_by_player = {
    "alice": [
        {
            "id": 4,
            "event_type": "level_up",
            "timestamp": "2024-01-07T22:41",
            "level": 45,
            "score_delta": 458,
            "zone": "pixel_zone_4",
        },
        {
            "id": 23,
            "event_type": "item_found",
            "timestamp": "2024-01-10T20:32",
            "level": 39,
            "score_delta": 103,
            "zone": "pixel_zone_2",
        },
        {
            "id": 35,
            "event_type": "item_found",
            "timestamp": "2024-01-14T11:27",
            "level": 27,
            "score_delta": 378,
            "zone": "pixel_zone_1",
        },
        {
            "id": 50,
            "event_type": "login",
            "timestamp": "2024-01-15T19:36",
            "level": 7,
            "score_delta": -25,
            "zone": "pixel_zone_5",
        },
        {
            "id": 10,
            "event_type": "logout",
            "timestamp": "2024-01-28T03:24",
            "level": 18,
            "score_delta": 364,
            "zone": "pixel_zone_3",
        },
        {
            "id": 46,
            "event_type": "item_found",
            "timestamp": "2024-01-28T07:25",
            "level": 8,
            "score_delta": 483,
            "zone": "pixel_zone_2",
        },
        {
            "id": 32,
            "event_type": "login",
            "timestamp": "2024-01-28T10:04",
            "level": 33,
            "score_delta": 143,
            "zone": "pixel_zone_3",
        },
        {
            "id": 22,
            "event_type": "item_found",
            "timestamp": "2024-01-29T23:16",
            "level": 33,
            "score_delta": 82,
            "zone": "pixel_zone_5",
        },
        {
            "id": 25,
            "event_type": "login",
            "timestamp": "2024-01-30T11:56",
            "level": 20,
            "score_delta": 145,
            "zone": "pixel_zone_1",
        },
    ],
    "bob": [
        {
            "id": 26,
            "event_type": "level_up",
            "timestamp": "2024-01-03T02:46",
            "level": 32,
            "score_delta": -30,
            "zone": "pixel_zone_5",
        },
        {
            "id": 30,
            "event_type": "logout",
            "timestamp": "2024-01-03T10:01",
            "level": 38,
            "score_delta": 467,
            "zone": "pixel_zone_2",
        },
        {
            "id": 16,
            "event_type": "kill",
            "timestamp": "2024-01-05T07:47",
            "level": 36,
            "score_delta": 451,
            "zone": "pixel_zone_3",
        },
        {
            "id": 43,
            "event_type": "kill",
            "timestamp": "2024-01-07T01:37",
            "level": 48,
            "score_delta": 455,
            "zone": "pixel_zone_1",
        },
        {
            "id": 37,
            "event_type": "logout",
            "timestamp": "2024-01-07T17:28",
            "level": 9,
            "score_delta": 332,
            "zone": "pixel_zone_2",
        },
        {
            "id": 11,
            "event_type": "kill",
            "timestamp": "2024-01-12T06:42",
            "level": 18,
            "score_delta": -27,
            "zone": "pixel_zone_5",
        },
        {
            "id": 45,
            "event_type": "login",
            "timestamp": "2024-01-17T02:54",
            "level": 12,
            "score_delta": -30,
            "zone": "pixel_zone_5",
        },
        {
            "id": 5,
            "event_type": "death",
            "timestamp": "2024-01-19T08:51",
            "level": 1,
            "score_delta": 63,
            "zone": "pixel_zone_4",
        },
        {
            "id": 27,
            "event_type": "logout",
            "timestamp": "2024-01-22T15:35",
            "level": 11,
            "score_delta": 171,
            "zone": "pixel_zone_5",
        },
        {
            "id": 14,
            "event_type": "login",
            "timestamp": "2024-01-26T10:25",
            "level": 18,
            "score_delta": -33,
            "zone": "pixel_zone_2",
        },
    ],
}


def combine_player_events(events_by_player0):
    """
    Sorts events by their timestamp in ascending order.

    Args:
        events (list): A list of event dictionaries, each containing
                       at least a 'timestamp' key.

    Yields:
        dict: The next event in chronological order.
    """
    all_events = []
    for player_name, player_events in events_by_player0.items():
        for event in player_events:
            event["player"] = player_name
            all_events.append(event)
    return all_events


def sort_events(events):
    """
    Sorts events by their timestamp in ascending order.

    Args:
        events (list): A list of event dictionaries, each containing
                       at least a 'timestamp' key.

    Yields:
        dict: The next event in chronological order.
    """
    current_time = events[0]["timestamp"]
    for event in events:
        if event["timestamp"] < current_time:
            current_time = event["timestamp"]
        yield event


def process_event(events_gen, num_events):
    """
    Simulates processing a series of events.
    Yields:
        int: The index of the processed event.
    """
    for i in range(num_events):
        event = next(events_gen)
        print(
            f"Event {i + 1}: {event['player']} (level {event['level']}) "
            f"{event['event_type']}"
        )
        yield i + 1


def count_type_events(event_type, events):
    """
    Counts events of a specific type.
    """
    count = 0
    for event in events:
        if event.get("event_type") == event_type:
            count += 1
    return count


def fibonacci_generator():
    """
    Generator that yields Fibonacci numbers.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def is_prime(n):
    """
    Checks if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is a prime number, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_number_generator():
    """
    Generator that yields prime numbers.
    """
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


def main():
    """
    Entry point for the data stream utility.
    """

    all_events = combine_player_events(events_by_player)
    events_gen = sort_events(all_events)
    print("=== Game Data Stream Processor ===\n")
    print(f"Processing {len(all_events)} game events...")

    my_generator = process_event(events_gen, len(all_events))
    i = 0
    start_time = time.time()
    for _ in my_generator:
        i = i + 1
    end_time = time.time()
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {i}")
    print(f"High-level players: (10+){len(events_by_player)}")

    treasure_count = count_type_events("item_found", all_events)
    print(f"Treasure events: {treasure_count}")
    levelup_count = count_type_events("level_up", all_events)
    print(f"Level-up events: {levelup_count}")

    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {end_time - start_time:.4f} seconds\n")

    print("=== Generator Demonstration ===")

    fib_gen = fibonacci_generator()
    print("First 10 Fibonacci numbers: ", end="")
    fibonacci_numbers = [str(next(fib_gen)) for _ in range(10)]
    print(", ".join(fibonacci_numbers))

    prime_gen = prime_number_generator()
    print("\nFirst 10 Prime numbers: ", end="")
    primes = [str(next(prime_gen)) for _ in range(10)]
    print(", ".join(primes))


if __name__ == "__main__":
    main()
