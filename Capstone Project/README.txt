# Temperature Converter – MVC PySide6 Application

## Description
This project is a simple desktop application that converts a temperature from Celsius to Fahrenheit.  
It demonstrates how to build a GUI application using Python, PySide6, Qt Designer, and the Model–View–Controller (MVC) architectural pattern.

The goal is to show a clean separation between:
- the Model (application logic),
- the View (Qt Designer UI),
- and the Controller (signal/slot connections and coordination).

---

## MVC Overview

### Model (model.py)
- Contains the temperature conversion logic.
- Stores Celsius and Fahrenheit values.
- Performs the calculation (C × 9/5) + 32.
- Does not import PySide6 or interact with the GUI.

### View (view.ui + view.py)
- Built visually in Qt Designer.
- Contains:
  - A QLineEdit for Celsius input  
  - A QPushButton to trigger conversion  
  - A QLabel to display the Fahrenheit result  
- Has no business logic; only UI elements.

### Controller (controller.py)
- Loads the UI from view.py.
- Creates and manages the Model.
- Connects button clicks to logic.
- Reads user input, updates the Model, and refreshes the View.

---

## How to Run the Application

### 1. You can open main.py and press ctrl +F5 or just run the application
    2. You can also open main.py and open a terminal, change directory to your application folder and then run by typing 	python main.py
