import hashlib
import sqlite3

def CreateUser(Username, Password):
    
    # encode it to bytes using UTF-8 encoding
    username = hashlib.sha256(Username.encode()).hexdigest()
    password= hashlib.sha256(Password.encode()).hexdigest()
    return username, password

sqlite3.connect('shelter_finder.db')
conn = sqlite3.connect('shelter_finder.db') 
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS users
          ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT)
          ''')
          
c.execute('''
          CREATE TABLE IF NOT EXISTS shelters
          ([product_id] INTEGER PRIMARY KEY, [price] INTEGER)
          ''')
                     
conn.commit()


