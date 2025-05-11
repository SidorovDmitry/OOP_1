import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def input_data_bu_product() -> Product:
    """Входные данные для класса Product"""
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def input_incorrect_data() -> Product:
    """Не полные входные данные для класса Product"""
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий")


@pytest.fixture
def input_data_bu_category() -> Category:
    """Входные данные для класса Category"""
    product = "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products=[product],
    )


@pytest.fixture
def product_category() -> Category:
    """осуществляет возврат Класс Сategory"""
    products = [Product("Iphone 16PRO", "Smartphone", 107990, 2)]
    return Category("Мобильная электроника", "Smartphone", products)


@pytest.fixture
def category_item() -> Category:
    # Создаем список товаров (с одним товаром)
    products = [Product("Samsung QLED", "4K TV", 50000, 5)]
    return Category("Телевизоры", "Устройство отображения фильмов и тв-передач", products)
