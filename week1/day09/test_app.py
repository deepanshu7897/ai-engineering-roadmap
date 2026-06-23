from app import process_order


def test_process_order():
    assert process_order(101) == "Order 101 processed"