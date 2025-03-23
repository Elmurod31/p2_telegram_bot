import sqlite3


from pydantic.v1.validators import float_finite_validator


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()







    #Ichimliklar tableni yaratish
    def create_table_ichimliklar(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS ichimliklar(
            id INTEGER PRIMARY KEY,
            nomi CHAR NOT NULL,
            hajmi CHAR NOT NULL,
            soni INTEGER NOT NULL,
            shakarli BOOLEAN DEFAULT FALSE) 
        """)
    def add_to_ichimliklar(self, nomi, hajmi, soni, shakarli):
        self.create_table_ichimliklar()
        self.cursor.execute("""
        INSERT INTO ichimliklar(nomi, hajmi, soni, shakarli)
            VALUES (?, ?, ?, ?) 
            """, (nomi, hajmi, soni, shakarli)
)
        self.connection.commit()







    #Mevalar tablesini yaratish
    def create_table_mevalar(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS mevalar(
            id INTEGER PRIMARY KEY,
            nomi CHAR NOT NULL,
            ogirli CHAR NOT NULL,
            rangi CHAR NOT NULL,
            shakli CHAR NOT NULL)
        """)
    def add_to_mevalar(self, nomi, ogirligi, rangi, shakli):
        self.create_table_mevalar()
        self.cursor.execute("""
        INSERT INTO mevalar(nomi, ogirli, rangi, shakli)
            VALUES (?, ?, ?, ?)
            """, (nomi, ogirligi, rangi, shakli)
)
        self.connection.commit()


    # Go'sht tablesini yaratish
    def create_table_goshtlar(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS goshtlar(
            id INTEGER PRIMARY KEY,
            turi CHAR NOT NULL,
            ogirli CHAR NOT NULL,
            rangi CHAR NOT NULL,
            shakli CHAR NOT NULL)
        """)

    def add_to_goshtlar(self, turi, ogirligi, rangi, shakli):
        self.create_table_goshtlar()
        self.cursor.execute("""
            INSERT INTO goshtlar(turi, ogirli, rangi, shakli)
                VALUES (?, ?, ?, ?)
                """, (turi, ogirligi, rangi, shakli)
)
        self.connection.commit()



    # Sut tablesini yaratish
    def create_table_sutlar(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS sutlar(
            id INTEGER PRIMARY KEY,
            nomi CHAR NOT NULL,
            yog_mikdori CHAR NOT NULL,
            ogirligi CHAR NOT NULL,
            narxi CHAR NOT NULL)
        """)

    def add_to_sutlar(self, nomi, yog_mikdori, ogirligi, narxi):
        self.create_table_sutlar()
        self.cursor.execute("""
            INSERT INTO sutlar(nomi, yog_mikdori, ogirligi, narxi)
                VALUES (?, ?, ?, ?)
                """, (nomi, yog_mikdori, ogirligi, narxi)
                            )
        self.connection.commit()


    # Soatlar tablesini yaratish
    def create_table_soatlar(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS soatlar(
            id INTEGER PRIMARY KEY,
            brendi CHAR NOT NULL,
            materyali CHAR NOT NULL,
            narxi CHAR NOT NULL,
            turi CHAR NOT NULL)
        """)

    def add_to_soatlar(self, brendi, materyali, narxi, turi):
        self.create_table_soatlar()
        self.cursor.execute("""
            INSERT INTO soatlar(brendi, materyali, narxi, turi)
                VALUES (?, ?, ?, ?)
                """, (brendi, materyali, narxi, turi)
)
        self.connection.commit()


    # Oyoq kiyimlar tablesini yaratish
    def create_table_Oyoq_kiyimlar(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS Oyoq_kiyimlar(
            id INTEGER PRIMARY KEY,
            modeli CHAR NOT NULL,
            quvvat CHAR NOT NULL,
            batareya BOOLEAN NOT NULL,
            narxi CHAR NOT NULL)
        """)

    def add_to_Oyoq_Kiyim(self, brendi, razmeri, materyali, narxi):
        self.create_table_Oyoq_kiyimlar()
        self.cursor.execute("""
            INSERT INTO Oyoq_kiyimlar(brendi, razmeri, materyali, narxi)
                VALUES (?, ?, ?, ?)
                """, (brendi, razmeri, materyali, narxi)
                            )
        self.connection.commit()

    # Elektromobillar tablesini yaratish
    def create_table_Elektromobillar(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS Elektromobillar(
            id INTEGER PRIMARY KEY,
            modeli CHAR NOT NULL,
            quvvat CHAR NOT NULL,
            batareya BOOLEAN NOT NULL,
            narxi CHAR NOT NULL)
        """)

    def add_to_Elektromobillar(self, modeli, quvvat, batareya, narxi):
        self.create_table_Elektromobillar()
        self.cursor.execute("""
            INSERT INTO Elektromobillar(modeli, quvvat, batareya, narxi)
                VALUES (?, ?, ?, ?)
                """, (modeli, quvvat, batareya, narxi)
)
        self.connection.commit()

    # Smartfonlar tablesini yaratish
    def create_table_Smartfonlar(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS Smartfonlar(
            id INTEGER PRIMARY KEY,
            brendi CHAR NOT NULL,
            modeli CHAR NOT NULL,
            xotira CHAR NOT NULL,
            narxi CHAR NOT NULL)
        """)

    def add_to_Smartfonlar(self, brendi, modeli, xotira, narxi):
        self.create_table_Smartfonlar()
        self.cursor.execute("""
            INSERT INTO Smartfonlar(brendi, modeli, xotira, narxi)
                VALUES (?, ?, ?, ?)
                """, (brendi, modeli, xotira, narxi)
)
        self.connection.commit()

    # Notebooklar tablesini yaratish
    def create_table_Notebooklar(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS Notebooklar(
            id INTEGER PRIMARY KEY,
            brendi CHAR NOT NULL,
            protsessor CHAR NOT NULL,
            ram CHAR NOT NULL,
            narxi CHAR NOT NULL)
        """)

    def add_to_Notebooklar(self, brendi, protsessor, ram, narxi):
        self.create_table_Notebooklar()
        self.cursor.execute("""
            INSERT INTO Notebooklar(brendi, protsessor, ram, narxi)
                VALUES (?, ?, ?, ?)
                """, (brendi, protsessor, ram, narxi)
                            )
        self.connection.commit()


    # Kampiyuterlar tablesini yaratish
    def create_table_Kompiyuter(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS Kompiyuterlar(
            id INTEGER PRIMARY KEY,
            brendi CHAR NOT NULL,
            protsessor CHAR NOT NULL,
            videokarta CHAR NOT NULL,
            narxi CHAR NOT NULL)
        """)

    def add_to_Kompyuterlar(self, brendi, protsessor, videokarta, narxi):
        self.create_table_Kompiyuter()
        self.cursor.execute("""
            INSERT INTO Kompiyuterlar(brendi, protsessor, videokarta, narxi)
                VALUES (?, ?, ?, ?)
                """, (brendi, protsessor, videokarta, narxi)
                            )
        self.connection.commit()




    def create_user_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                telegram_id INTEGER UNIQUE,
                is_seller BOOLEAN,
                full_name TEXT,
                phone_number TEXT,
                age INTEGER,
                address TEXT
    )""")
        self.connection.commit()

    def get_telegram_user_from_db(self, telegram_id):
        self.create_user_table()
        user = {}
        db_user = self.cursor.execute("""
        SELECT * FROM users WHERE telegram_id = ?""",
                                      (telegram_id,)).fetchone()
        if db_user:
            user["id"] = db_user[0]
            user["telegram_id"] = db_user[1]
            user["is_seller"] = db_user[2]
            user["full_name"] = db_user[3]
            user["phone_number"] = db_user[4]
            user["age"] = db_user[5]
            user["address"] = db_user[6]
            return user
        return None





    def get_ichimliklar(self, ):
        ichimliklar = self.cursor.execute("""
        SELECT * FROM ichimliklar""")
        return ichimliklar.fetchall()


    def get_mevalar(self, ):
        mevalar = self.cursor.execute("""
        SELECT * FROM mevalar""")
        return mevalar.fetchall()


    def get_goshtlar(self, ):
        goshtlar = self.cursor.execute("""
        SELECT * FROM goshtlar""")
        return goshtlar.fetchall()

# Database obyektini yaratamiz
db = Database()