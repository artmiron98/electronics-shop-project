import csv
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    @property
    def get_name(self):
        return self.__name

    @get_name.setter
    def set_name(self, name):
        if len(name) >= 10:
            self.name = name[:10]
        else:
            self.name = name



    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate


    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise TypeError("Складывать можно только объекты классов с родительским классом Item")

    @classmethod
    def instantiate_from_csv(cls, file):
        """Создание объектов из данных файла"""
        Item.all.clear()
        with open(file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cls(row['name'], row['price'], row['quantity'])


    @staticmethod
    def string_to_number(string):
        """Возвращающает число из числа-строки"""
        return int(float(string))
