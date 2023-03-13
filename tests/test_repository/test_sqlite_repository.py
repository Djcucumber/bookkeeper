from bookkeeper.repository.sqlite_repository import SQLiteRepository

import pytest


@pytest.fixture
def custom_class():
    class Custom:
        pk: int = 0

    return Custom


@pytest.fixture
def repo(custom_class):
    return SQLiteRepository("database.db", custom_class)  # не видит файл базы данных:с


def test_crud(repo, custom_class):
    obj = custom_class()
    pk = repo.add(obj)
    o = repo.get(5555)
    assert obj.pk == pk
    assert repo.get(pk) == obj
    assert o is None
    repo.delete(pk)
    assert repo.get(pk) is None
