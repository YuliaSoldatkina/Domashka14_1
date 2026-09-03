import pytest

from src.product import (
    BaseProduct,
    LawnGrass,
    Product,
    Smartphone,
)


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


@pytest.fixture
def smartphone() -> Smartphone:
    """Создаёт тестовый смартфон."""
    return Smartphone(
        name="iPhone 15",
        description="Смартфон Apple",
        price=100000.0,
        quantity=10,
        efficiency=95.0,
        model="iPhone 15",
        memory=256,
        color="Черный",
    )


@pytest.fixture
def lawn_grass() -> LawnGrass:
    """Создаёт тестовую газонную траву."""
    return LawnGrass(
        name="Газонная трава",
        description="Семена для газона",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый",
    )


def test_smartphone_initialization(smartphone: Smartphone) -> None:
    """Проверяет создание смартфона и его наследование от Product."""
    assert isinstance(smartphone, Product)
    assert smartphone.name == "iPhone 15"
    assert smartphone.description == "Смартфон Apple"
    assert smartphone.price == 100000.0
    assert smartphone.quantity == 10
    assert smartphone.efficiency == 95.0
    assert smartphone.model == "iPhone 15"
    assert smartphone.memory == 256
    assert smartphone.color == "Черный"


def test_lawn_grass_initialization(lawn_grass: LawnGrass) -> None:
    """Проверяет создание газонной травы и её наследование от Product."""
    assert isinstance(lawn_grass, Product)
    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.description == "Семена для газона"
    assert lawn_grass.price == 500.0
    assert lawn_grass.quantity == 20
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == "7 дней"
    assert lawn_grass.color == "Зеленый"


def test_add_same_product_classes(smartphone: Smartphone) -> None:
    """Проверяет сложение двух смартфонов."""
    second_smartphone = Smartphone(
        name="Samsung Galaxy S24",
        description="Смартфон Samsung",
        price=120000.0,
        quantity=5,
        efficiency=90.0,
        model="Galaxy S24",
        memory=512,
        color="Серый",
    )

    assert smartphone + second_smartphone == 1600000.0


def test_add_different_product_classes(
    smartphone: Smartphone,
    lawn_grass: LawnGrass,
) -> None:
    """Проверяет запрет сложения товаров разных классов."""
    with pytest.raises(TypeError):
        smartphone + lawn_grass


def test_product_repr_mixin(capsys: pytest.CaptureFixture[str]) -> None:
    """Проверяет вывод миксина при создании продукта."""
    Product(
        name="Тестовый продукт",
        description="Описание продукта",
        price=1200,
        quantity=10,
    )

    captured = capsys.readouterr()

    assert "Product(" in captured.out
    assert "name=" in captured.out
    assert "description=" in captured.out
    assert "price=" in captured.out
    assert "quantity=" in captured.out


def test_base_product_is_abstract() -> None:
    """Проверяет, что BaseProduct нельзя создать напрямую."""
    with pytest.raises(TypeError):
        BaseProduct()


def test_smartphone_mixin_output(
    capsys: pytest.CaptureFixture[str],
) -> None:
    """Проверяет вывод миксина при создании смартфона."""
    Smartphone(
        "iPhone 15",
        "Смартфон Apple",
        100000.0,
        10,
        95.0,
        "iPhone 15",
        256,
        "Черный",
    )

    captured = capsys.readouterr()

    assert "Smartphone(" in captured.out
    assert "'iPhone 15'" in captured.out
    assert "100000.0" in captured.out


def test_lawn_grass_mixin_output(
    capsys: pytest.CaptureFixture[str],
) -> None:
    """Проверяет вывод миксина при создании газонной травы."""
    LawnGrass(
        "Газонная трава",
        "Семена для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )

    captured = capsys.readouterr()

    assert "LawnGrass(" in captured.out
    assert "'Газонная трава'" in captured.out
    assert "500.0" in captured.out
