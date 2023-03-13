"""
Таблица расходов из лекции
"""

import sys
from PySide6 import QtWidgets

app = QtWidgets.QApplication(sys.argv)

expenses_table = QtWidgets.QTableWidget(4, 20)
expenses_table.setColumnCount(4)
expenses_table.setRowCount(20)
expenses_table.setHorizontalHeaderLabels(
"Дата Сумма Категория Комментарий".split())
header = expenses_table.horizontalHeader()
header.setSectionResizeMode(
0, QtWidgets.QHeaderView.ResizeToContents)
header.setSectionResizeMode(
1, QtWidgets.QHeaderView.ResizeToContents)
header.setSectionResizeMode(
2, QtWidgets.QHeaderView.ResizeToContents)
header.setSectionResizeMode(
3, QtWidgets.QHeaderView.Stretch)

expenses_table.setEditTriggers(
QtWidgets.QAbstractItemView.NoEditTriggers)
expenses_table.verticalHeader().hide()


def set_data(data: list[list[str]]):
    for i, row in enumerate(data):
        for j, x in enumerate(row):
            expenses_table.setItem(
                i, j,
                QtWidgets.QTableWidgetItem(x.capitalize())
            )


expenses_table.show()
sys.exit(app.exec())


