from cli_app import greet


def test_greet():
    assert greet("Deepanshu") == "Hello, Deepanshu!"
    