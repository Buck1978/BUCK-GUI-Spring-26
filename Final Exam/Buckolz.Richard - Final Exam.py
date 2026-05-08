# Name: Richard Buckholz
# Course: CPSC 3118 Graph User Interface Dev.
# Final Project: Student Grade Calculator (MVC with PySide6)

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QGridLayout, QMessageBox, QMainWindow
)
from PySide6.QtCore import Qt


# ============================================================
# MODEL
# ============================================================
class GradeModel:
    """Handles grade calculations and validation."""

    def validate_and_convert(self, g1, g2, g3):
        """Validate inputs and return list of floats."""
        raw = [g1.strip(), g2.strip(), g3.strip()]

        if any(v == "" for v in raw):
            raise ValueError("All three grades must be entered.")

        grades = []
        for i, value in enumerate(raw, start=1):
            try:
                num = float(value)
            except ValueError:
                raise ValueError(f"Grade {i} must be a valid number.")

            if not (0 <= num <= 100):
                raise ValueError(f"Grade {i} must be between 0 and 100.")

            grades.append(num)

        return grades

    def calculate_average(self, grades):
        avg = sum(grades) / len(grades)
        return round(avg, 2)

    def letter_grade(self, avg):
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        return "F"


# ============================================================
# VIEW
# ============================================================
class GradeView(QWidget):
    """Defines the GUI layout and widgets."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Grade Calculator")

        # Labels
        self.lbl_g1 = QLabel("Grade 1:")
        self.lbl_g2 = QLabel("Grade 2:")
        self.lbl_g3 = QLabel("Grade 3:")
        self.lbl_avg_title = QLabel("Average:")
        self.lbl_letter_title = QLabel("Letter Grade:")

        # Inputs
        self.input_g1 = QLineEdit()
        self.input_g2 = QLineEdit()
        self.input_g3 = QLineEdit()

        self.input_g1.setPlaceholderText("")
        self.input_g2.setPlaceholderText("")
        self.input_g3.setPlaceholderText("")

        # Output labels
        self.lbl_avg_value = QLabel("-")
        self.lbl_letter_value = QLabel("-")

        # Buttons
        self.btn_calculate = QPushButton("Calculate")
        self.btn_clear = QPushButton("Clear")
        self.btn_exit = QPushButton("Exit")

        # Layout
        layout = QGridLayout()
        layout.addWidget(self.lbl_g1, 0, 0)
        layout.addWidget(self.input_g1, 0, 1)

        layout.addWidget(self.lbl_g2, 1, 0)
        layout.addWidget(self.input_g2, 1, 1)

        layout.addWidget(self.lbl_g3, 2, 0)
        layout.addWidget(self.input_g3, 2, 1)

        layout.addWidget(self.lbl_avg_title, 3, 0)
        layout.addWidget(self.lbl_avg_value, 3, 1)

        layout.addWidget(self.lbl_letter_title, 4, 0)
        layout.addWidget(self.lbl_letter_value, 4, 1)

        layout.addWidget(self.btn_calculate, 5, 0)
        layout.addWidget(self.btn_clear, 5, 1)
        layout.addWidget(self.btn_exit, 6, 0, 1, 2)

        self.setLayout(layout)


# ============================================================
# CONTROLLER
# ============================================================
class GradeController(QMainWindow):
    """Connects the View and Model, handles events."""

    def __init__(self):
        super().__init__()

        self.model = GradeModel()
        self.view = GradeView()

        self.setCentralWidget(self.view)

        # Connect signals
        self.view.btn_calculate.clicked.connect(self.calculate)
        self.view.btn_clear.clicked.connect(self.clear)
        self.view.btn_exit.clicked.connect(self.exit_app)

    # -------------------------
    # Event Handlers
    # -------------------------
    def calculate(self):
        try:
            grades = self.model.validate_and_convert(
                self.view.input_g1.text(),
                self.view.input_g2.text(),
                self.view.input_g3.text()
            )
        except ValueError as e:
            self.show_error(str(e))
            return

        avg = self.model.calculate_average(grades)
        letter = self.model.letter_grade(avg)

        self.view.lbl_avg_value.setText(f"{avg:.2f}")
        self.view.lbl_letter_value.setText(letter)

    def clear(self):
        self.view.input_g1.clear()
        self.view.input_g2.clear()
        self.view.input_g3.clear()
        self.view.lbl_avg_value.setText("-")
        self.view.lbl_letter_value.setText("-")

    def exit_app(self):
        QApplication.instance().quit()

    # -------------------------
    # Helper
    # -------------------------
    def show_error(self, message):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Input Error")
        msg.setText(message)
        msg.exec()


# ============================================================
# MAIN
# ============================================================
def main():
    app = QApplication(sys.argv)
    window = GradeController()
    window.resize(350, 250)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()