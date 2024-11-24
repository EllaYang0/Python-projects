class DrinkOrder:
    def __init__(self):
        self.drinks = []

    def addBeverage(self, beverage):
        self.drinks.append(beverage)

    def getTotalOrder(self):
        order_info = "Order Items:\n"
        total_price = 0.0
        for drink in self.drinks:
            order_info = order_info + f"* {drink.getInfo()}\n"
            total_price = total_price + drink.getPrice()
        order_info = order_info + f"Total Price: ${total_price:.2f}"
        return order_info.strip()
