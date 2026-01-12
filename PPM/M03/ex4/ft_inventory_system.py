"""A simple inventory management system module using a normalized data
structure.
"""


def main():
    """Run the main inventory management system program."""
    print("=== Player Inventory System ===\n")
    game_items = {
        "sword": {
            "name": "Sword",
            "type": "weapon",
            "rarity": "rare",
            "gold": 500
        },
        "potion": {
            "name": "Potion",
            "type": "consumable",
            "rarity": "common",
            "gold": 50
        },
        "shield": {
            "name": "Shield",
            "type": "armor",
            "rarity": "uncommon",
            "gold": 200
        },
        "magic_ring": {
            "name": "Magic Ring",
            "type": "accessory",
            "rarity": "rare",
            "gold": 500
        }
    }
    alice_inventory = {
        "sword": 1,
        "potion": 5,
        "shield": 1
    }
    bob_inventory = {
        "potion": 0,
        "magic_ring": 1
    }

    print("=== Alice's Inventory ===")
    item_total_gold = 0
    item_count = 0
    categories_str = ""

    for item_id, quantity in alice_inventory.items():
        item_blueprint = game_items[item_id]
        item_value = quantity * item_blueprint['gold']
        item_total_gold += item_value
        item_count += quantity
        print(f"{item_blueprint['name']} ({item_blueprint['type']}, "
              f"{item_blueprint['rarity']}): "
              f"{quantity}x @ {item_blueprint['gold']} gold each"
              f" = {item_value} gold")
        category_part = f"{item_blueprint['type']}({quantity})"
        if categories_str == "":
            categories_str = category_part
        else:
            categories_str = categories_str + ", " + category_part

    print(f"\nInventory value: {item_total_gold} gold")
    print(f"Item count: {item_count}\n")
    print(f"Categories: {categories_str}")

    print("\n=== Transaction: Alice gives Bob 2 potions ===")
    alice_inventory["potion"] -= 2
    bob_inventory["potion"] += 2
    print("Transaction successful!")

    print("\n=== Updated Inventories ===")
    print(f"Alice potions: {alice_inventory['potion']}")
    print(f"Bob potions: {bob_inventory['potion']}")

    print("\n=== Inventory Analytics ===")
    alice_total_g_i = [0, 0]
    for item_id, quantity in alice_inventory.items():
        item_blueprint = game_items[item_id]
        alice_total_g_i[0] += quantity * item_blueprint['gold']
        alice_total_g_i[1] += quantity
    print(f"Most valuable player: Alice ({alice_total_g_i[0]} gold)")
    print(f"Most items: Alice ({alice_total_g_i[1]} items)")

    rare_items_str = ""
    for item_id in alice_inventory:
        if game_items[item_id]["rarity"] == "rare":
            if rare_items_str == "":
                rare_items_str = game_items[item_id]["name"]
            else:
                rare_items_str = rare_items_str + ", " +  \
                    game_items[item_id]["name"]
    for item_id in bob_inventory:
        if game_items[item_id]["rarity"] == "rare":
            if rare_items_str == "":
                rare_items_str = game_items[item_id]["name"]
            else:
                rare_items_str = rare_items_str + ", " \
                    + game_items[item_id]["name"]
    print(f"Rarest items: {rare_items_str}")


if __name__ == "__main__":
    main()
