class Car:

    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.colo = color
        self._state = "En reposo"
        self._motor = Motor(cilinders = 4)

    def speed_up(self, type = "Despacio"):
        if type ==  "rapida":
            self._motor.fuel_injection(10)
        else:
            self._motor.fuel_injection(3)

        self._state = "En movimiento"

class Motor:

    def __init__(self, cilinders, type = "petrol"):
        self.cilinders = cilinders
        self.type = type
        self._temperature = 0

    def fuel_injection(self, quantity):
        self.quantity = quantity