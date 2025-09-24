import unittest
import sqlite3

from db_prepare.create_tables import create_cars_table, create_users_table, create_rent_table
from db_prepare.delete_tables import delete_cars, delete_users, delete_rents
from db_prepare.insert_test_data import insert_cars, insert_users, insert_rents
from models.carModel import CarModel

DB_PATH = "car_rent.db"


class BbTests(unittest.TestCase):

    # conn
    # cursor

    @classmethod
    def setUpClass(cls):
        print("Before all tests")
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(delete_cars)
            cursor.execute(delete_users)
            cursor.execute(delete_rents)
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            print(cursor.fetchall())

            cursor.execute(create_cars_table)
            cursor.execute(create_users_table)
            cursor.execute(create_rent_table)
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            print(cursor.fetchall())

            cursor.executemany(
                "INSERT INTO cars (model, year, color, license_plates, day_price, insurance_price) VALUES (?, ?, ?, ?, ?, ?);",
                insert_cars
            )

            cursor.executemany(
                "INSERT INTO clients (name, license_num) VALUES (?, ?);",
                insert_users
            )

            cursor.executemany(
                "INSERT INTO rents (car_id, client_id, days_qty, total_price) "
                "VALUES (?, ?, ?, ?);", insert_rents
            )



    def test_itself(self):
        self.assertIsNotNone( 1)

    def test_db_init(self):
        conn = sqlite3.connect('car_rent.db')
        cursor = conn.cursor()
        self.assertIsNotNone(cursor)

    def test_model_find_by(self):
        car = CarModel.find_by('id', 1)
        self.assertEqual({'columns': ['id', 'model', 'year', 'color', 'license_plates', 'day_price', 'insurance_price', 'availability'], 'values': [(1, 'Toyota Corolla', 2020, 'Red', 'ABC123', 50.0, 10.0, 1)], 'qty': 1}, car)

