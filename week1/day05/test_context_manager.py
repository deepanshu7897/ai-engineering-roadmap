from pathlib import Path


def test_file_exists():
    assert Path("sample.txt").exists()