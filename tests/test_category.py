from src.category import Category
import pytest

def test_correct_category(input_data_bu_category):
    """Тест на корректность вывода с полными входными данными"""
    assert input_data_bu_category.name == "Смартфоны"
    assert input_data_bu_category.products == [("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)]
    assert input_data_bu_category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert input_data_bu_category.category_count == 1
    assert input_data_bu_category.product_count == 1

def test_category_edge_cases(input_data_bu_category):
    """Тест проверяет обработку граничных случаев."""
    # Проверка типов данных
    assert isinstance(input_data_bu_category.name, str)
    assert isinstance(input_data_bu_category.products, list)
    assert isinstance(input_data_bu_category.description, str)
    assert isinstance(input_data_bu_category.category_count, int)
    assert isinstance(input_data_bu_category.product_count, int)