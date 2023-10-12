from src.keyboard import Keyboard

if __name__ == '__main__':
    kb = Keyboard('LaLaLa', 5000, 10)
    assert str(kb) == "LaLaLa"
    assert str(kb.language) == "EN"
    #
    kb.change_lang()
    assert str(kb.language) == "RU"
    #
    # Сделали EN -> RU -> EN
    kb.change_lang()
    assert str(kb.language) == "EN"
    assert repr(kb) == "Keyboard('LaLaLa', 5000, 10)"