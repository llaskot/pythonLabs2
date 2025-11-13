import unittest
import sqlite3
from datetime import datetime

from db_prepare.create_tables import create_cars_table, create_users_table, create_rent_table
from db_prepare.delete_tables import delete_cars, delete_users, delete_rents
from db_prepare.insert_test_data import insert_cars, insert_users, insert_rents
from models.carModel import CarModel
from models.clientModel import ClientModel
from models.rentModel import RentModel

DB_PATH = "car_rent.db"


class BbTests(unittest.TestCase):

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
                "INSERT INTO rents (car_id, client_id, start_date, days_qty, total_price) "
                "VALUES (?, ?, ?, ?, ?);", insert_rents
            )

    def setUp(self):
        # Подключение к тестовой БД
        self.conn = sqlite3.connect(DB_PATH)
        self.cursor = self.conn.cursor()
        import models.model as model_mod
        model_mod.cursor = self.cursor
        model_mod.connection = self.conn

    def tearDown(self):
        self.cursor.close()
        self.conn.close()

    def test_itself(self):
        self.assertIsNotNone(1)

    def test_db_init(self):
        conn = sqlite3.connect('car_rent.db')
        cursor = conn.cursor()
        self.assertIsNotNone(cursor)

    def test_model_find_by(self):
        car = CarModel.find_by('id', 1)
        print(car)
        self.assertEqual({'columns': ['id', 'model', 'year', 'color', 'license_plates', 'day_price', 'insurance_price',
                                      'availability'],
                          'values': [(1, 'Toyota Corolla', 2020, 'Red', 'ABC123', 50.0, 10.0, 1)], 'qty': 1}, car)

    def test_model_create(self):
        car = CarModel("Honda Civ", 2019, "Blue", "XYZ789j", 45, 12)
        newCar = car.create()
        print('new id = ', newCar['id'])
        self.assertEqual(newCar['id'], 6)

    def test_model_update_by_id(self):
        client = ClientModel('Wasya Pupkin', None)
        res = client.update_by_id(1)
        print(res)
        print(ClientModel.find_by('id', 1))
        self.assertEqual({'success': True, 'affected_rows': 1}, res)

    def test_delete_by(self):
        res = ClientModel.delete_by('id', 2)
        print(res)
        print(ClientModel.find_by('id', 2))
        self.assertEqual({'success': True, 'affected_rows': 1}, res)

    def test_find_all(self):
        res = RentModel.find_all()
        print(res)
        self.assertEqual({'columns': ['id', 'car_id', 'client_id', 'start_date', 'days_qty', 'total_price', 'active'],
                          'values': [(1, 1, 2, datetime.now().strftime("%Y-%m-%d"), 3, 500.0, 1), (2, 2, 4, datetime.now().strftime("%Y-%m-%d"), 8, 980.0, 1)],
                          'qty': 2}, res)



def run():
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    RESET = "\033[0m"

    print(f"{CYAN}🚀 Starting Car Rent Database Tests...\n{RESET}")
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(BbTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    fails = len(result.failures)
    errors = len(result.errors)
    total = result.testsRun
    passed = total - fails - errors

    print("\n" + "-" * 40)
    print(f"{GREEN}✅ Passed: {passed}{RESET}")
    print(f"{RED}❌ Failed: {fails}{RESET}")
    print(f"{YELLOW}⚠️  Errors: {errors}{RESET}")
    print("-" * 40)

if __name__ == "__main__":
    run()