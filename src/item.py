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
        """Метод-сеттер для установки атрибута name"""
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception("Длина наименования товара превышает 10 символов.")

    @classmethod
    def instantiate_from_csv(cls, PATH='src/items.csv'):
        "метод создания объектов из данных файла"
        cls.all = []  # там был экзепляр от "Телефон" в мейне (через Инит записался)
        for dict_ in DictReader(open(PATH, encoding='cp1251')):
            cls(dict_['name'], float(dict_['price']), int(dict_['quantity']))
        return len(cls.all)

    @staticmethod
    def string_to_number(string: str) -> int:
        "метод создания числового объекта из переданной строки"
        if not string:
            return 0
        return int(float(string))

    def __repr__(self):
        '''Метод отображения инфаормации в режиме отладки'''
        return f"{self.__class__.__name__}('{self.name.title()}', {self.price}, {self.quantity})"

    def __str__(self):
        '''Метод отображения для пользователя'''
        return f'{self.name.title()}'
