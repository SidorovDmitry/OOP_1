from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый абстрактный класс, который станет родительским для класса продуктов."""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass
