# week_1/student_union_shop/item.py

class Item:
    """A base class to represent an item in the store."""

    def __init__(self, name, price):
        """Constructor to initialise a new item."""
        self.name = name
        self.price = price

    def calculate_total_cost(self, quantity):
        """Calculates the total cost of a given quantity."""
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        return quantity * self.price