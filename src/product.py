class Product:
    """Создание класса Product """

    name: str        # Имя продукта
    description: str # Описание продукта
    price: float     # Цена продукта
    quantity: int    # Количество в наличии

    def __init__(self, name, description, price=0.0, quantity=0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity





