from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent.parent  # папка на уровень выше
DB_PATH = BASE_DIR / "car_rent.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()