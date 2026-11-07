from orders import apply_discount, is_large


def test_half_price():
    assert apply_discount(1000, 0.5) == 500


def test_small_order_is_not_large():
    assert not is_large(4500)
