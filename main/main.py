specials = {
    "Apple": {
        "quantity": 3,
        "price": 130
    }
}


items = {
    "Apple": 50,
    "Banana": 30,
    "Carrot": 20,
}

def check_price(item, quantity = 1):
    if specials.get(item) and quantity == specials[item]["quantity"]:
        return specials[item]["price"]

    return items[item]