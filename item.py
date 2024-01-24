# item.py

class Item:
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight

    def __repr__(self):
        return f"Item({self.name}, {self.value}, {self.weight})"