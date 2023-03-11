import sqlite3

from inspect import get_annotations
from bookkeeper.repository.abstract_repository import AbstractRepository, T
from typing import Any


class SQLiteRepository(AbstractRepository[T]):
    """
    Репозиторий, работающий с базой данных SQLite"
    """
    def __init__(self, db_file: str, cls: type) -> None:
        self.db_file = db_file
        self.table_name = cls.__name__.lower()
        self.fields = get_annotations(cls, eval_str=True)
        self.fields.pop('pk')

    def add(self, obj: T) -> int:
        names = ', '.join(self.fields.keys())
        p = ', '.join("?" * len(self.fields))
        values = [getattr(obj, x) for x in self.fields]
        """
        if getattr(obj, 'pk', None) != 0:
        raise ValueError(f'trying to add object {obj} with filled `pk` attribute')
        """
        with sqlite3.connect(self.db_file) as con:
            cur = con.cursor()
            cur.execute('PRAGMA foreign_keys = ON')
            cur.execute(
                f'INSERT INTO {self.table_name} ({names}) VALUES ({p})',
                values
            )
            obj.pk = cur.lastrowid
        con.close()
        return obj.pk

    def get(self, pk: int) -> T | None:
        """ Получить объект по id """
        with sqlite3.connect(self.db_file) as con:
            cur = con.cursor()
            cur.execute(f'SELECT * FROM {self.table_name} where pk = {pk}')
            con.close()
        return None

    def get_all(self, where: dict[str, Any] | None = None) -> list[T]:
        """
        Получить все записи по некоторому условию
        where - условие в виде словаря {'название_поля': значение}
        если условие не задано (по умолчанию), вернуть все записи
        """
        with sqlite3.connect(self.db_file) as con:
            cur = con.cursor()
            """
            if where is None:
                #return list[self._container.values()]
            """
            cur.execute(f'SELECT * FROM {self.table_name} where ({names}: {p}) VALUES ({p})')   \
                # добавить если условия не заданы
            res = cur.fetchall()
        con.close()
        return res

    def update(self, obj: T) -> None:
        """ Обновить данные об объекте. Объект должен содержать поле pk. """
        """
        if obj.pk == 0:
            raise ValueError('attempt to update object with unknown primary key')
        self._container[obj.pk] = obj
        """
        with sqlite3.connect(self.db_file) as con:
            cur = con.cursor()
            cur.execute(f'SELECT * FROM {self.table_name} where pk = {obj.pk}')
            con.close()
        return None

    def delete(self, pk: int) -> None:
        """ Удалить запись """
        with sqlite3.connect(self.db_file) as con:
            cur = con.cursor()
            cur.execute(f'DELETE * FROM {self.table_name} where pk = {pk}')
            con.close()
        return None
