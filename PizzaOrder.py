from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
class PizzaOrder:
    def __init__(self, time):
        self.time = time
        self.pizzas = []

    def getTime(self):
        return self.time

    def setTime(self, time):
        self.time = time

    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def getOrderDescription(self):
        details = "******\n"
        details += f"Order Time: {self.time}\n"
        for pizza in self.pizzas:
            details += pizza.getPizzaDetails() + "\n----\n"
        total_price = sum(pizza.getPrice() for pizza in self.pizzas)
        details += f"TOTAL ORDER PRICE: ${total_price:.2f}\n"
        details += "******\n"
        return details
