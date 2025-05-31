def test_order_init(firs_product_order):
    assert firs_product_order.name == "Смартфоны"
    assert firs_product_order.description == "Заказ"
    assert firs_product_order.quantity_purchased == 2
    assert firs_product_order.total_cost == 210000
