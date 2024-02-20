import threading

from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QLineEdit, QMessageBox
import sys
from backend import Chatbot

class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Chatbot')
        self.setMinimumSize(700, 500)
        self.chatbot = Chatbot()

        #Add Chabot area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        #Add the input field widget
        self.input_area = QLineEdit(self)
        self.input_area.setGeometry(10, 340, 480, 40)
        self.input_area.returnPressed.connect(self.send_prompt)

        #Add the button
        self.send_button = QPushButton('Send', self)
        self.send_button.setGeometry(500, 340, 100, 40)
        self.send_button.clicked.connect(self.send_prompt)

    def send_prompt(self):
        user_input = self.input_area.text().strip()
        if user_input:
            self.chat_area.append(f"<p style='color:#333333'>Me: {user_input}</p>")
            self.input_area.clear()

            thread = threading.Thread(target=self.get_bot_response, args=(user_input,))
            thread.start()

        else:
            message_box = QMessageBox()
            message_box.setWindowTitle('ERROR')
            message_box.setText('Please fill in a text first')
            message_box.exec()

    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(self.input_area.text()).strip()
        self.chat_area.append(f"<p style='color:#333333; background-color:#E9E9E9'>AI: {response}</p>")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = ChatbotWindow()
    main_window.show()
    sys.exit(app.exec())