import pytest

from src.product import Product


@pytest.fixture
def product() -> Product:
    """Создаёт тестовый товар."""
    return Product(
        name="Смартфон",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


def test_product_initialization(product: Product) -> None:
    """Проверяет корректность создания товара."""
    assert product.name == "Смартфон"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_new_product() -> None:
    """Проверяет создание товара из словаря."""
    product_data = {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8,
    }

    product = Product.new_product(product_data)

    assert product.name == "Iphone 15"
    assert product.description == "512GB, Gray space"
    assert product.price == 210000.0
    assert product.quantity == 8


def test_price_setter(product: Product) -> None:
    """Проверяет установку положительной цены."""
    product.price = 150000.0

    assert product.price == 150000.0


def test_price_setter_with_invalid_price(
    product: Product,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """Проверяет защиту от нулевой и отрицательной цены."""
    product.price = -100
    captured = capsys.readouterr()

    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"
    assert product.price == 180000.0

    product.price = 0
    captured = capsys.readouterr()

    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"
    assert product.price == 180000.0


def test_product_str(product: Product) -> None:
    """Проверяет строковое представление товара."""
    assert str(product) == "Смартфон, 180000.0 руб. Остаток: 5 шт."


def test_product_add(product: Product) -> None:
    """Проверяет сложение стоимости запасов двух товаров."""
    second_product = Product(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8,
    )

    assert product + second_product == 2580000.0
