import unittest
import sqlite3


class BbTests(unittest.TestCase):

    def test_db_init(self):
        conn = sqlite3.connect('cars_rent.db')
        cursor = conn.cursor()
        assert cursor

    def test_itself(self):
        assert 1
