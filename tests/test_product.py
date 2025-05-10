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
