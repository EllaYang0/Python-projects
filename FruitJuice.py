from Beverage import Beverage
class FruitJuice(Beverage):
    def __init__(self, ounces, price, fruits):
        super().__init__(ounces, price)
        self.fruits = fruits

    def getInfo(self):
        fruit_names = "/".join(self.fruits)
        base_info = super().getInfo()
        return f"{fruit_names} Juice, {base_info}"
