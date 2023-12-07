from dataclasses import dataclass


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


@dataclass
class Furniture(Product):
    pass


@dataclass
class Table(Furniture):
    type: str


@dataclass
class Chair(Furniture):
    chair_back: str


@dataclass
class Cupboard(Furniture):
    color: str


@dataclass
class Books(Product):
    pass


@dataclass
class Book(Books):
    author: str
    genre: str


@dataclass
class Magazine(Books):
    date: str


@dataclass
class Components(Product):
    pass


@dataclass
class Motherboard(Components):
    pass


@dataclass
class GraphicsCard(Components):
    pass