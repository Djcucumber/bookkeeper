from PySide6.QtWidgets import QApplication
from bookkeeper.view.expense_view import MainWindow
from bookkeeper.presenter.expense_presenter import ExpensePresenter
from bookkeeper.models.category import Category
from bookkeeper.models.expense import Expense
from bookkeeper.repository.sqlite_repository import SQLiteRepository
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    view = MainWindow()
    model = None

    cat_repo = SQLiteRepository[Category]("database.db", Category)
    exp_repo = SQLiteRepository[Expense]("database.db", Expense)

    window = ExpensePresenter(model, view, cat_repo, exp_repo)
    window.show()
    app.exec_()
