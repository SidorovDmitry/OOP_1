from src.category import Category
from src.product import Product


def test_product_category(product_category):
    """Проверка имеющегося вывода продукта"""

    assert product_category.name == "Мобильная электроника"
    assert product_category.description == "Smartphone"
    assert Category.category_count == 1
    assert Category.product_count == 1


def test_wrong_product_category(product_category):
    """Проверка вывода отсутствующего продукта"""

    assert product_category.name != "Спорт инвентарь"
    assert product_category.description != "Scooter"
    assert Category.category_count != 3
    assert Category.product_count != 0

def test_category_edge_cases(input_data_bu_category):
    """Тест проверяет обработку граничных случаев."""
    # Проверка типов данных
    assert isinstance(input_data_bu_category.name, str)
    # assert isinstance(input_data_bu_category.products, list)
    assert isinstance(input_data_bu_category.description, str)
    assert isinstance(input_data_bu_category.category_count, int)
    assert isinstance(input_data_bu_category.product_count, int)


def test_category_incorrect(category_item):
    """Тест некорректных значений категории."""
    assert category_item.name != "Смартфоны"
    assert category_item.description != "Устройство связи"
    assert len(category_item.products) != 0
    assert Category.category_count != 0
    assert Category.product_count != 0


def test_add_product_increases_count(category_item):
    """Тест, что add_product увеличивает счетчик товаров"""
    initial_count = Category.product_count
    new_product = Product("Ноутбук", "Игровой", 150000, 5)

    category_item.add_product(new_product)

    assert len(category_item._Category__products) == 2 # type: ignore
    assert Category.product_count == initial_count + 1


def test_add_product_correctly_adds(category_item):
    """Тест, что add_product корректно добавляет продукт"""
    new_product = Product("Смартфон", "Android", 80000, 10)

    category_item.add_product(new_product)

    assert category_item._Category__products[-1] == new_product # type: ignore


def test_products_property_returns_string(category_item):
    """Тест, что свойство products возвращает строку"""
    assert isinstance(category_item.products, str)


def test_products_property_format(category_item):
    """Тест формата возвращаемой строки"""
    result = category_item.products
    expected = "Samsung QLED, 50000 руб. Остаток: 5 шт.\n"
    assert result == expected