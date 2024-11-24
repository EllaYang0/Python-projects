import pytest
from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder
from OrderQueue import OrderQueue, QueueEmptyException

def test_pizza():
    pizza = Pizza("M")
    assert pizza.getSize() == "M"
    assert pizza.getPrice() == 0.0

    pizza.setPrice(15.00)
    assert pizza.getPrice() == 15.00

    pizza.setSize("L")
    assert pizza.getSize() == "L"

def test_custompizza():
    custom_pizza = CustomPizza("M")
    assert custom_pizza.getSize() == "M"
    assert custom_pizza.getPrice() == 10.00
    custom_pizza.addTopping("Mushrooms")
    assert custom_pizza.getPrice() == 10.75
    custom_pizza.addTopping("Pepperoni")
    assert custom_pizza.getPrice() == 11.50
    details = custom_pizza.getPizzaDetails()
    assert "CUSTOM PIZZA" in details
    assert "Size: M" in details
    assert "Toppings:" in details
    assert "+ Mushrooms" in details
    assert "+ Pepperoni" in details
    assert "Price: $11.50" in details

def test_specialtypizza():
    specialty_pizza = SpecialtyPizza("L", "Margherita")
    assert specialty_pizza.getSize() == "L"
    assert specialty_pizza.getPrice() == 16.00
    details = specialty_pizza.getPizzaDetails()
    assert "SPECIALTY PIZZA" in details
    assert "Size: L" in details
    assert "Name: Margherita" in details
    assert "Price: $16.00" in details

def test_pizzaorder():
    order = PizzaOrder("12:30")
    assert order.getTime() == "12:30"

    custom_pizza = CustomPizza("M")
    specialty_pizza = SpecialtyPizza("L", "Margherita")
    order.addPizza(custom_pizza)
    order.addPizza(specialty_pizza)

    order_description = order.getOrderDescription()
    assert "Order Time: 12:30" in order_description
    assert "CUSTOM PIZZA" in order_description
    assert "SPECIALTY PIZZA" in order_description
    assert "TOTAL ORDER PRICE: $27.50" in order_description

def test_queue():
    order_queue = OrderQueue()
    order1 = PizzaOrder("12:00")
    order1.addPizza(CustomPizza("M"))
    order_queue.addOrder(order1)
    order2 = PizzaOrder("12:15")
    order2.addPizza(SpecialtyPizza("L", "Pepperoni"))
    order_queue.addOrder(order2)
    assert order_queue.processNextOrder() == order1.getOrderDescription()
    assert order_queue.processNextOrder() == order2.getOrderDescription()
    with pytest.raises(QueueEmptyException):
        order_queue.delMin()
