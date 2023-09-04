"""Здесь надо написать тесты с использованием pytest для модуля item."""
import src.item as item

if __name__ == '__main__':
    item.Item.pay_rate = 0,5
    item1 = item.Item("Смартфон", 20000, 30)
    # testing calculate_total_price
    assert item1.calculate_total_price() == 600000
    # testing apply_discount
    item1.apply_discount()
    assert item1.price == 20000 * item1.pay_rate