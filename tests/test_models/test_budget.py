"""
Тесты для бюджета
"""

import pytest

from bookkeeper.repository.memory_repository import MemoryRepository
from bookkeeper.models.budget import Budget


@pytest.fixture
def repo():
    return MemoryRepository()


def test_create_with_full_args_list():
    e = Budget(term="day", amount=100, category=1, pk=1)
    assert e.term == "day"
    assert e.amount == 100


def test_create_brief():
    e = Budget("day", 100, 1)
    assert e.term == "day"
    assert e.amount == 100


def test_can_add_to_repo(repo):
    e = Budget("day", 100, 1)
    pk = repo.add(e)
    assert e.pk == pk
