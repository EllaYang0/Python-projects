from Beverage import Beverage
from FruitJuice import FruitJuice
from Coffee import Coffee
from DrinkOrder import DrinkOrder
def test_beverage():
    b2 = Beverage(20, 20.5)
    assert b2.getOunces() == 20
    assert b2.getPrice() == 20.5
    b2.updateOunces(30)
    assert b2.getOunces() == 30
    b2.updatePrice(29)
    assert b2.getPrice() == 29
    assert b2.getInfo() == "30 oz, $29.00"

def test_Coffee():
    c2 = Coffee(10, 4.0, "Americano")
    assert c2.getInfo() == "Americano Coffee, 10 oz, $4.00"

def test_FruitJuice():
    d2 = FruitJuice(20, 6.7, ["Banana", "Grape"])
    assert d2.getInfo() == "Banana/Grape Juice, 20 oz, $6.70"

def test_DrinkOrder():
    c3 = Coffee(11, 5.5, "Mocha")
    juice2 = FruitJuice(21, 7.8, ["Guava", "Orange"])
    order2 = DrinkOrder()
    order2.addBeverage(c3)
    order2.addBeverage(juice2)
    assert order2.getTotalOrder() == f"Order Items:\n* Mocha Coffee, 11 oz, $5.50\n* Guava/Orange Juice, 21 oz, $7.80\nTotal Price: $13.30"


