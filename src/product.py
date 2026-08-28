class Product:
    """Класс для представления товара интернет-магазина."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Возвращает цену товара."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Устанавливает новую цену товара."""
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        """Создаёт объект Product из словаря."""
        return cls(**product_data)

    def __str__(self) -> str:
        """Возвращает строковое представление товара."""
        return (
            f"{self.name}, {self.price} руб. "
            f"Остаток: {self.quantity} шт."
        )

    def __add__(self, other: "Product") -> float:
        """Возвращает суммарную стоимость запасов двух товаров."""
        return self.price * self.quantity + other.price * other.quantity
