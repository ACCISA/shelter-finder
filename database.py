import hashlib
import sqlite3

def Hash(word):
    
    # encode it to bytes using UTF-8 encoding
    hashed = hashlib.sha256(word.encode()).hexdigest()
    return hashed

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


