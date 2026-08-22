from src.category import Category
from src.product import Product


product_1 = Product(
    name="Смартфон",
    description="256GB, Серый цвет, 200MP камера",
    price=180000.0,
    quantity=5,
)

product_2 = Product(
    name="Samsung Galaxy C23 Ultra",
    description="512GB, Серый цвет, 200MP камера",
    price=180000.0,
    quantity=8,
)

category = Category(
    name="Смартфоны",
    description=(
        "Смартфоны, как средство не только коммуникации, "
        "но и получения удовольствия от качественного фото"
    ),
    products=[product_1, product_2],
)

print(category.name)
print(category.description)
print(category.products)
print(Category.category_count)
print(Category.product_count)
