# app/services/services.py

from app.library.models import Numbers

def sum_numbers(numbers: list[int]) -> int:
    """
    Soma uma lista de inteiros.
    """
    return Numbers.sum(numbers)

def average_numbers(numbers: list[int]) -> float:
    """
    Calcula a média de uma lista de inteiros.
    """
    return Numbers.average(numbers)
