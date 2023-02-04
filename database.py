import hashlib
import sqlite3

def Hash(word):
    
    # encode it to bytes using UTF-8 encoding
    hashed = hashlib.sha256(word.encode()).hexdigest()
    return hashed

sqlite3.connect('shelter_finder.db')
conn = sqlite3.connect('shelter_finder.db') 
c = conn.cursor()


def create_user(conn, user):
    sql = ''' INSERT INTO user(username,password)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()
    return cur.lastrowid


def create_shelter(conn, shelter):

    sql = ''' INSERT INTO shelter(name,adress,email,telephone)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, shelter)
    conn.commit()
    return cur.lastrowid

def create_database():
    c.execute('''
            CREATE TABLE IF NOT EXISTS users  (user_id INTEGER PRIMARY KEY, 
            username VARCHAR(110) NOT NULL, 
            password VARCHAR(110) NOT NULL, 
            email VARCHAR(50) NOT NULL,
            shelter VARCHAR(50) NOT NULL)
            ''')
            
    c.execute('''
            CREATE TABLE IF NOT EXISTS shelters
            ([shelter_id] INTEGER PRIMARY KEY, 
            [name] VARCHAR(100) NOT NULL,
            [adress] VARCHAR(100) NOT NULL,
            [email] VARCHAR(100) NOT NULL,
            [tel] VARCHAR(100) NOT NULL
            )
            ''')

    c.execute('''
            CREATE TABLE IF NOT EXISTS shelter_info
            ([shelter] VARCHAR(100) NOT NULL,
            [shower] BOOLEAN NOT NULL CHECK (shower IN (0,1)),
            [bed] BOOLEAN NOT NULL CHECK (bed IN (0,1)),
            [food] BOOLEAN NOT NULL CHECK (food IN (0,1)),
            [therapist] BOOLEAN NOT NULL CHECK (therapist IN (0,1))
            )
            ''')      
    conn.commit()

