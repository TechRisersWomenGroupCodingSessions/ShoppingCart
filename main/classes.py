class ItemType():
    def __init__(self, name, price, quantity = 1):
        self.name = name
        
        self.quantity = quantity
        self.special_offers = {}

        if name == "Apple":
            self.price = 50
            self.special_offers = { 3: 130 }

        if name == "Banana":
            self.price = 40
            self.special_offers = { 2: 45 }

        if name == "Carrot":
            self.price = 20

    def get_price(item):
        if item.quantity in item.special_offers:
            return item.special_offers.get(item.quantity)

        return item.price

class Cart():
    def add_item(self, item):
        self.items.append(item)