import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def item():
    return Item("Смартфон", 1000, 2)


@pytest.fixture
def phone():
    return Phone("Самсунг", 1000, 3, 3)


def test_phone(phone):
    assert phone.name == "Самсунг"
    assert phone.price == 1000
    assert phone.quantity == 3
    assert phone.calculate_total_price() == 3000
    assert phone.number_of_sim == 3


def test_str(phone):
    assert str(phone) == "Самсунг"


def test_repr(phone):
    assert repr(phone) == "Phone('Самсунг', 1000, 3, 3)"


def test_add(phone, item):
    assert item + phone == 5
    assert phone + phone == 6


def test_name(phone):
    try:
        phone.name = 'что-то больше 10 символов'
    except Exception as e:
        assert str(e) == "Длина наименования товара превышает 10 символов."


def test_setter(phone):
    try:
        phone.number_of_sim = -10
    except ValueError as e:
        assert str(e) == 'Количество физических SIM-карт должно быть целым числом больше нуля.'
    phone.number_of_sim = 5
    assert phone.number_of_sim == 5
