from .basicshop import AbstractShop
from .Product import Product, Furniture, Books, Components
from .exception import NonProductError


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

    def all_product(self) -> list[Product]:
        return self.products


class FurnitureShop(AbstractShop):
    pass

class BookShop(AbstractShop):
    pass


class CompShop(AbstractShop):
    pass


