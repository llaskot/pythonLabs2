from models.model import Model


class ClientModel(Model):
    def __init__(self, name, license_num):
        self.name = name
        self.license_num = license_num

    table = "clients"
    required_columns = {'name', 'license_num'}
