import pytest

from src.category import Category
from src.product import Product


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
        description="Смартфоны, как средство не только коммуникации, "
        "но и получения удовольствия от качественного фото",
        products=[first_product, second_product],
    )


def test_category_initialization(category: Category) -> None:
    """Проверяет корректность создания категории."""
    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, "
        "но и получения удовольствия от качественного фото"
    )
    assert len(category.products) == 2


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
