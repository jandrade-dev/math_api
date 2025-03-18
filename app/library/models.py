# app/library/models.py

class Number:
    
    @staticmethod
    def sum(a: int, b: int) -> int:
        return a + b

    @staticmethod
    def divide(a: int, b: int) -> float:
        if b == 0:
            raise ValueError("Divisão por zero não permitida.")
        return a / b


class Numbers:

    @staticmethod
    def sum(numbers: list[int]) -> int:
        return sum(numbers)

    @staticmethod
    def average(numbers: list[int]) -> float:
        if not numbers:
            raise ValueError("Lista vazia não permitida.")
        return sum(numbers) / len(numbers)
