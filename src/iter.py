class CategoryIterator:
    """Итератор для перебора товаров в категории"""

    def __init__(self, category):
        """Инициализатор"""
        self._category = category
        self._index = 0

    def __iter__(self):
        """Итератор"""
        return self

    def __next__(self):
        """Переход к следующему значение в итерации"""
        if self._index < len(self._category.products):
            product = self._category.products[self._index]
            self._index += 1
            return product
        raise StopIteration
