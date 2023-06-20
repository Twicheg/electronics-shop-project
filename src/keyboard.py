from src.item import Item


class MixinLog:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        self.__language = 'EN'

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = "RU"
            return self
        else:
            self.__language = 'EN'
            return self


class KeyBoard(Item, MixinLog):
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    # @language.setter
    # def language(self, other_language):
    #     """Функция по инициализации языка"""
    #     if other_language in ["EN", "RU"]:
    #         self.__language = other_language
    #     else:
    #         raise AttributeError("property 'language' of 'KeyBoard' object has no setter")

    def __str__(self):
        return f'{self.name}'
