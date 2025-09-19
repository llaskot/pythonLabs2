import sqlite3

from db_prepare.connection import DB_PATH

# connection = sqlite3.connect(DB_PATH)



create_cars_table = '''CREATE TABLE IF NOT EXISTS cars (
    id INTEGER PRIMARY KEY,
    model TEXT NOT NULL,
    `year` INTEGER NOT NULL,
    color TEXT NOT NULL,
    license_plates TEXT  UNIQUE NOT NULL,
    day_price REAL DEFAULT 0,
    insurance_price REAL DEFAULT 0,
    avalabulity INTEGER DEFAULT 1 NOT NULL
);
'''

create_users_table = '''CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY,
    `name` TEXT NOT NULL,
    license_num TEXT UNIQUE NOT NULL
);
'''

create_rent_table = '''CREATE TABLE IF NOT EXISTS rents (
    car_id INTEGER NOT NULL,
    client_id INTEGER NOT NULL,
    days_qty INTEGER NOT NULL,
    total_price REAL NOT NULL,
    active INTEGER NOT NULL DEFAULT 1,
    FOREIGN KEY (car_id) REFERENCES cars(id) ON DELETE SET NULL  
    FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE SET NULL
);
'''

if __name__ == '__main__':
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(create_cars_table)
        cursor.execute(create_users_table)
        cursor.execute(create_rent_table)
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        print(cursor.fetchall())