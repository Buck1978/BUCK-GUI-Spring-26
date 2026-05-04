class TemperatureModel:
    def __init__(self):
        self.celsius = 0.0
        self.fahrenheit = 32.0

    def set_celsius(self, value: float):
        """Store Celsius value and compute Fahrenheit."""
        self.celsius = value
        self.fahrenheit = (value * 9/5) + 32

    def get_fahrenheit(self) -> float:
        """Return the computed Fahrenheit value."""
        return self.fahrenheit