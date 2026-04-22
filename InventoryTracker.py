# Final Exam AIDI 2004 - Aman Bansal

class InventoryTracker:
    def __init__(self):
        self.inventory = {}

    def addItem(self, name, quantity):
        """Add a new item to the inventory with the given quantity."""
        self.inventory[name] = quantity
        print(f"Added '{name}' with quantity {quantity}.")

    def updateStock(self, item_name, new_quantity):
        """
        Update the quantity of an existing inventory item.
        If the item does not exist, it will be added with the new quantity.
        """
        self.inventory[item_name] = new_quantity
        print(f"Updated '{item_name}' to quantity {new_quantity}.")
