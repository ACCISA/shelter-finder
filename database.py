import hashlib
import sqlite3

def Hash(word):
    #
    # encode it to bytes using UTF-8 encoding
    hashed = hashlib.sha256(word.encode()).hexdigest()
    return hashed


conn = sqlite3.connect('shelter_finder.db') 
c = conn.cursor()


def create_user(username, password, email, shelter):
    sql = ''' INSERT INTO user(username,password,email,shelter)
              VALUES(?,?) '''
    for parameter in user:
        if  isinstance(parameter,str):
            raise Exception("a parameter in user is not a string")
    c.execute(sql, username, password, email, shelter)
    conn.commit()


def create_shelter(shelter, name, adress, email):

    sql = ''' INSERT INTO shelter(name,adress,email,tel)
              VALUES(?,?,?,?) '''
    

    args = [shelter, name, adress, email]

    for arg in range(len(args)):
        if not isinstance(arg, str):
            raise Exception("Shelter must be a string")
        if arg[i] == None or ar[i] == "":
            raise Exception("Arguments cannot be null")

    c.execute(sql, shelter, name, adress, email)
    conn.commit()

def create_shelter_info(conn, shelter_info):

    sql = ''' INSERT INTO shelter_info(shelter,shower,bed,food,therapist)
              VALUES(?,?,?,?,?) '''
    
    if  isinstance(shelter_info[0],str):
        raise Exception("shelter in shelter_info is not a string")

    for i in range(len(shelter_info)):
        if i == 0: continue
        if shelter_info[i] != 0 or shelter_info[i] != 1:
            raise Exception("Shelter info must be 0 or 1")

    c.execute(sql, shelter_info[0], shelter_info[1], shelter_info[2], shelter_info[3], shelter_info[4])
    conn.commit()

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
            ([shelter_info_id] INTEGER PRIMARY KEY,
            [shelter] VARCHAR(100) NOT NULL,
            [shower] BOOLEAN NOT NULL CHECK (shower IN (0,1)),
            [bed] BOOLEAN NOT NULL CHECK (bed IN (0,1)),
            [food] BOOLEAN NOT NULL CHECK (food IN (0,1)),
            [therapist] BOOLEAN NOT NULL CHECK (therapist IN (0,1))
            )
            ''')      
    conn.commit()

