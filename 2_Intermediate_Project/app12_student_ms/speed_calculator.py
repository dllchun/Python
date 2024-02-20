from PyQt6.QtWidgets import (
    QVBoxLayout,
    QLabel,
    QWidget,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QApplication,
    QComboBox,
)

import sys


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()

        distance_label = QLabel("Distance: ")
        self.distance_line_edit = QLineEdit("")
        self.selector = QComboBox()
        self.selector.addItems(["Imperial(miles)", "Metric(km)"])

        time_label = QLabel("Time(hours): ")
        self.time_line_edit = QLineEdit("")

        self.calculator_button = QPushButton("Calculate")
        self.calculator_button.clicked.connect(self.calculate_speed)

        self.output_label = QLabel("")

        # add widget to the grid

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.selector, 0, 2)

        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)

        grid.addWidget(self.calculator_button, 2, 1)
        grid.addWidget(self.output_label, 3, 0)

        self.setLayout(grid)

    def calculate_speed(self, ctext):
        distance = float(self.distance_line_edit.text())
        time = float(self.time_line_edit.text())

        average_speed = distance / time

        if self.selector.currentText() == "Metric(km)":
            average_speed = round(average_speed, 2)
            self.output_label.setText(f"Average speed: {average_speed} m/h")

        elif self.selector.currentText() == "Imperial(miles)":
            average_speed = round(average_speed * 0.621371, 2)
            self.output_label.setText(f"Average speed: {average_speed} km/h")

        else:
            self.output_label.setText("You have filled in wrong information")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    speed_calculator = SpeedCalculator()
    speed_calculator.show()
    sys.exit(app.exec())
