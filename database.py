import hashlib
import sqlite3
from verification import verify_user, verify_shelter

from func import Hash



conn = sqlite3.connect('shelter_finder.db') 
c = conn.cursor()


def create_user(username, password, email, shelter):
    if(verify_user(username)):
        return False
    user=[username,password,email,shelter]
    sql = ''' INSERT INTO user(username,password,email,shelter)
              VALUES(?,?,?,?) '''
        
    for parameter in user:
        if  isinstance(parameter,str):
            raise Exception("a parameter in user is not a string")
    c.execute(sql, username, password, email, shelter)
    conn.commit()
    return True


def create_shelter(name, long, lat, adress, email, tel):
    args = [name, long, lat, adress, email, tel]
    if (verify_shelter(args)):
        return False
    sql = ''' INSERT INTO shelter(name,long,lat,email,tel)
              VALUES(?,?,?,?,?) '''
    

    

    for arg in args:
        if arg == None or arg == "":
            raise Exception("Arguments cannot be null")
        if arg==long or arg==lat:
            if not isinstance(arg, float):
                raise Exception("Longitude or Latitude has to be a number") 
        if not isinstance(arg, str):
            raise Exception("Shelter must be a string")
        

    c.execute(sql, name, long, lat, adress, email, tel)
    conn.commit()
    return True

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
    c.execute('''
            CREATE TABLE IF NOT EXISTS auth
            ([shelter_id] INTEGER PRIMARY KEY, 
            [name] VARCHAR(100) NOT NULL,
            [adress] VARCHAR(100) NOT NULL,
            [email] VARCHAR(100) NOT NULL,
            [tel] VARCHAR(100) NOT NULL
            )
            ''')       
    conn.commit()

