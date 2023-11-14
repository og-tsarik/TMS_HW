print("------------Задание 1------------")


class Auto:
    def __init__(self, brand, age: int, mark, color=None, weight: float = None):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print("move")

    @staticmethod
    def stop():
        print("stop")

    def birthday(self):
        return self.age + 1


print("------------Задание 2------------")


class Truck(Auto):
    def __init__(self, brand, age: int, mark, max_load, *args, **kwargs):
        super().__init__(brand, age, mark, *args, **kwargs)
        self.max_load = max_load

    def move(self):
        print("attention")
        super().move()

    @staticmethod
    def load():
        print("load")


class Car(Auto):
    def __init__(self, brand, age: int, mark, max_speed, *args, **kwargs):
        super().__init__(brand, age, mark, *args, **kwargs)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print("max speed is", self.max_speed)


truck1 = Truck("MAZ", 7, "4570", 15800)
truck2 = Truck("MAZ", 12, "2107", 12000, color="yellow")

car1 = Car("Honda", 5, "Avancier", 260, color="white")
car2 = Car("BMW", 2, "X7", 220, color="green", weight=1700)

truck1.move()
print(truck2.brand, truck2.age, truck2.mark, truck2.max_load)
print(car1.birthday())
print(car1.max_speed)
car2.stop()
