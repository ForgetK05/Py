from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent



'''
Dấu / đi vào bên trong thư mục và tạo ra file db.sqlite3
'''
DB_PATH = BASE_DIR / 'db.sqlite3'


print(BASE_DIR,'\n', DB_PATH)