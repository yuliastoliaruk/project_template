import pytest
import app.io.input as input
import pandas as pd


def test_read_file():
    results = input.read_file('data/input.txt')
    with open('data/input.txt') as f:
        data = f.read()
    assert results == data


def test_read_file_error():
    with pytest.raises(FileNotFoundError):
        input.read_file('no_file')


def test_read_file_pandas():
    results = input.read_file_pandas('data/input.txt')
    file = pd.read_csv('data/input.txt')
    data = ' '.join(file.iloc[:, 0].astype(str).tolist())
    assert results == data


def test_read_file_pandas_error():
    with pytest.raises(FileNotFoundError):
        input.read_file_pandas('no_file')
