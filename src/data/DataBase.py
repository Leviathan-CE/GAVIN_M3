import sqlite3

class DataBase():   
    
 
    def __init__(self, name:str="Leviathan_local") -> None:  
        self._connection = None
        self._cursor = None          
        self.create_database(name=name)
        self._message_count= len(self.get_all())


    def create_database(self,name: str = "Leviathan_local"):
        try:
            self._connection = sqlite3.connect(name)
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
                             INSERT INTO messages (user,message) VALUES('{user}', '{message_content}');
                             ''')
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
        
        
if __name__ == "__main__":
    db = DataBase()
    #db.insert("test user", "message with /[x+3=y/]")
    
    print(db.get_last(3))
    db.close()
   
    