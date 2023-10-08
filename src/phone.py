from src.item import Item

class Phone(Item):
    """
        Класс для представления смартфонов.
        """
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim


    @property
    def number_of_sim(self):
        return self.__number_of_sim


    @number_of_sim.setter
    def number_of_sim(self, new_number_of_sim):
        if type(new_number_of_sim) == int and new_number_of_sim>0:
            self.__number_of_sim = new_number_of_sim
        else:
            print('Количество физических SIM-карт должно быть целым числом больше нуля.')


    def __repr__(self):
        return super().__repr__()[:-1] + f", {self.__number_of_sim})"

