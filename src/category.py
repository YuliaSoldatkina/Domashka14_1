from src.product import Product


class Category:
    """Класс для представления категории товаров."""

    category_count = 0
    product_count = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: list[Product],
    ) -> None:
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """Добавляет товар в категорию."""
        if not isinstance(product, Product):
            raise TypeError(
                "В категорию можно добавлять только товары и их наследников"
            )

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает товары категории строкой."""
        return "\n".join(str(product) for product in self.__products)

    def __str__(self) -> str:
        """Возвращает строковое представление категории."""
        total_quantity = sum(product.quantity for product in self.__products)

        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def average_price(self) -> float:
        """Возвращает средний ценник товаров в категории."""
        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0.0
