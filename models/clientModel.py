from connection import cursor
from models.model import Model


class ClientModel(Model):
    def __init__(self, name, license_num):
        self.name = name
        self.license_num = license_num

    table = "clients"
    required_columns = {'name', 'license_num'}

    @classmethod
    def search(cls, val):
        val = f"%{val}%"
        sql = f'''
        SELECT *
        FROM clients 
        WHERE id LIKE ?
        OR name LIKE ?
        OR license_num LIKE ?
        '''
        cursor.execute(sql, (val, val, val))
        columns = [desc[0] for desc in cursor.description]
        vals = cursor.fetchall()
        return {'columns': columns, 'values': vals, 'qty': len(vals)}

