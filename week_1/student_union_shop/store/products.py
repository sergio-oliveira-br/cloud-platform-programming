# week_1/student_union_shop/store/products.py

from week_1.student_union_shop.store.item import Item

class Cap(Item):
    """A representation of the Item"""
    def __init__(self):
        super().__init__("Cap", 5)

class Shirts(Item):
    """A representation of the Item"""
    def __init__(self):
        super().__init__("Shirts", 10)

class Hoodie(Item):
    """A representation of the Item"""
    def __init__(self):
        super().__init__("Hoodie", 20)

