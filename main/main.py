# specials = {
#     "Apple": {
#         "quantity": 3,
#         "price": 130
#     },
#     "Banana": {
#         "quantity": 2,
#         "price": 45
#     }
# }

# items = {
#     "Apple": 50,
#     "Banana": 30,
#     "Carrot": 20,
# }

# def check_price(item, quantity = 1):
#     if specials.get(item) and quantity == specials[item]["quantity"]:
#         return specials[item]["price"]

#     return items[item]

class ItemType():
    def __init__(self, name, quantity = 1):
        self.name = name
        self.quantity = quantity
        self.special_offers = {}

        if name == "Apples":
            self.price_per_unit = 50
            self.special_offers = { 3: 130 }

        if name == "Bananas":
            self.price_per_unit = 40
            self.special_offers = { 2: 45 }

        if name == "Carrots":
            self.price_per_unit = 20

    def get_price_per_unit(self):
        return self.price_per_unit
    
    def get_total_price(self):
        for offer_quantity in self.special_offers:
            if self.quantity >= offer_quantity:
                
                offer_sets = self.quantity // offer_quantity
                remaining_items = self.quantity % offer_quantity
                
                offer_price = self.special_offers[offer_quantity] * offer_sets
                regular_price = remaining_items * self.price_per_unit
                
                return offer_price + regular_price
                
        return self.price_per_unit * self.quantity

class Cart():
    def __init__(self):
        self.items = []

    def get_item(self, obj):
        index = self.items.index(obj)
        return self.items[index]
    
    def add_item(self, obj):
        self.items.append(obj)