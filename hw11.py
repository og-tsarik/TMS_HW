print("------------Задание 1------------")


class Soda:
    def __init__(self, add=None):
        self.add = add

    def show_my_drink(self):
        if self.add is None:
            print("Обычная газировка")
        else:
            print("Газировка и", self.add)


drink1 = Soda("Лёд")
drink1.show_my_drink()
drink2 = Soda()
drink2.show_my_drink()

print("------------Задание 2------------")


class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if isinstance(self.a, (int, float)) and isinstance(self.b, (int, float)) and isinstance(self.c, (int, float)):
            if self.a >= 0 and self.b >= 0 and self.c >= 0:
                if self.a + self.b > self.c and self.b + self.c > self.a and self.c + self.a > self.b:
                    print("Ура, можно построить треугольник!")
                else:
                    print("Жаль, но треугольник не сделать.")
            else:
                print("С отрицательными числами ничего не выйдет!")
        else:
            print("Нужно вводить только числа!")


triangle1 = TriangleChecker(5, 4, 1)
triangle1.is_triangle()
triangle2 = TriangleChecker("4", 3, 1)
triangle2.is_triangle()
triangle3 = TriangleChecker(3, -2, 3)
triangle3.is_triangle()
triangle4 = TriangleChecker(4, 7, 0)
triangle4.is_triangle()
triangle5 = TriangleChecker(4, 3, 2)
triangle5.is_triangle()

print("------------Задание 3------------")


class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return 2.205 * self.__kg

    def set_kg(self, kg: int | float):
        if type(kg) == int or type(kg) == float:
            self.__kg = kg

    def get_kg(self):
        return self.__kg


weight1 = KgToPounds(1)
print(weight1.to_pounds())
weight2 = KgToPounds(2)
print(weight2.to_pounds())

weight3 = KgToPounds(5)
print(weight3.get_kg())
weight3.set_kg(10)


class KgToPounds2:
    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return 2.205 * self.__kg

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, kg):
        if type(kg) == int or type(kg) == float:
            self.__kg = kg


weight4 = KgToPounds2(10)
print(weight4.to_pounds())

print("------------Задание 4------------")


class RealString:
    def __init__(self, string):
        self.string = string

    def __len__(self):
        return len(self.string)

    def __eq__(self, other):
        return len(self.string) == len(other)

    def __gt__(self, other):
        return len(self.string) > len(other)

    def __lt__(self, other):
        return len(self.string) < len(other)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)


string1 = RealString("Яблоко")
string2 = RealString("Apple")
print(string1 == string2)
print(string1 < string2)
print(string1 > string2)
print(string1 <= string2)
print(string1 >= string2)


print("------------Задание 5------------")


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def str(self):
        return f"Прямоугольник с шириной {self.width} и высотой {self.height}"

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.height + self.width) * 2

    @property
    def is_square(self):
        if self.width == self.height:
            return True
        else:
            return False


rect1 = Rectangle(5, 4)
print(rect1.str(), rect1.get_area(), rect1.get_perimeter(), rect1.is_square)
rect2 = Rectangle(6, 6)
print(rect2.str(), rect2.get_area(), rect2.get_perimeter(), rect2.is_square)

print("------------Задание 6------------")


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def str(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}"

    @property
    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    @staticmethod
    def is_adult(age):
        if age >= 18:
            return True
        else:
            return False

    @classmethod
    def create_from_string(cls, s):
        name, age, gender = s.split("-")
        return cls(name, age, gender)


person1 = Person("Max", 27, "Male")
print(person1.str())
print(person1.get_name)
print(person1.is_adult(person1.age))
person2 = Person.create_from_string("Karina-18-Female")
print(person2.str())
