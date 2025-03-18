# app/tests/test_services.py

from app.services.services import sum_numbers, average_numbers

def test_service_sum():
    assert sum_numbers([1, 2, 3]) == 6

def test_service_average():
    assert average_numbers([2, 4, 6]) == 4.0
