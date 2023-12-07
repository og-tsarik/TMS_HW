from abc import ABC, abstractmethod
from .Product import Product


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