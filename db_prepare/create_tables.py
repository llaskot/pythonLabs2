import sqlite3

conn = sqlite3.connect('db.sqlite')
cursor = conn.cursor()

create_tables = '''CREATE TABLE IF NOT EXISTS cars (
    id INTEGER PRIMARY KEY,
    model TEXT,
    `year` INTEGER,
    collor TEXT,
    licnse_plates TEXT,
    day_price REAL,
    insurance_price REAL
);
'''

cursor.execute(create_tables)