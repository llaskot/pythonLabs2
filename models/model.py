from connection import cursor, connection


class Model:
    required_columns = None
    table = None

    def create(self):
        fields = []
        place_holder = []
        values = []
        for (key, value) in self.__dict__.items():
            if key in self.required_columns and value is None:
                raise KeyError(f'The values of {self.required_columns} must be truthy')
            fields.append(key)
            place_holder.append(' ?')
            values.append(value)
        sql = f'''INSERT INTO {self.table} ({', '.join(fields)}) VALUES ({', '.join(place_holder)})'''
        cursor.execute(sql, values)
        connection.commit()
        setattr(self, 'id', cursor.lastrowid)
        return self.__dict__

    def update_by_id(self, id: int):
        fields = []
        values = []
        for (key, value) in self.__dict__.items():
            if value is not None:
                fields.append(f'{key} = ?')
                values.append(value)
        values.append(id)
        sql = f'''UPDATE {self.table} 
         SET {',\n '.join(fields)} WHERE id = ?'''
        cursor.execute(sql, values)
        print(cursor.rowcount)
        connection.commit()
        return {'success': True, 'affected_rows': cursor.rowcount}

    @classmethod
    def find_by(cls, key, value):
        sql = f'''SELECT *
            FROM {cls.table}
            WHERE {key} = ?'''
        cursor.execute(sql, (value,))
        columns = [desc[0] for desc in cursor.description]
        vals = cursor.fetchall()
        return {'columns': columns, 'values': vals, 'qty': len(vals)}

    @classmethod
    def delete_by(cls, key, value):
        sql = f'''DELETE 
            FROM {cls.table}
            WHERE {key} = ?'''
        cursor.execute(sql, (value,))
        connection.commit()
        return {'success': True, 'affected_rows': cursor.rowcount}
