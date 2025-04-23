from database import db

ichimliklar = db.get_ichimliklar()
print(f"Nomi: {ichimliklar[1][1]}")
print(f"Nomi: {ichimliklar[1][2]}")
print(f"Nomi: {ichimliklar[1][3]}")
print(f"Nomi: {ichimliklar[1][4]}")