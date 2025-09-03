from main.main import check_price

def test_price_of_one_apple():
    item = "Apple"
    result = check_price(item)
    assert result == 50

def test_price_of_one_banana():
    item = "Banana"
    result = check_price(item)
    assert result == 30

def test_price_of_one_carrot():
    item = "Carrot"
    result = check_price(item)
    assert result == 20

def test_special_price_of_apples():
    item = "Apple"
    quantity = 3
    result = check_price(item, quantity)
    assert result == 130

#
# Item             Unit              Special
# Price            Price
# ---------------------------------------------------
# Apple         50                3 for 130
# Banana      30                2 for 45
# Carrots      20

