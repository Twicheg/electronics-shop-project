from src.item import Item


class Mixin:
    def change_lang(self):
        if self._language == 'EN':
            self._language = "RU"
            return self
        elif self._language == "RU":
            self._language = 'EN'
            return self


class KeyBoard(Mixin, Item):
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        self._language = 'EN'

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, other_language):
        """Функция по инициализации языка"""
        if other_language in ["EN", "RU"]:
            self._language = other_language
        else:
            raise AttributeError("property 'language' of 'KeyBoard' object has no setter")

    def __str__(self):
        return f'{self.name}'
