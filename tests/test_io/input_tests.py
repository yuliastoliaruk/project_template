import pytest
import app.io.input as input


def test_read_file():
    results = input.read_file('data/input.txt')
    with open('data/input.txt') as f:
        data = f.read()
    assert results == data


def test_read_file_error():
    with pytest.raises(FileNotFoundError):
        input.read_file('no_file')