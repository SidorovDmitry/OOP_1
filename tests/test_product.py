from src.product import Product
from src.category import Category
from unittest.mock import patch


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