class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.85
    all = []

    def __init__(self, name, price, quantity):
        """ Создание экземпляра класса item. """
        self.name = name
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
