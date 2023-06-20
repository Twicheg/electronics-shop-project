from src.keyboard import KeyBoard
import pytest


@pytest.fixture
def keyboard():
    return KeyBoard('Dark Project KD87A', 9600, 5)


def test_keyboard(keyboard):
    assert keyboard.name == 'Dark Project KD87A'
    assert keyboard.language == 'EN'
    keyboard.change_lang()
    assert keyboard.language == "RU"
    keyboard.change_lang()
    assert keyboard.language == "EN"
    assert str(keyboard) == keyboard.name
    try:
        keyboard.language = 'CH'
    except AttributeError as e:
        assert str(e) == "property 'language' of 'KeyBoard' object has no setter"
