# Final Exam AIDI 2004 - Aman Bansal

class InventoryTracker:
    def __init__(self):
        self.inventory = {}

    def addItem(self, name, quantity):
        """Add a new item to the inventory with the given quantity."""
        self.inventory[name] = quantity
        print(f"Added '{name}' with quantity {quantity}.")
