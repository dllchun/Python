from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QVBoxLayout,
    QLabel,
    QWidget,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QApplication,
    QComboBox,
    QMainWindow,
    QMenu, QTableWidget, QTableWidgetItem, QDialog
)
import sys
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Management System')
        self.setFixedSize(500,500)

        menu = self.menuBar()

        #File Menu Item
        file_menu = menu.addMenu('&File')
        add_student_action = QAction('Add Student', self)
        add_student_action.triggered.connect(self.insert)
        file_menu.addAction(add_student_action)

        #About Menu Item
        about_menu = menu.addMenu('&Help')
        about_action = QAction('About', self)
        about_menu.addAction(about_action)
        about_action.setMenuRole(QAction.MenuRole.NoRole)

        #Edit_Meu_Item
        edit_menu = menu.addMenu('&Edit')
        search_action = QAction('Search', self)
        search_action.triggered.connect(self.search)
        edit_menu.addAction(search_action)

        #Table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

    def load_data(self):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.execute("SELECT * FROM students").fetchall()
            self.table.setRowCount(0)
            for row_num, row_data in enumerate(cursor):
                self.table.insertRow(row_num)
                for column_number, data in enumerate(row_data):
                    self.table.setItem(row_num, column_number, QTableWidgetItem(str(data)))

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()

    def search(self):
        dialog = SearchDialog()
        dialog.exec()

class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Insert Student Data')
        self.setFixedSize(300, 300)

        layout = QVBoxLayout()
        #Student Field
        self.student = QLineEdit()
        self.student.setPlaceholderText('Student')
        layout.addWidget(self.student)

        #Course Field
        self.courses = QComboBox(self)
        course_list = ['Math', 'Astronomy', 'Biology', 'Physics']
        self.courses.addItems(course_list)
        layout.addWidget(self.courses)

        #mobile Field
        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText('mobile')
        layout.addWidget(self.mobile)

        #Submit Button
        button = QPushButton('Submit')
        button.clicked.connect(self.add_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def add_student(self):
        name = self.student.text()
        course = self.courses.itemText(self.courses.currentIndex())
        mobile = self.mobile.text()
        with sqlite3.connect('database.db') as conn:
            cursor = conn.execute('INSERT INTO Students (name, course, mobile) VALUES (?,?,?)',
                                  (name,course, mobile))
            conn.commit()
            main_window.load_data()
            self.close()


class SearchDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Search Student')
        self.setFixedSize(300, 300)

        layout = QVBoxLayout()

        #Name Field
        self.name = QLineEdit()
        self.name.setPlaceholderText('Name')
        layout.addWidget(self.name)

        #Button
        search_button = QPushButton('Search')
        search_button.clicked.connect(self.search)
        layout.addWidget(search_button)

        self.setLayout(layout)

    def search(self):
        name = self.name.text()
        items = main_window.table.findItems(name, Qt.MatchFlag.MatchExactly)
        for item in items:
            main_window.table.item(item.row(), 1).setSelected(True)
        self.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.load_data()
    sys.exit(app.exec())