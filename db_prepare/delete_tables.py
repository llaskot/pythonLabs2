import sqlite3

from connection import DB_PATH

delete_cars = '''DROP TABLE IF EXISTS cars;'''
delete_users = '''DROP TABLE IF EXISTS clients;'''
delete_rents = '''DROP TABLE IF EXISTS rents;'''

if __name__ == '__main__':
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(delete_cars)
        cursor.execute(delete_users)
        cursor.execute(delete_rents)
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        print(cursor.fetchall())
