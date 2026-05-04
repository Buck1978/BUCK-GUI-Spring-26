from PySide6.QtWidgets import QMainWindow
from view import Ui_MainWindow
from model import TemperatureModel

class Controller(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Create Model
        self.model = TemperatureModel()

        # Connect signals
        self.ui.btn_convert.clicked.connect(self.convert_temperature)

    def convert_temperature(self):
        text = self.ui.input_celsius.text()

        try:
            value = float(text)
            self.model.set_celsius(value)
            result = self.model.get_fahrenheit()
            self.ui.label_result.setText(f"{result:.2f} °F")
        except ValueError:
            self.ui.label_result.setText("Invalid input")