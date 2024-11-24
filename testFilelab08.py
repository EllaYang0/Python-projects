import pytest
from Car import Car
from CarInventoryNode import CarInventoryNode
from CarInventory import CarInventory

def test_car_class():
    car1 = Car("Tesla", "Model3", 2021, 50000)
    assert car1.make == "TESLA"
    assert car1.model == "MODEL3"
    assert car1.year == 2021
    assert car1.price == 50000
    assert str(car1) == "Make: TESLA, Model: MODEL3, Year: 2021, Price: $50000"

    car2 = Car("Tesla", "Model3", 2019, 48000)
    assert car1 > car2
    assert car2 < car1
    car3 = Car("Tesla", "ModelS", 2021, 80000)
    assert car3 > car1
    car4 = Car("Audi", "A3", 2021, 30000)
    assert car4 < car1
    assert car1 == Car("Tesla", "Model3", 2021, 50000)

def test_inventorynode():
    car1 = Car("Tesla", "Model3", 2021, 50000)
    node = CarInventoryNode(car1)
    assert node.getMake() == "TESLA"
    assert node.getModel() == "MODEL3"
    assert len(node.cars) == 1
    assert str(node) == "Make: TESLA, Model: MODEL3, Year: 2021, Price: $50000\n"

    car2 = Car("Tesla", "Model3", 2022, 60000)
    node.cars.append(car2)
    assert len(node.cars) == 2
    assert str(node) == ("Make: TESLA, Model: MODEL3, Year: 2021, Price: $50000\n"
                         "Make: TESLA, Model: MODEL3, Year: 2022, Price: $60000\n")

def test_inventory():
    inventory = CarInventory()
    car1 = Car("Tesla", "Model3", 2021, 50000)
    car2 = Car("Tesla", "ModelS", 2022, 90000)
    car3 = Car("Audi", "A4", 2020, 35000)
    inventory.addCar(car1)
    inventory.addCar(car2)
    inventory.addCar(car3)
    assert inventory.doesCarExist(car1) is True
    assert inventory.doesCarExist(Car("Audi", "A3", 2021, 30000)) is False

    assert inventory.inOrder().strip() == (
        "Make: AUDI, Model: A4, Year: 2020, Price: $35000\n"
        "Make: TESLA, Model: MODEL3, Year: 2021, Price: $50000\n"
        "Make: TESLA, Model: MODELS, Year: 2022, Price: $90000"
    )

    assert inventory.preOrder().strip() == (
        "Make: TESLA, Model: MODEL3, Year: 2021, Price: $50000\n"
        "Make: AUDI, Model: A4, Year: 2020, Price: $35000\n"
        "Make: TESLA, Model: MODELS, Year: 2022, Price: $90000"
    )

    assert inventory.postOrder().strip() == (
        "Make: AUDI, Model: A4, Year: 2020, Price: $35000\n"
        "Make: TESLA, Model: MODELS, Year: 2022, Price: $90000\n"
        "Make: TESLA, Model: MODEL3, Year: 2021, Price: $50000"
    )
    best_car = inventory.getBestCar("Tesla", "Model3")
    assert best_car.year == 2021 and best_car.price == 50000
    worst_car = inventory.getWorstCar("Tesla", "ModelS")
    assert worst_car.year == 2022 and worst_car.price == 90000
    assert inventory.getTotalInventoryPrice() == (50000 + 90000 + 35000)
