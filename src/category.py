class Category:
    """Создание класса категории """

    name: str          # Имя
    description: str   # Описание
    products: list     # Список товаров категории
    category_count = 0 # Количество категорий
    product_count = 0  # Количество товаров

    def __init__(self, name, description, products ):
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0