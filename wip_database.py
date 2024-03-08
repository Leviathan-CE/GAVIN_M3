from src.data.DataBase import DataBase
from cryptography.fernet import Fernet


print(Fernet.generate_key().decode())
db = DataBase()
    # db.insert("test user", "message with /[x+3=y/]")

print(db.get_last(3))
db.close()
