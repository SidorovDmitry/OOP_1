from abc import ABC, abstractmethod


class BaseCategory(ABC):
    """Базовый абстрактный класс, который станет родительским для класса категории."""

    @abstractmethod
    def add_product(self, *args, **kwargs):
        pass
