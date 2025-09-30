from models.model import Model
from connection import cursor, connection


class RentModel(Model):
    def __init__(self, car_id, client_id, days_qty, total_price, active=True):
        self.car_id = car_id
        self.client_id = client_id
        self.days_qty = days_qty
        self.total_price = total_price
        self.active = active

    table = "rents"
    required_columns = ["car_id", "client_id", "days_qty", "total_price"]

    @classmethod
    def get_full_info(cls, id=None):

        sql = f'''SELECT re.id AS rent_number, cl.name||" #"||cl.id AS client_name, ca.model AS car_model,
                            ca.license_plates, re.start_date, re.days_qty, re.total_price, re.active AS active_status
                    FROM rents re 
                    JOIN cars ca ON re.car_id = ca.id
                    JOIN clients cl ON re.client_id = cl.id
                    WHERE ? IS NULL OR re.id = ?;'''
        cursor.execute(sql, (id,id))

        columns = [desc[0] for desc in cursor.description]
        vals = cursor.fetchall()
        return {'columns': columns, 'values': vals, 'qty': len(vals)}
