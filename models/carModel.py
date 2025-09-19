from models.model import Model


class CarModel(Model):
    def __init__(self, model, year, color, license_plates, day_price=None, insurance_price=None):
        self.model = model
        self.year = year
        self.color = color
        self.license_plates = license_plates
        self.insurance_price = insurance_price
        self.day_price = day_price

    table = "cars"
    required_columns = {'model', 'year', 'color', 'license_plates'}
