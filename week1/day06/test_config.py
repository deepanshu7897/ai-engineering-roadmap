from config import app_config


def test_app_name():
    assert app_config.app_name == "AI Engineering Roadmap"


def test_environment():
    assert app_config.environment.value == "development"