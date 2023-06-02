import pytest
from src.item import Item


@pytest.fixture
def item():
    return Item("Смартфон", 1000, 2)


def test_item(item):
    assert item.name == "Смартфон"
    assert item.price == 1000
    assert item.quantity == 2
    assert item.calculate_total_price() == 2000
    item.apply_discount()
    assert item.price == 1000 * 0.85
    item.apply_discount()
    assert item.price == 1000 * 0.85 * 0.85