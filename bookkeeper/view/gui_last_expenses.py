"""
Демонстрация TableView на основе https://www.pythonguis.com/\
tutorials/qtableview-modelviews-numpy-pandas/
Пример из семинара
"""
"""
from bookkeeper.models.category import Category
from bookkeeper.repository.sqlite_repository import SQLiteRepository

import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

cat_repo = SQLiteRepository[Category]('database.db', Category)  \
    # Почему-то не видит готовый файл базы данных, и при запуске программы создаёт новый \
# хорошо бы с этим разобраться


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QtWidgets.QTableView()

        data = cat_repo.get_all()

        self.model = TableModel(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
"""
