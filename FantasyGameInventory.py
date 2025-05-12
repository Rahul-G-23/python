def display_inventory(inventory):
    print("Inventory:")
    total_items = 0
    for item, count in inventory.items():
        print(f"{count} {item}")
        total_items += count
    print(f"Total number of items: {total_items}")

def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

if __name__ == "__main__":
    print(' Name: Rahul G \n USN: 1AY24AI088 \n Section: O')
    player_inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    display_inventory(player_inventory)

    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    print("\nYou found the following loot:")
    print(dragon_loot)

    player_inventory = add_to_inventory(player_inventory, dragon_loot)
    print("\nUpdated inventory:")
    display_inventory(player_inventory)
