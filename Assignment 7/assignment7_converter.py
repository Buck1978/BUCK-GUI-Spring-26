"""
Student: Richard Buckholz
Course: CPSC 3118 Graph User Interface Dev. 
Assignment: 7 – Measurement Converter GUI (Python/Qt)
Date: 2026-03-24
"""

import sys
import os

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit,
    QRadioButton, QGroupBox, QPushButton, QVBoxLayout, QHBoxLayout,
    QMessageBox, QFrame
)
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtCore import Qt


class ConverterWindow(QMainWindow):
    """Main GUI window for the measurement converter."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Converter App")
        self._init_ui()
        self._connect_signals()

    # ---------------------------------------------------------
    # UI SETUP
    # ---------------------------------------------------------
    def _init_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        # Fonts
        title_font = QFont("Segoe UI", 18, QFont.Bold)
        normal_font = QFont("Segoe UI", 12)

        # Title
        self.lblTitle = QLabel("Converter App")
        self.lblTitle.setFont(title_font)
        self.lblTitle.setAlignment(Qt.AlignCenter)

        # Instruction
        self.lblInstruction = QLabel("Enter a value and choose conversion")
        self.lblInstruction.setFont(normal_font)

        # Input
        self.txtInput = QLineEdit()
        self.txtInput.setFont(normal_font)
        self.txtInput.setPlaceholderText("Enter a number...")

        # Radio buttons
        self.rbInToM = QRadioButton("Inches to Meters")
        self.rbMToIn = QRadioButton("Meters to Inches")
        self.rbInToM.setFont(normal_font)
        self.rbMToIn.setFont(normal_font)
        self.rbInToM.setChecked(True)

        self.grpConversion = QGroupBox("Convert Measurement")
        grp_layout = QVBoxLayout()
        grp_layout.addWidget(self.rbInToM)
        grp_layout.addWidget(self.rbMToIn)
        self.grpConversion.setLayout(grp_layout)
        self.grpConversion.setFont(normal_font)

        # Result label
        self.lblResult = QLabel("Result will appear here.")
        self.lblResult.setFont(normal_font)
        self.lblResult.setAlignment(Qt.AlignCenter)
        self.lblResult.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.lblResult.setMinimumHeight(45)

        # Buttons
        self.btnConvert = QPushButton("Convert")
        self.btnClear = QPushButton("Clear")
        self.btnExit = QPushButton("Exit")

        for btn in (self.btnConvert, self.btnClear, self.btnExit):
            btn.setFont(normal_font)

        # Image
        self.lblImage = QLabel()
        self.lblImage.setAlignment(Qt.AlignCenter)

        #Build an absolute path to the image

        img_path = os.path.join(os.path.dirname(__file__), "house.png")

        img_path = os.path.join(os.path.dirname(__file__), "house.png")
        print("LOOKING FOR:", img_path)
        
        pix = QPixmap(img_path)
        if not pix.isNull():
            self.lblImage.setPixmap(pix.scaled(260, 260, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            self.lblImage.setText("house.png not found")

        image_frame = QFrame()
        image_frame.setFrameStyle(QFrame.StyledPanel | QFrame.Raised)
        img_layout = QVBoxLayout()
        img_layout.addWidget(self.lblImage)
        image_frame.setLayout(img_layout)

        # ---------------------------------------------------------
        # LAYOUT 
        # ---------------------------------------------------------
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(25)

        # LEFT COLUMN (IMAGE)
        main_layout.addWidget(image_frame, stretch=1)

        # RIGHT COLUMN (CONTROLS)
        right_col = QVBoxLayout()
        right_col.setSpacing(15)

        right_col.addWidget(self.lblTitle)
        right_col.addWidget(self.lblInstruction)
        right_col.addWidget(self.txtInput)
        right_col.addWidget(self.grpConversion)
        right_col.addWidget(self.lblResult)

        # Buttons row
        btn_row = QHBoxLayout()
        btn_row.addWidget(self.btnConvert)
        btn_row.addWidget(self.btnClear)
        btn_row.addWidget(self.btnExit)
        right_col.addLayout(btn_row)

        main_layout.addLayout(right_col, stretch=2)

        central.setLayout(main_layout)

        # Initial focus
        self.txtInput.setFocus()

        self.setStyleSheet("""QPushButton {background-color: #ADD8E6; /* Light Blue */ color: #000000; padding: 6px 14px; border-radius: 4px; border: 1px solid #7FB3D5;}
                           QPushButton:hover {background-color: #9CC9DD;/* Slightly darker on hover */}
                           QPushButton#btnExit {background-color: #ADD8E6; color: #000000;}
                           QPushButton#btnExit:hover {background-color: #9CC9DD;}""")

    # ---------------------------------------------------------
    # SIGNALS
    # ---------------------------------------------------------
    def _connect_signals(self):
        self.btnConvert.clicked.connect(self.handle_convert)
        self.btnClear.clicked.connect(self.handle_clear)
        self.btnExit.clicked.connect(QApplication.quit)

    # ---------------------------------------------------------
    # CONVERSION LOGIC
    # ---------------------------------------------------------
    @staticmethod
    def inches_to_meters(inches: float) -> float:
        return inches * 0.0254

    @staticmethod
    def meters_to_inches(meters: float) -> float:
        return meters / 0.0254

    # ---------------------------------------------------------
    # EVENT HANDLERS
    # ---------------------------------------------------------
    def handle_convert(self):
        text = self.txtInput.text().strip()

        # Validate
        if not text:
            return self._error("Value entered is not numeric.")

        try:
            value = float(text)
        except ValueError:
            return self._error("Value entered is not numeric.")

        if value <= 0:
            return self._error("Converted value is negative.")

        # Conversion
        if self.rbInToM.isChecked():
            meters = self.inches_to_meters(value)
            result = f"{value:.3f} inches = {meters:.3f} meters"
        else:
            inches = self.meters_to_inches(value)
            result = f"{value:.3f} meters = {inches:.3f} inches"

        self.lblResult.setText(result)

    def handle_clear(self):
        self.txtInput.clear()
        self.lblResult.setText("Result will appear here.")
        self.rbInToM.setChecked(True)
        self.txtInput.setFocus()

    def _error(self, msg):
        QMessageBox.critical(self, "Input Error", msg)

# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------
def main():
    app = QApplication(sys.argv)
    window = ConverterWindow()
    window.resize(800, 400)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
