from typing import Union

from src.category import Category


class Order(Category):
    """Класс-наследник для категории «Заказ». Родительский класс Category.
    В котором будет ссылка на то, какой товар был куплен,
    количество купленного товара, а также итоговая стоимость.
    В заказе может быть указан только один товар."""

    quantity_purchased: int = 0
    total_cost: Union[int, float] = 0

    def __init__(self, name, description, products, quantity_purchased, total_cost):
        super().__init__(name, description, products)
        self.quantity_purchased = quantity_purchased
        self.total_cost = total_cost
