class DNI:
    def __init__(self, identity_numer=""):
        self.dni = identity_numer
        self.healthy_number = False
        self.healthy_letter = False
        self.table = Table()

    def set_dni(self, identity_number):
        self.dni = identity_number

    def get_dni(self):
        return self.dni
