from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для продуктов."""

    @abstractmethod
    def __str__(self) -> str:
        """Возвращает строковое представление продукта."""
        pass


class PrintMixin:
    """Миксин для вывода информации о создании объекта."""

    def __init__(self, *args, **kwargs) -> None:
        parameters = ", ".join(
            [repr(argument) for argument in args]
            + [
                f"{key}={value!r}"
                for key, value in kwargs.items()
            ]
        )
        print(f"{self.__class__.__name__}({parameters})")
        super().__init__()

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта."""
        parameters = ", ".join(
            f"{key}={value!r}" for key, value in self.__dict__.items()
        )
        return f"{self.__class__.__name__}({parameters})"


class Product(PrintMixin, BaseProduct):
    """Класс для представления товара интернет-магазина."""

    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
    ) -> None:
        super().__init__(
            name=name,
            description=description,
            price=price,
            quantity=quantity,
        )
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        if self.quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

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
        if type(self) is not type(other):
            raise TypeError(
                "Складывать можно только товары одного класса"
            )

        return (
            self.price * self.quantity
            + other.price * other.quantity
        )


class Smartphone(Product):
    """Класс для представления смартфона."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для представления газонной травы."""

    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
            country: str,
            germination_period: str,
            color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
