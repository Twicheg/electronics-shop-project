from src.item import Item


class Phone(Item):
    """ Класс Phone , наследуемый от Item"""

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.__number_of_sim = number_of_sim
        Item.__init__(self, self.__name, self.price, self.quantity)

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if number_of_sim <= 0 or type(number_of_sim).__name__ != int.__name__:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        else:
            self.__number_of_sim = number_of_sim

    def __repr__(self):
        """Метод отображения инфаормации в режиме отладки """
        # str в Item
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"