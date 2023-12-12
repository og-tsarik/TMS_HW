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
    def __init__(self):
        self.products = []

    def is_valid(self, product: Furniture):
        if not isinstance(product, Furniture):
            raise NonProductError("Тип передаваемого значения должен быть Furniture")
        pass

    def add_product(self, product: Furniture):
        self.is_valid(product)
        self.products.append(product)

    def sell_product(self, product: Furniture):
        self.is_valid(product)
        self.products.remove(product)

    def all_product(self) -> list[Furniture]:
        return self.products
    pass


class BookShop(AbstractShop):
    def __init__(self):
        self.products = []

    def is_valid(self, product: Books):
        if not isinstance(product, Books):
            raise NonProductError("Тип передаваемого значения должен быть Books")
        pass

    def add_product(self, product: Books):
        self.is_valid(product)
        self.products.append(product)

    def sell_product(self, product: Books):
        self.is_valid(product)
        self.products.remove(product)

    def all_product(self) -> list[Books]:
        return self.products
    pass


class CompShop(AbstractShop):
    def __init__(self):
        self.products = []

    def is_valid(self, product: Components):
        if not isinstance(product, Components):
            raise NonProductError("Тип передаваемого значения должен быть Components")
        pass

    def add_product(self, product: Components):
        self.is_valid(product)
        self.products.append(product)

    def sell_product(self, product: Components):
        self.is_valid(product)
        self.products.remove(product)

    def all_product(self) -> list[Components]:
        return self.products
    pass
