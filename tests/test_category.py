import pytest

from src.category import Category
from src.product import LawnGrass, Product, Smartphone


@pytest.fixture(autouse=True)
def reset_category_counters() -> None:
    """Обнуляет счётчики категорий перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def first_product() -> Product:
    """Создаёт первый тестовый товар."""
    return Product(
        name="Смартфон",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def second_product() -> Product:
    """Создаёт второй тестовый товар."""
    return Product(
        name="Samsung Galaxy C23 Ultra",
        description="512GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=8,
    )


@pytest.fixture
def category(first_product: Product, second_product: Product) -> Category:
    """Создаёт тестовую категорию с двумя товарами."""
    return Category(
        name="Смартфоны",
        description=(
            "Смартфоны, как средство не только коммуникации, "
            "но и получения удовольствия от качественного фото"
        ),
        products=[first_product, second_product],
    )


def test_category_initialization(category: Category) -> None:
    """Проверяет корректность создания категории."""
    assert category.name == "Смартфоны"
    assert category.description == (
        "Смартфоны, как средство не только коммуникации, "
        "но и получения удовольствия от качественного фото"
    )


def test_products_getter(category: Category) -> None:
    """Проверяет строковое представление товаров категории."""
    expected_products = (
        "Смартфон, 180000.0 руб. Остаток: 5 шт.\n"
        "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 8 шт."
    )

    assert category.products == expected_products


def test_add_product(
    category: Category,
    first_product: Product,
) -> None:
    """Проверяет добавление товара и подсчёт товаров."""
    result = category.add_product(first_product)

    assert result is None
    assert Category.product_count == 3
    assert category.products.count("Смартфон") == 2


def test_category_count(first_product: Product) -> None:
    """Проверяет подсчёт количества категорий."""
    Category("Смартфоны", "Категория смартфонов", [first_product])
    Category("Телевизоры", "Категория телевизоров", [])

    assert Category.category_count == 2


def test_product_count(
    first_product: Product,
    second_product: Product,
) -> None:
    """Проверяет подсчёт общего количества товаров."""
    Category(
        "Смартфоны",
        "Категория смартфонов",
        [first_product, second_product],
    )
    Category("Телевизоры", "Категория телевизоров", [])

    assert Category.product_count == 2


def test_category_str(category: Category) -> None:
    """Проверяет строковое представление категории."""
    assert str(category) == "Смартфоны, количество продуктов: 13 шт."


def test_add_product_inheritors(category: Category) -> None:
    """Проверяет добавление наследников Product в категорию."""
    smartphone = Smartphone(
        name="iPhone 15",
        description="Смартфон Apple",
        price=100000.0,
        quantity=10,
        efficiency=95.0,
        model="iPhone 15",
        memory=256,
        color="Черный",
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

    category.add_product(smartphone)
    category.add_product(lawn_grass)

    assert Category.product_count == 4
    assert "iPhone 15" in category.products
    assert "Газонная трава" in category.products


def test_add_not_product_to_category(category: Category) -> None:
    """Проверяет запрет добавления объекта, не являющегося Product."""
    initial_product_count = Category.product_count

    with pytest.raises(TypeError):
        category.add_product("Это не товар")

    assert Category.product_count == initial_product_count
