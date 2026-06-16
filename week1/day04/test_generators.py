from generators import count_up_to


def test_generator():
    result = list(count_up_to(5))

    assert result == [1, 2, 3, 4, 5]