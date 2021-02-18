import sys
import sqlite3
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt
from UI.mainUI import Ui_MainWindow
from UI.addEditCoffeeFormUI import Ui_addEditForm
from PyQt5 import uic


DATABASE_PATH = 'data/coffee.sqlite3'
GROUND_OR_GRAINS = {0: 'молотый',
                    1: 'в зёрнах'}
GROUND_OR_GRAINS_NUMBER = 3
TABLE_CREATE_REQUEST = '''CREATE TABLE coffee (
    id                  INTEGER        PRIMARY KEY AUTOINCREMENT
                                       UNIQUE
                                       NOT NULL,
    sort_title          TEXT           NOT NULL,
    degree_of_roasting  TEXT           NOT NULL,
    ground_or_grains    INTEGER (0, 1) NOT NULL,
    flavor_description  TEXT,
    price               REAL,
    volume_of_packaging REAL
);'''


def create_empty_file(full_path: str):
    full_path = full_path.replace('\\', '/')
    path = '/'.join(full_path.split('/')[:-1])
    if not os.path.isdir(path):
        os.makedirs(path)
    open(full_path, mode='w').close()


def create_database_if_need():
    if not os.path.isfile(DATABASE_PATH):
        create_empty_file(DATABASE_PATH)
        con = sqlite3.connect(DATABASE_PATH)
        cur = con.cursor()
        cur.execute(TABLE_CREATE_REQUEST)
        con.commit()
        con.close()


class CoffeeAddForm(QWidget, Ui_addEditForm):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window
        self.submit_btn.clicked.connect(self.submit)
        self.id_box.valueChanged.connect(self.changer)

    def changer(self, coffee_id):
        create_database_if_need()
        con = sqlite3.connect(DATABASE_PATH)
        cur = con.cursor()
        e = cur.execute('SELECT * FROM coffee WHERE id = ?',
                              (coffee_id, )).fetchone()
        if e is not None:
            e = e[1:]
            self.sort_edit.setText(e[0])
            self.degree_edit.setText(e[1])
            self.ground_or_grains_box.setValue(e[2])
            self.flavor_edit.setText(e[3])
            self.price_box.setValue(e[4])
            self.volume_box.setValue(e[5])
        con.close()

    def submit(self):
        id = self.id_box.value()
        sort = self.sort_edit.text()
        degree = self.degree_edit.text()
        grain = self.ground_or_grains_box.value()
        flavor = self.flavor_edit.text()
        price = self.price_box.value()
        volume = self.volume_box.value()
        create_database_if_need()
        con = sqlite3.connect(DATABASE_PATH)
        cur = con.cursor()
        if (cur.execute('SELECT id FROM coffee WHERE id = ?',
                        (id, )).fetchone() is not None):
            cur.execute('DELETE FROM coffee WHERE id = ?', (id, ))
        if id != 0:
            cur.execute('INSERT INTO coffee VALUES (?, ?, ?, ?, ?, ?, ?)',
                        (id, sort, degree, grain,
                         flavor, price, volume))
        else:
            cur.execute('INSERT INTO coffee(sort_title,'
                        ' degree_of_roasting,'
                        ' ground_or_grains,'
                        ' flavor_description,'
                        ' price,'
                        ' volume_of_packaging) VALUES (?, ?, ?, ?, ?, ?)',
                        (sort, degree, grain,
                         flavor, price, volume))
        con.commit()
        con.close()
        self.main_window.load_table()
        self.deleteLater()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.coffee_table: QTableWidget = self.coffee_table
        self.add_form = None
        self.coffee_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        self.add_edit_btn.clicked.connect(self.add_item)
        self.load_table()

    def load_table(self):
        self.coffee_table.setRowCount(0)
        create_database_if_need()
        con = sqlite3.connect(DATABASE_PATH)
        cur = con.cursor()
        data = cur.execute('SELECT * FROM coffee').fetchall()
        self.coffee_table.setRowCount(len(data))
        for i, row in enumerate(data):
            for j in range(len(row)):
                if j == GROUND_OR_GRAINS_NUMBER:
                    value = GROUND_OR_GRAINS[row[j]]
                else:
                    value = str(row[j])
                item = QTableWidgetItem(value)
                item.setFlags(Qt.ItemIsEnabled)
                self.coffee_table.setItem(i, j, item)
        con.close()

    def add_item(self):
        self.add_form = CoffeeAddForm(self)
        self.add_form.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
