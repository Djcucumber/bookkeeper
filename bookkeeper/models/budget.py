"""
Модель бюджета
"""
from dataclasses import dataclass
"""
В модели "Бюджет" существуют следующие поля: срок, категория расходов, сумма.
Сроки: день, неделя, месяц
Категория расходов
Сумма - ограничение на категорию/категории расходов
"""


@dataclass
class Budget:
    """
    Бюджет
    term - срок
    amount - сумма
    category - категория
    pk - id записи в базе данных
    """
    term: str
    amount: int
    category: int
    pk: int = 0
