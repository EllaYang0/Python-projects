from Pizza import Pizza

class SpecialtyPizza(Pizza):

    def __init__(self, size, name):
        super().__init__(size)
        self.name = name
        if size == 'S':
            self.price = 12.00
        elif size == 'M':
            self.price = 14.00
        elif size == 'L':
            self.price = 16.00

    def getPizzaDetails(self):
        details = "SPECIALTY PIZZA\n"
        details += f"Size: {self.size}\n"
        details += f"Name: {self.name}\n"
        details += f"Price: ${self.price:.2f}\n"
        return details