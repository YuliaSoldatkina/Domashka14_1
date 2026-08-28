from src.category import Category
from src.product import Product


if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
    )
    product2 = Product(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
    )
    product3 = Product(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14,
    )

    category1 = Category(
        "Смартфоны",
        (
            "Смартфоны, как средство не только коммуникации, "
            "но и получения дополнительных функций для удобства жизни"
        ),
        [product1, product2, product3],
    )

    print("Товары в категории:")
    print(category1.products)
    print()

    print("Категория:")
    print(category1)
    print()

    print("Суммарная стоимость запасов первого и второго товаров:")
    print(product1 + product2)
    print()

    product4 = Product(
        '55" QLED 4K',
        "Фоновая подсветка",
        123000.0,
        7,
    )
    category1.add_product(product4)

    print("Товары после добавления нового товара:")
    print(category1.products)
    print()

    print("Категория после добавления товара:")
    print(category1)
    print()

    print("Количество объектов товаров во всех категориях:")
    print(category1.product_count)
    print()

    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )

    print("Товар, созданный через new_product:")
    print(new_product)
    print()

    new_product.price = 800
    print("Цена после установки значения 800:")
    print(new_product.price)

    new_product.price = -100
    print("Цена после попытки установить -100:")
    print(new_product.price)

    new_product.price = 0
    print("Цена после попытки установить 0:")
    print(new_product.price)
