# app/tests/test_models.py

import pytest
from app.library.models import Number, Numbers

def test_sum_numbers():
    assert Number.sum(2, 3) == 5

def test_divide_numbers():
    assert Number.divide(10, 2) == 5.0

def test_divide_by_zero():
    with pytest.raises(ValueError):
        Number.divide(10, 0)

def test_sum_list():
    assert Numbers.sum([1, 2, 3]) == 6

def test_average_list():
    assert Numbers.average([2, 4, 6]) == 4.0

def test_average_empty_list():
    with pytest.raises(ValueError):
        Numbers.average([])
