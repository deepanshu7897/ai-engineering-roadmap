from decorators import unstable_function


def test_retry():
    result = unstable_function()

    assert result == "Success"