import pytest
from src.keyboard import Keyboard

@pytest.fixture
def key_board():
    return Keyboard('Lenovo', 5000, 10)

def test_change_lang(key_board):
    key_board.change_lang()
    assert key_board.language == "RU"

def test__repr__(key_board):
    assert repr(key_board) == "Keyboard('Lenovo', 5000, 10)"

def test__str__(key_board):
    assert str(key_board) == 'Lenovo'

