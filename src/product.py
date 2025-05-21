class Product:
    """Создание класса Product"""

    name: str  # Имя продукта
    description: str  # Описание продукта
    price: float  # Цена продукта
    quantity: int  # Количество в наличии

    def __init__(self, name, description, price=0.0, quantity=0):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, products_dict, products_list):
        """
        Добавляет новый продукт в список или обновляет существующий:
        - Если продукт с таким именем найден, увеличивает quantity, а цену делает максимальной.
        - Если не найден - добавляет новый продукт.
        """
        name = products_dict["name"]
        description = products_dict["description"]
        price = float(products_dict["price"])
        quantity = int(products_dict["quantity"])

        for product in products_list:
            if product.name == name:
                product.quantity += quantity
                product.price = max(product.price, price)
                return product

        new_product = cls(name=name, description=description, price=price, quantity=quantity)
        products_list.append(new_product)
        return new_product

    @property  # type: ignore
    def price(self):
        """Вызов цены в приватном статусе"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Корректор цены приватного статуса"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            answer = input(
                f"Новая цена {new_price} ниже текущей {self.__price}. Подтвердите изменение (y/n): "
            ).lower()
            if answer != "y":
                print("Изменение цены отменено")
                return

        self.__price = new_price
        print(f"Цена успешно изменена на {self.__price}")

    def __str__(self):
        """Метод отображения информации об объекте класса для пользователя"""

        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Метод сложения продуктов, считающий их полную стоимость"""

        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product")

        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    """Класс «Смартфон» (Smartphone) расширен атрибутами: производительность (efficiency), модель (model),
    объем встроенной памяти (memory), цвет (color)."""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        return self.price + other.price


class LawnGrass(Product):
    """Класс «Трава газонная» (LawnGrass) расширен атрибутами: страна - производитель( country), срок
    прорастания(germination_period), цвет(color)."""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        return self.price + other.price
