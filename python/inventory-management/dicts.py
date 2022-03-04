def create_inventory(items):
    """

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """
    item_inventory = {item: items.count(item) for item in items}

    return item_inventory


# print(create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"]))


def add_items(inventory, items):
    """

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """

    old_inventory = create_inventory(items)
    for stuff in inventory:
        if stuff in old_inventory:
            old_inventory[stuff] += inventory[stuff]
        else:
            old_inventory[stuff] = inventory[stuff]

    return old_inventory


# print(add_items({"coal": 1}, ["wood", "iron", "coal", "wood"]))
# print(add_items({"iron": 1, "diamond": 2}, ["iron", "wood", "wood"]))


def decrement_items(inventory, items):
    """

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """

    old_inventory = create_inventory(items)
    for stuff in inventory:
        inventory[stuff] -= old_inventory[stuff]
        if inventory[stuff] < 0:
            inventory[stuff] = 0

    return inventory


# print(
#     decrement_items(
#         {"wood": 2, "iron": 3, "diamond": 1},
#         ["wood", "wood", "wood", "iron", "diamond", "diamond"],
#     )
# )

# print(
#     decrement_items(
#         {"coal": 3, "diamond": 1, "iron": 5}, ["diamond", "coal", "iron", "iron"]
#     )
# )


def remove_item(inventory, item):
    """
    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """
    inventory.pop(item, "")

    return inventory


# print(remove_item({"coal": 2, "wood": 1, "diamond": 2}, "coal"))
# print(remove_item({"coal": 2, "wood": 1, "diamond": 2}, "gold"))


def list_inventory(inventory):
    """

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    new_inventory = {}
    for stuff in inventory:
        # print(inventory[stuff])
        if inventory[stuff] == 0:
            continue
        else:
            new_inventory[stuff] = inventory[stuff]
    new_inventory = {(thing, new_inventory[thing]) for thing in new_inventory}
    # for stuff in inventory:
    #     inventory[stuff] -= old_inventory[stuff]

    return list(new_inventory)


# print(list_inventory({"coal": 15, "diamond": 3, "wood": 67, "silver": 0}))
# print(list_inventory({"coal": 7, "wood": 11, "diamond": 2, "iron": 7, "silver": 0}))
