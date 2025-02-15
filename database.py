import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()

    #Users tableni yaratish
    def create_user_table(self, full_name, phone_number, age, address):
        self.cursor.execute(
            """CREATE TABLE users(
            id INTEGER PRIMARY KEY,
            full_name, CHAR NOT NULL,
            phone_number CHAR NOT NULL,
            age INTEGER NOT NULL)
        )
        """)
    # User tablega malumot qo'shish
    def add_to_users(self, full_name, phone_number, age, address):
        self.create_user_table()
        self.cursor.execute("""
        INSERT INTO users(
        full_name,
        phone_number,
        age,
        address)""", (full_name, phone_number, age, address)
        )
        self.connection.commit()


db= Database()