# Task 1: Create the Inventory
inventory = {}
inventory.update({"banana": (20, 1.2)})
inventory.update({"apple": (10, 2.5)})

# Task 2: Add, Remove, Update Items
inventory.update({"mango": (15, 3.0)})
# this is one way we can remove dictionary elements...
inventory.pop("apple")
inventory.update({"banana": (25, 1.5)})

# Task 3: Display the Inventory
for key in inventory:
    print("Item:", key, "Quantity:", inventory[key][0], "Price:", inventory[key][1])
