from src.category import Category
from src.product import LawnGrass, Product, Smartphone


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

    smartphone1 = Smartphone(
        name="iPhone 15",
        description="Смартфон Apple",
        price=100000.0,
        quantity=10,
        efficiency=95.0,
        model="iPhone 15",
        memory=256,
        color="Черный",
    )
    smartphone2 = Smartphone(
        name="Samsung Galaxy S24",
        description="Смартфон Samsung",
        price=120000.0,
        quantity=5,
        efficiency=90.0,
        model="Galaxy S24",
        memory=512,
        color="Серый",
    )
    lawn_grass = LawnGrass(
        name="Газонная трава",
        description="Семена для газона",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый",
    )

    smartphone_category = Category(
        name="Смартфоны нового поколения",
        description="Современные смартфоны с высокой производительностью",
        products=[smartphone1, smartphone2],
    )
    garden_category = Category(
        name="Товары для сада",
        description="Товары для обустройства сада и газона",
        products=[lawn_grass],
    )

    print()
    print("Смартфон с дополнительными характеристиками:")
    print(smartphone1)
    print(f"Модель: {smartphone1.model}")
    print(f"Память: {smartphone1.memory} ГБ")
    print(f"Цвет: {smartphone1.color}")
    print(f"Производительность: {smartphone1.efficiency}")
    print()

    print("Газонная трава с дополнительными характеристиками:")
    print(lawn_grass)
    print(f"Страна-производитель: {lawn_grass.country}")
    print(f"Срок прорастания: {lawn_grass.germination_period}")
    print(f"Цвет: {lawn_grass.color}")
    print()

    print("Суммарная стоимость запасов двух смартфонов:")
    print(smartphone1 + smartphone2)
    print()

    print("Категория смартфонов:")
    print(smartphone_category)
    print()

    print("Категория товаров для сада:")
    print(garden_category)
