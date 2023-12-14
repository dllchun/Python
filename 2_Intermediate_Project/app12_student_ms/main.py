from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon
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
    QMenu, QTableWidget, QTableWidgetItem, QDialog, QToolBar, QStatusBar, QMessageBox,
)
import sys
import sqlite3

class Database():
    def __init__(self, database_file= 'database.db'):
        self.database_file = database_file

    def connect(self):
        with sqlite3.connect(self.database_file) as conn:
            return conn

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Management System')
        self.setMinimumSize(800, 600)

        menu = self.menuBar()

        #File Menu Item
        file_menu = menu.addMenu('&File')
        add_student_action = QAction(QIcon('icons/add.png'),'Add Student', self)
        add_student_action.triggered.connect(self.insert)
        file_menu.addAction(add_student_action)

        #About Menu Item
        about_menu = menu.addMenu('&Help')
        about_action = QAction('About', self)
        about_menu.addAction(about_action)
        about_action.setMenuRole(QAction.MenuRole.NoRole)
        about_action.triggered.connect(self.about)

        #Edit_Meu_Item
        edit_menu = menu.addMenu('&Edit')
        search_action = QAction(QIcon("icons/search.png"), 'Search', self)
        search_action.triggered.connect(self.search)
        edit_menu.addAction(search_action)

        #Table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

        #Toolbar
        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        toolbar.addActions([add_student_action, search_action])

        #Status Bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        #Detect a cell clicked
        self.table.cellClicked.connect(self.cell_clicked)

    def cell_clicked(self):
        edit_button = QPushButton('Edit Record')
        edit_button.clicked.connect(self.edit)

        delete_button = QPushButton('delete Record')
        delete_button.clicked.connect(self.delete)

        children = self.findChildren(QPushButton)
        if children:
            for child in children:
                self.status_bar.removeWidget(child)

        self.status_bar.addWidget(edit_button)
        self.status_bar.addWidget(delete_button)

    def about(self):
        dialog = AboutDialog()
        dialog.exec()

    def load_data(self):
        conn = Database().connect()
        cursor = conn.cursor()
        result = cursor.execute("SELECT * FROM students").fetchall()
        self.table.setRowCount(0)
        for row_num, row_data in enumerate(result):
            self.table.insertRow(row_num)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_num, column_number, QTableWidgetItem(str(data)))

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()

    def search(self):
        dialog = SearchDialog()
        dialog.exec()

    def edit(self):
        dialog = EditDialog()
        dialog.exec()

    def delete(self):
        dialog = DeleteDialog()
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

        conn = Database().connect()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Students (name, course, mobile) VALUES (?,?,?)',
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


class EditDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Update Student Data')
        self.setFixedSize(300, 300)

        layout = QVBoxLayout()
        selected_table_index = main_window.table.currentRow()

        #Get id from the selected one
        self.student_id = main_window.table.item(selected_table_index, 0).text()

        #Student Field
        student_name = main_window.table.item(selected_table_index, 1).text()
        self.student = QLineEdit(student_name)
        self.student.setPlaceholderText('Student')
        layout.addWidget(self.student)

        #Course Field
        course = main_window.table.item(selected_table_index, 2).text()
        self.courses = QComboBox(self)
        course_list = ['Math', 'Astronomy', 'Biology', 'Physics']
        self.courses.addItems(course_list)
        self.courses.setCurrentText(course)
        layout.addWidget(self.courses)

        #mobile Field
        mobile = main_window.table.item(selected_table_index, 3).text()
        self.mobile = QLineEdit(mobile)
        self.mobile.setPlaceholderText('mobile')
        layout.addWidget(self.mobile)

        #Submit Button
        button = QPushButton('Update')
        button.clicked.connect(self.update_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def update_student(self):
            conn = Database().connect()
            cursor = conn.cursor()
            cursor.execute("UPDATE students SET name = ?, course = ? , mobile = ? WHERE id = ?",
                           (self.student.text(),
                                        self.courses.itemText(self.courses.currentIndex()),
                                        self.mobile.text(),
                                        self.student_id))
            conn.commit()
            main_window.load_data()
            self.close()


class DeleteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Delete Student Data')


        layout = QGridLayout()
        confirmation = QLabel('Are you sure you want to delete the record')
        layout.addWidget(confirmation, 0, 0 , 1, 2)

        yes_button = QPushButton('Yes')
        yes_button.clicked.connect(self.delete_record)
        layout.addWidget(yes_button, 1, 0 )

        no_button = QPushButton('No')
        no_button.clicked.connect(self.close_dialog)
        layout.addWidget(no_button, 1, 1)


        self.setLayout(layout)

    def delete_record(self):
        selected_table_index = main_window.table.currentRow()
        student_id = main_window.table.item(selected_table_index, 0).text()

        #Execute Query
        conn = Database().connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
        main_window.load_data()
        self.close()

        confirmation_widget = QMessageBox()
        confirmation_widget.setWindowTitle('Delete Record')
        confirmation_widget.setText('The record has been deleted')
        confirmation_widget.exec()

    def close_dialog(self):
        self.close()
        main_window.load_data()

class AboutDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        content = '''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et 
        dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex 
        ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
        nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim 
        id est laborum.
        '''
        self.setText(content)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.load_data()
    sys.exit(app.exec())