import sqlite3
from verification import verify_user, verify_shelter

from func import Hash



conn = sqlite3.connect('shelter_finder.db', check_same_thread=False) 
c = conn.cursor()
def connection():
    conn = sqlite3.connect('shelter_finder.db', check_same_thread=False) 
    return conn



def create_user(username, password, email, shelter):
    
    if(verify_user(username)):
        return False
    co=connection()
    c = co.cursor()
    user=[username,password,email,shelter] #here it isw2xxx22
    sql = ''' INSERT INTO users(username,password,email,shelter)
              VALUES(?,?,?,?) '''
        
    for parameter in user:
        if not isinstance(parameter,str):
            raise Exception("a parameter in user is not a string")
    c.execute(sql, (username, Hash(password), email, shelter))
    co.commit()
    co.close()
    return True


def create_shelter(name, long, lat, adress, email, tel, logo):
    
    args = [name, long, lat, adress, email, tel, logo]
    if (verify_shelter(args)):
        return False
    c=connection()
    sql = ''' INSERT INTO shelters(name,long,lat,adress,email,tel,logo)
              VALUES(?,?,?,?,?,?,?) '''
    

    

    for arg in args:
        if arg == None or arg == "":
            raise Exception("Arguments cannot be null")
        if arg==long or arg==lat:
            if not isinstance(arg, float):
                raise Exception("Longitude or Latitude has to be a number")
            continue
        if not isinstance(arg, str):
            raise Exception("Shelter must be a string")
        

    c.execute((sql, name, long, lat, adress, email, tel, logo))
    conn.commit()
    conn.close()
    return True


def create_shelter_info(name, shower, bed, food, therapist):
    args = [name, shower, bed, food, therapist]
    if (verify_shelter(args[0])):
        return False

    co = connection()
    c = co.cursor()
    sql = '''INSERT INTO shelters(name,shower,bed,food,therapist)
                  VALUES(?,?,?,?,?)'''

    for arg in args:
        if arg == None or arg == "":
            raise Exception("Arguments cannot be null")
        if arg == shower or arg == bed or arg==food or arg==therapist:
            if not arg==0 and not arg==1:
                raise Exception("Longitude or Latitude has to be a number")
            continue
        if not isinstance(arg, str):
            raise Exception("Shelter must be a string")

    c.execute(sql, (name, shower, bed, food, therapist))
    co.commit()
    co.close()
    return True


def get_shelters():
    c=connection()
    c.execute("SELECT * FROM shelters") 
    result= c.fetchall()
    c.close()
    return result

def get_shelters_info():
    c=connection()
    c.execute("SELECT * FROM shelter_info") 
    result= c.fetchall()
    c.close()
    return result

def get_shelters_names():
    c=connection()
    c.execute("SELECT name FROM shelters") 
    result= c.fetchall()
    c.close()
    return result

def create_database():
    c=connection()
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
            [long] VARCHAR(50) NOT NULL,
            [lat] VARCHAR(50) NOT NULL,
            [email] VARCHAR(100) NOT NULL,
            [tel] VARCHAR(100) NOT NULL,
            [logo] VARCHAR(100) NOT NULL
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
            ([auth_id] INTEGER PRIMARY KEY, 
            [username] VARCHAR(100) NOT NULL,
            [token] VARCHAR(100) NOT NULL,
            [expiry] DATETIME NOT NULL
            )
            ''')       
    conn.commit()
    conn.close()

