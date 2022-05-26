class WashinMachine:

    def __init__(self):
        pass

    def wash(self, temperature = "Caliente"):
        self.temperature = temperature
        self._fill_tank(temperature)
        self._add_soap()
        self._wash()
        self._centrifuge()

    def _fill_tank(self, temperature):
        print(f'Llenando el tanque de agua a {temperature} grados')

    def _add_soap(self):
        print(f'Añadiendo jabón')

    def _wash(self):
        print(f'Lavando la ropa')
    
    def _centrifuge(self):
        print(f'Centrifugando la ropa')


if __name__ == "__main__":
    wash_machine = WashinMachine()
    wash_machine.wash(temperature = 35)
