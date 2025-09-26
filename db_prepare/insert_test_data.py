import sqlite3
from datetime import datetime

from connection import DB_PATH

insert_cars = [
    ("Toyota Corolla", 2020, "Red", "ABC123", 50, 10),
    ("Honda Civic", 2019, "Blue", "XYZ789", 45, 12),
    ("Ford Focus", 2021, "Black", "DEF456", 55, 15),
    ("Chevrolet Malibu", 2018, "White", "GHI321", 40, 8),
    ("Nissan Altima", 2022, "Gray", "JKL654", 60, 20)
]

insert_users = [
    ("Alice", "L12345"),
    ("Bob", "L23456"),
    ("Charlie", "L34567"),
    ("Diana", "L45678"),
    ("Eve", "L56789")
]

insert_rents = [
    (1, 2, datetime.now().strftime("%Y-%m-%d") , 3, 500),
    (2, 4, datetime.now().strftime("%Y-%m-%d") , 8, 980)

]

if __name__ == '__main__':
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()

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

