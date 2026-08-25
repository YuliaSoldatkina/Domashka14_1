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
