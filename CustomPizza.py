from Pizza import Pizza
class CustomPizza(Pizza):
    def __init__(self, size):
        super().__init__(size)
        self.topping = []
        if size == 'S':
            self.price = 8.00
        if size == 'M':
            self.price = 10.00
        if size == "L":
            self.price = 12.00

    def addTopping(self, topping):
        self.topping.append(topping)
        if self.size == 'S':
            self.price += 0.50
        elif self.size == 'M':
            self.price += 0.75
        elif self.size == 'L':
            self.price += 1.00

    def getPizzaDetails(self):
        details = "CUSTOM PIZZA\n" + f"Size: {self.size}\n" + f"Toppings:\n"
        if not self.topping:
            pass
        else:
            for topping in self.topping:
                details += f"\t+ {topping}\n"

        details += f"Price: ${self.price:.2f}\n"
        return details