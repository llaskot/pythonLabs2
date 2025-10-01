from models.model import Model
from connection import cursor, connection


class RentModel(Model):
    def __init__(self, car_id, client_id, days_qty, total_price, start_date=None, active=True):
        self.car_id = car_id
        self.client_id = client_id
        self.days_qty = days_qty
        self.total_price = total_price
        self.start_date = start_date
        self.active = active

    table = "rents"
    required_columns = ["car_id", "client_id", "days_qty", "total_price"]

    @classmethod
    def get_full_info(cls, id=None):
        sql = f'''SELECT re.id AS rent_number, cl.name||" #"||cl.id AS client_name, cl.license_num as driver_license,
                            ca.model AS car_model,
                            ca.license_plates, re.start_date, re.days_qty, re.total_price, re.active AS active_status
                    FROM rents re 
                    JOIN cars ca ON re.car_id = ca.id
                    JOIN clients cl ON re.client_id = cl.id
                    WHERE ? IS NULL OR re.id = ?;'''
        cursor.execute(sql, (id, id))
        columns = [desc[0] for desc in cursor.description]
        vals = cursor.fetchall()
        return {'columns': columns, 'values': vals, 'qty': len(vals)}

    @classmethod
    def search_full_info(cls, val):
        val = f"%{val}%"
        sql = f'''SELECT re.id AS rent_number, cl.name||" #"||cl.id AS client_name, cl.license_num as driver_license,
                            ca.model AS car_model,
                            ca.license_plates, re.start_date, re.days_qty, re.total_price, re.active AS active_status
                    FROM rents re 
                    JOIN cars ca ON re.car_id = ca.id
                    JOIN clients cl ON re.client_id = cl.id
                    WHERE ca.license_plates LIKE ?
                    OR cl.license_num LIKE ?
                    '''
        cursor.execute(sql, (val, val))
        columns = [desc[0] for desc in cursor.description]
        vals = cursor.fetchall()
        return {'columns': columns, 'values': vals, 'qty': len(vals)}
