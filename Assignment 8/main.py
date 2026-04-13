import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from asn8_ui import Ui_root

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_root()
        self.ui.setupUi(self)
        
        # Connect buttons
        self.ui.btnS.clicked.connect(self.submit)
        self.ui.btnR.clicked.connect(self.reset)
        self.ui.btnQ.clicked.connect(self.close)

        # Put cursor in First Name box
        self.ui.entFirst.setFocus()

        # Keyboard shortcuts
        self.ui.btnS.setDefault(True)   # Enter = Submit
        self.ui.btnQ.setShortcut("Esc") # Esc = Quit

    def submit(self):
        first = self.ui.entFirst.text().strip()
        last = self.ui.entLast.text().strip()
        email = self.ui.entEmail.text().strip()
        phone = self.ui.entPhone.text().strip()

        if not first or not last:
            QMessageBox.warning(self, "Error", "First and Last Name are required.")
            return

        full_name = f"{first} {last}"
        info = f"{full_name}\n{email}\n{phone}"

        print(info)
        QMessageBox.information(self, "Submitted", info)

    def reset(self):
        self.ui.entFirst.clear()
        self.ui.entLast.clear()
        self.ui.entEmail.clear()
        self.ui.entPhone.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())