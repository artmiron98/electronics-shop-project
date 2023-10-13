from src.keyboard import Keyboard

if __name__ == '__main__':
    kb = Keyboard('Lenovo', 5000, 10)
    # test change_lang
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang()
    assert str(kb.language) == "EN"
    # test __repr__
    assert repr(kb) == "Keyboard('Lenovo', 5000, 10)"
    # test __str__
    assert str(kb) == 'Lenovo'