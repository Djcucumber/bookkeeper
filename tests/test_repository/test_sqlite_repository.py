from bookkeeper.repository.sqlite_repository import SQLiteRepository

import pytest

@pytest.fixture
def custom_class():
    class Custom():
        pk = 0

    return Custom


@pytest.fixture
def repo():
    return SQLiteRepository()
"""
Тесты на проверку pk
"""

def test_cannot_add_with_pk(db_file, cls):
    """
    Тесты на проверку pk
    """
    obj = custom_class()
    obj.pk = 1
    with pytest.raises(ValueError):
        repo.add(obj)

def test_cannot_add_without_pk(db_file, cls):
    with pytest.raises(ValueError):
        repo.add(0)

def test_cannot_delete_unexistent(db_file, cls):
    with pytest.raises(KeyError):
        repo.delete(1)

def test_cannot_delete_unexistent(db_file, cls):
    with pytest.raises(KeyError):
        repo.delete(1)


def test_cannot_update_without_pk(db_file, cls):
    obj = custom_class()
    with pytest.raises(ValueError):
        repo.update(obj)


def test_get_all(db_file, cls):
    objects = [custom_class() for i in range(5)]
    for o in objects:
        repo.add(o)
    assert repo.get_all() == objects


def test_get_all_with_condition(db_file, cls):
    objects = []
    for i in range(5):
        o = custom_class()
        o.name = str(i)
        o.test = 'test'
        repo.add(o)
        objects.append(o)
    assert repo.get_all({'name': '0'}) == [objects[0]]
    assert repo.get_all({'test': 'test'}) == objects
