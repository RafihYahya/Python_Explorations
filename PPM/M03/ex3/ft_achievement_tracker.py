"""
This module provides functionality for tracking user achievements.
"""


def main():
    """Main function to demonstrate achievement tracking and analysis."""

    print("=== Achievement Tracker System ===")
    alice_achievs = {
        'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob_achievs = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie_achievs = {
        'level_10', 'treasure_hunter', 'boss_slayer',
        'speed_demon', 'perfectionist'}
    print(f"alice_achievs: {alice_achievs}")
    print(f"bob_achievs: {bob_achievs}")
    print(f"charlie_achievs: {charlie_achievs}")
    print("=== Achievement Analytics ===\n")
    print(
        f"All unique achievements: "
        f"{ set.union(alice_achievs, bob_achievs, charlie_achievs)}"
        )
    unique_achievs = set.union(
        alice_achievs, bob_achievs, charlie_achievs)
    print(
        f"Total unique achievements: {len(unique_achievs)}\n"
        )
    print(
        f"Common to all players: "
        f"{set.intersection(alice_achievs, bob_achievs, charlie_achievs)}"
        )
    alice_unique = alice_achievs.difference(bob_achievs, charlie_achievs)
    bob_unique = bob_achievs.difference(alice_achievs, charlie_achievs)
    charlie_unique = charlie_achievs.difference(alice_achievs, bob_achievs)
    rare_achievements = set.union(alice_unique, bob_unique, charlie_unique)
    print(
        f"Rare achievements (1 player): "
        f"{rare_achievements}\n"
        )
    print(
        f"Alice vs Bob common: {set.intersection(alice_achievs, bob_achievs)}"
        )
    print(f"Alice unique: {set.difference(alice_achievs, bob_achievs)}")
    print(f"Bob unique: {set.difference(bob_achievs, alice_achievs)}")


if __name__ == "__main__":
    main()
