from models.model import Model


class RentModel(Model):
    def __init__(self, car_id, client_id, days_qty, total_price, active=True):
        self.car_id = car_id
        self.client_id = client_id
        self.days_qty = days_qty
        self.total_price = total_price
        self.active = active

    table = "rents"
    required_columns = ["car_id", "client_id", "days_qty", "total_price"]
