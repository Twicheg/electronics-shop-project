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
    assert item.price == 1000 * Item.pay_rate
    item.apply_discount()
    assert item.price == 1000 * Item.pay_rate * Item.pay_rate


def test_item_two(item):
    item.name = "Билли"
    assert item.name == "Билли"
    try:
        item.name = "Билли Боб Джонсон"  # len > 10
    except Exception:
        print('allright')
    #assert item.name == ""
    assert Item.string_to_number('0') == 0
    assert Item.string_to_number('3.99') == 3
    assert Item.string_to_number('') == 0
    assert Item.instantiate_from_csv() == 'Экземпляры из файла добавлены'
