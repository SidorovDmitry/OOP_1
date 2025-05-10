import json

from src.category import Category
from src.product import Product

# from config import FILE_PATH_JSON


def read_file_json(filename=None):
    """Функция для чтения JSON-файла и обработки возможных ошибок при его открытии и чтении"""
    # logger.info(read_file.__doc__)
    try:

        with open(filename, "r", encoding="utf-8") as f:
            #             logger.info("Открытие JSON-файла")
            data = json.load(f)

        # Проверяем, что данные представляют собой список
        if not isinstance(data, list):
            #             logger.error("Ошибка обработки файла")
            return []

        return data
    except FileNotFoundError:
        #         logger.error(f"Файл не найден {e}")
        print(f"Файл не найден по пути: {filename}")
        return []
    except json.JSONDecodeError:
        #         logger.error(f"Ошибка при декодировании JSON из файла {e}")
        print(f"Ошибка при декодировании JSON из файла: {filename}")
        return []


def create_object_from_json(data):
    """Преобразования Данных из JSON в объекты"""

    categories = []
    for category_data in data:
        products = []
        for product_data in category_data["products"]:
            product = Product(
                name=product_data["name"],
                description=product_data["description"],
                price=product_data["price"],
                quantity=product_data["quantity"],
            )
            products.append(product)

        category = Category(name=category_data["name"], description=category_data["description"], products=products)
        categories.append(category)

    return categories


# if __name__ == "__main__":
#     # 1. Загружаем данные
#     data = read_file_json(FILE_PATH_JSON)
#     categories = create_object_from_json(data)  # Получаем список категорий
#
#     # 2. Выводим общую информацию
#     print(f"\nВсего категорий: {Category.category_count}")
#     print(f"Всего товаров: {Category.product_count}")
#
#     # 3. Выводим подробную информацию по каждой категории
#     for category in categories:  # Теперь categories определена
#         print(f"\nКатегория: {category.name}")
#         print(f"Описание: {category.description}")
#         print(f"Количество товаров: {len(category.products)}")
#
#         # Выводим все товары в категории
#         for product in category.products:
#             print(f"  {product}")
