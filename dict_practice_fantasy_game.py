def displayInventory(inventory):
    print('Inventory'.upper().center(20,'='))
    total_items = 0
    for k, v in stuff.items():
        print(f"{str(v).ljust(5, '.')}{k[0].upper()}{k[1:].lower()}")
        total_items += v
    print(f'\nTotal number of items: {total_items}')


def addToInventary(inventory, added_items):
    new_stuff = {}
    for i in added_items:
        new_stuff.setdefault(i, added_items.count(i))
    for k, v in new_stuff.items():
        if k in inventory:
            inventory[k] += v
        else:
            inventory[k] = v
    return inventory


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventary(stuff, dragonLoot)

displayInventory(inv)