import sqlite3
from SoftToyOnlineAPI.mem_repo import ToyData, ToyMeMRepository


def create_and_populate_database(toys):
    try:
        conn = sqlite3.connect('instance/soft_toys_db.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS toys (
                id INTEGER PRIMARY KEY,
                name TEXT,
                description TEXT,
                price REAL,
                quantity INTEGER
            )
        ''')
        for toy_id, toy_data in toys.items():
            cursor.execute('''
                INSERT INTO toys (id, name, description, price, quantity)
                VALUES (?, ?, ?, ?, ?)
            ''', (toy_id, toy_data.name, toy_data.description, toy_data.price, toy_data.quantity))

        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("sql lite error ", e)
    finally:
        if conn:
            conn.close()


mem_r = ToyMeMRepository()
create_and_populate_database(mem_r.toys)
