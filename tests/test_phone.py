import src.item as item
from src.phone import Phone

if __name__ == '__main__':
    phone1 = Phone("iPhone 12", 90000, 6, 1)
    # test __repr__
    assert repr(phone1) == "Phone('iPhone 12', 90000, 6, 1)"
    # test number_of_sim
    phone1.number_of_sim = '12'
    assert "Количество физических SIM-карт должно быть целым числом больше нуля."
    phone1.number_of_sim = 3.5
    assert "Количество физических SIM-карт должно быть целым числом больше нуля."