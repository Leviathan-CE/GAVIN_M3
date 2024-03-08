import sqlite3
import os
class KeyManager():
    

    
    def __init__(self) -> None:
        self._connection = None
        self._cursor = None          
        self.create_database()
    
    def create_database(self):
        from src.data.Paths import DATA
        try:
            self._connection = sqlite3.connect(f"{DATA}/Key_manager")
            self._cursor = self._connection.cursor()
        except sqlite3.Error as e:
            print(f"failed to connect to databse 'Key_manager' : {e}")

        self._cursor.execute('''CREATE TABLE IF NOT EXISTS api_keys(
            KeyName TEXT PRIMARY KEY,            
            APIKey TEXT
        );''')
    
    def get_key(self, name:str) -> str:
        import configparser
        from src.data.Paths import DATA
        from cryptography.fernet import Fernet
        path = f"{DATA}/config.ini"
        
        #if config not iniailtized make new and gen key
        if not os.path.exists(path):
            os.makedirs(os.path.dirname(path),exist_ok=True)
            with open(path, 'w') as file:
                file.write(f'''
                           [DEFAULT]
                           encryption_key = '{Fernet.generate_key().decode()}'
                           ''')
                # Set the file permissions to w/r for the owner
                os.chmod(path, '0o600')
                
        config = configparser.ConfigParser()
        config.read(path)

        crypt_key = config["DEFAULT"]["encryption_key"]
        cipher = Fernet(crypt_key.encode())
        
        self._cursor.execute(f'''
                             SELECT * FROM api_keys WHERE KeyName = ?
                             ''',(name,))
        encrypted_key:str = self._cursor.fetchone()[1]       
        decrypted_key = cipher.decrypt(encrypted_key.encode())
        return decrypted_key.decode()

    def set_key(self, name:str, key:str):
        import configparser
        from src.data.Paths import DATA
        from cryptography.fernet import Fernet
        path = f"{DATA}/config.ini"
        
        #if config not iniailtized make new and gen key
        if not os.path.exists(path):
            os.makedirs(os.path.dirname(path),exist_ok=True)
            with open(path, 'w') as file:
                file.write(f'''
                           [DEFAULT]
                           encryption_key = '{Fernet.generate_key().decode()}'
                           ''')
                # Set the file permissions to w/r for the owner
                os.chmod(path, '0o600')       
        
        
        config = configparser.ConfigParser()
        config.read(path)
        
        crypt_key = config["DEFAULT"]["encryption_key"]
        cipher = Fernet(crypt_key.encode())
        encrypted_key =  cipher.encrypt(key.encode())
        encrypted_key = encrypted_key.decode()
        
        self._cursor.execute(f'''
                             INSERT OR REPLACE INTO api_keys (KeyName,APIKey) VALUES("{name}", "{encrypted_key}");
                             ''')
        self._connection.commit()
    
    def close(self):
        self._cursor.close()
        self._connection.close()
        

    
class DataBase():   
    
 
    def __init__(self, name:str="Leviathan_local") -> None:  
        self._connection = None
        self._cursor = None          
        self.create_database(name=name)
        self._message_count= len(self.get_all())


    def create_database(self,name: str = "Leviathan_local"):
        from src.data.Paths import DATA
        try:
            self._connection = sqlite3.connect(f"{DATA}/{name}")
            self._cursor = self._connection.cursor()
        except sqlite3.Error as e:
            print(f"failed to connect to databse '{name}' : {e}")
        
        self._cursor.execute('''CREATE TABLE IF NOT EXISTS messages(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            message TEXT
        );''')
    
    def insert(self,user:str, message_content:str):        
        self._cursor.execute(f'''
                             INSERT INTO messages (user,message) VALUES(?,?);
                             ''',(user,message_content,))
        self._connection.commit()
    def get_all(self) -> list:
         self._cursor.execute('''
                             SELECT * FROM messages;
                             ''')
         return self._cursor.fetchall()
    
    def get_last(self,num:int):
        self._cursor.execute(f'''
                             SELECT * FROM messages ORDER by id DESC LIMIT {num};
                             ''')
        return self._cursor.fetchall()
    
    def get(self, num:int):
        self._cursor.execute(f'''
                             SELECT * FROM messages ORDER by id LIMIT {num};
                             ''')
        return self._cursor.fetchall()
        
    def close(self):
        self._cursor.close()
        self._connection.close()
        
        

   
    