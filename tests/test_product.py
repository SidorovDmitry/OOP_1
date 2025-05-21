from unittest.mock import patch
import pytest
from src.category import Category
from src.product import Product, Smartphone, LawnGrass


def test_out_data_product(input_data_bu_product):
    """Тест на корректность вывода из объекта класса Product"""

    assert input_data_bu_product.name == "Samsung Galaxy S23 Ultra"
    assert input_data_bu_product.price == 180000.0
    assert input_data_bu_product.description == "256GB, Серый цвет, 200MP камера"
    assert input_data_bu_product.quantity == 5


def test_incorrect_output(input_incorrect_data):
    """Тест на некорректный ввод данных"""

    assert input_incorrect_data.name == "Xiaomi Redmi Note 11"
    assert input_incorrect_data.description == "1024GB, Синий"
    assert input_incorrect_data.price == 0.0
    assert input_incorrect_data.quantity == 0


def test_price_setter_lower_price_confirm_yes(product_category):
    with patch("builtins.input", return_value="y"):
        product_category.price = 100000
    assert product_category.price == 100000


def test_category_initialization(product_category):
    assert product_category.name == "Мобильная электроника"
    assert product_category.description == "Smartphone"
    assert Category.category_count >= 1
    assert Category.product_count >= 1


def test_product_price_setter_negative():
    """Тест, что цена не может быть отрицательной"""
    product = Product("Тест", "Тест", 100, 1)
    product.price = -50  # Попытка установить отрицательную цену
    assert product.price == 100  # Цена не должна измениться


def test_new_product_merges_duplicates():
    """Тест, что new_product объединяет дубликаты"""
    products_list = []
    product_data1 = {"name": "Телефон", "description": "Смартфон", "price": "50000", "quantity": "10"}
    product1 = Product.new_product(product_data1, products_list)

    product_data2 = {"name": "Телефон", "description": "Смартфон", "price": "55000", "quantity": "5"}
    product2 = Product.new_product(product_data2, products_list)

    assert product1 == product2  # Должен вернуться тот же объект
    assert product1.quantity == 15  # Количество суммируется
    assert product1.price == 55000  # Цена берется максимальная


def test_new_product_creates_new_if_no_duplicate():
    """Тест, что new_product создает новый продукт, если дубликата нет"""
    products_list = []
    product_data = {"name": "Ноутбук", "description": "Игровой", "price": "100000", "quantity": "3"}
    product = Product.new_product(product_data, products_list)

    assert product in products_list  # Продукт должен быть добавлен в список
    assert len(products_list) == 1


def test_smartfone_check(smartphone_item):
    """Тест инициализации объекта класса Smartphone"""
    assert smartphone_item.name == "Iphone"
    assert smartphone_item.description == "Американский Смартфон"
    assert smartphone_item.price == 12000
    assert smartphone_item.efficiency == 20.0
    assert smartphone_item.model == "16 PRO"
    assert smartphone_item.memory == 512
    assert smartphone_item.color == "Gold"


def test_lawngrass_item_check(lawngrass_item):
    """Тест инициализации объекта класса LawnGrass"""
    assert lawngrass_item.name == "Зелёный ковер"
    assert lawngrass_item.description == "Газонная трава"
    assert lawngrass_item.price == 1000
    assert lawngrass_item.quantity == 500
    assert lawngrass_item.country == "Россия"
    assert lawngrass_item.germination_period == "3 месяца"
    assert lawngrass_item.color == "Зеленая"


def test_add_method_smartphone(smartphone_item):
    """Тест сложения объектов класса Smartphone"""
    smartphone_new = Smartphone("Iphone", "512GB, Красный цвет, 12MP камера", 300000.0, 4, 19.0, "16Pro", 32, "Red")
    smartphone_sum = smartphone_new + smartphone_item
    assert smartphone_sum


def test_add_method_smartphone_rise_call():
    """Тест вызова исключения при сложении вместо продукта или его наследников любой другой объект."""
    with pytest.raises(TypeError):
        smartphone1 = Smartphone(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 11.0, "s20", 8, "green"
        )
        smartphone2 = "Неправильная строка"
        smartphone_sum = smartphone1 + smartphone2
        assert smartphone_sum


def test_add_method_lawngrass(lawngrass_item):
    """Тест сложения объектов класса LawnGrass"""
    lawngrass_new = LawnGrass("Лесной ковёр", "Газонная трава", 1000, 30, "Россия", "2 месяца", "Зеленая")

    lawngrass_sum = lawngrass_new + lawngrass_item
    assert lawngrass_sum


def test_add_method_lawngrass_rise_call():
    """Тест вызова исключения при сложении вместо продукта или его наследников любой другой объект."""
    with pytest.raises(TypeError):
        lawngrass_1 = LawnGrass("Зеленые ковер", "Трава для гольфа", 1500, 2, "Новая Зеландия", "1 неделя", "Синяя")
        lawngrass_2 = 1
        lawngrass_sum = lawngrass_1 + lawngrass_2
        assert lawngrass_sum


def test_add_method_rise_call(smartphone_item, lawngrass_item):
    """Тест вызова исключения при сложении продуктов с разных категорий."""
    with pytest.raises(TypeError):
        product1 = smartphone_item
        product2 = lawngrass_item
        product3 = "smartphone"

        assert product1 + product2
        assert product1 + product3
