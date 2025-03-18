# app/library/models.py

class Number:
    """
    Classe para operações matemáticas básicas envolvendo dois inteiros.
    """
    
    @staticmethod
    def sum(a: int, b: int) -> int:
        """
        Retorna a soma de dois inteiros.
        """
        return a + b

    @staticmethod
    def divide(a: int, b: int) -> float:
        """
        Retorna a divisão de dois inteiros.
        Levanta ValueError se b == 0.
        """
        if b == 0:
            raise ValueError("Divisão por zero não permitida.")
        return a / b


class Numbers:
    """
    Classe para operações em listas de inteiros.
    """

    @staticmethod
    def sum(numbers: list[int]) -> int:
        """
        Retorna a soma de todos os elementos de uma lista de inteiros.
        """
        return sum(numbers)

    @staticmethod
    def average(numbers: list[int]) -> float:
        """
        Retorna a média aritmética de uma lista de inteiros.
        Levanta ValueError se a lista estiver vazia.
        """
        if not numbers:
            raise ValueError("Lista vazia não permitida.")
        return sum(numbers) / len(numbers)
