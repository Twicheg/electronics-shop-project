from csv import DictReader


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.85
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """ Создание экземпляра класса item. """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self):
        """ Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара."""
        return self.price * self.quantity

    def apply_discount(self):
        """ Применяет установленную скидку для конкретного товара. """
        self.price *= Item.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if len(name) <= 10:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []  # там был экзепляр от "Телефон" в мейне (через Инит записался)
        PATH = '../src/items.csv'
        for dict_ in DictReader(open(PATH, encoding='cp1251')):
            cls(dict_["name"], float(dict_['price']), int(dict_['quantity']))

    @staticmethod
    def string_to_number(string: str) -> int:
        if not string:
            return 0
        return int(float(string))
