from main.main import Cart, ItemType

# def test_price_of_one_apple():
#     item = "Apple"
#     result = check_price(item)
#     assert result == 50

# def test_price_of_one_banana():
#     item = "Banana"
#     result = check_price(item)
#     assert result == 30

# def test_price_of_one_carrot():
#     item = "Carrot"
#     result = check_price(item)
#     assert result == 20

# def test_special_price_of_apples():
#     item = "Apple"
#     quantity = 3
#     result = check_price(item, quantity)
#     assert result == 130

# def test_special_price_of_bananas():
#     item = "Banana"
#     quantity = 2
#     result = check_price(item, quantity)
#     assert result == 45

def test_price_of_one_apple():
    apples = ItemType("Apples")
    result = apples.get_price_per_unit()
    assert result == 50

def test_price_of_one_banana():
    apples = ItemType("Bananas")
    result = apples.get_price_per_unit()
    assert result == 40

def test_price_of_one_carrot():
    apples = ItemType("Carrots")
    result = apples.get_price_per_unit()
    assert result == 20

def test_special_price_of_apples():
    quantity = 3
    apples = ItemType("Apples", quantity)
    result = apples.get_total_price()
    assert result == 130

def test_special_price_of_bananas():
    quantity = 2
    bananas = ItemType("Bananas", quantity)
    result = bananas.get_total_price()
    assert result == 45

def test_add_item_to_cart():
    apples = ItemType("Apples")
    cart = Cart()
    cart.add_item(apples)

    assert cart.get_item(apples).name == "Apples"
    assert cart.get_item(apples).quantity == 1

def test_price_of_two_apples():
    quantity = 2
    apples = ItemType("Apples", quantity)
    result = apples.get_total_price()
    assert result == 100

def test_price_of_two_carrots():
    quantity = 8
    apples = ItemType("Carrots", quantity)
    result = apples.get_total_price()
    assert result == 160

def test_price_of_four_bananas():
    quantity = 4
    apples = ItemType("Bananas", quantity)
    result = apples.get_total_price()
    assert result == 90

def test_price_of_six_apples():
    quantity = 6
    apples = ItemType("Apples", quantity)
    result = apples.get_total_price()
    assert result == 260 