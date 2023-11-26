from abc import ABC, abstractmethod
from dataclasses import dataclass

print("------------Задание 1------------")


@dataclass
class Product:
    id: int
    name: str
    price: float


@dataclass
class Pizza(Product):
    topping: list
    spicy: str
    diameter: int


@dataclass
class Coffee(Product):
    volume: int
    size: str


class AbstractShop(ABC):
    @abstractmethod
    def add_product(self, product: Product):
        """
        Добавить товар
        """
    @abstractmethod
    def sell_product(self, product: Product):
        """
        Продать товар
        """

    @abstractmethod
    def all_product(self) -> Product:
        """
        Перечень товаров
        """


class NonProductError(ValueError):
    pass


class RealShop(AbstractShop):
    def __init__(self):
        self.products = []

    def is_valid(self, product: Product):
        if not isinstance(product, Product):
            raise NonProductError("Тип передаваемого значения должен быть Product")
        pass

    def add_product(self, product: Product):
        self.is_valid(product)
        self.products.append(product)

    def sell_product(self, product: Product):
        self.is_valid(product)
        self.products.remove(product)

    def all_product(self):
        return self.products


prod1 = Pizza(7820, "Маргарита", 14.50, ["cheese", "tomato"], "not spicy", 20)
prod2 = Coffee(520, "Латте", 4.50, 350, "M")

shop = RealShop()

shop.add_product(prod1)
shop.add_product(prod2)
print(shop.all_product())

shop.sell_product(prod2)
print(shop.all_product())


class Furniture(Product):
    pass


class Table(Furniture):
    type: str


class Chair(Furniture):
    chair_back: str


class Cupboard(Furniture):
    color: str


table = Table(1530, "Стол", 520)
chair = Chair(1823, "Стул", 100)
cupboard = Cupboard(1401, "Шкаф", 3450)

furniture_shop = RealShop()

furniture_shop.add_product(table)
furniture_shop.add_product(chair)
furniture_shop.add_product(cupboard)

print(furniture_shop.all_product())
furniture_shop.sell_product(table)
print(f"Продан товар: {table}")
print(furniture_shop.all_product())
