import uuid
import datetime
import sqlite3

conn = sqlite3.connect('shelter_finder.db', check_same_thread=False) 
c = conn.cursor()
def connection():
    conn = sqlite3.connect('shelter_finder.db', check_same_thread=False) 
    c = conn.cursor()
    return c


# create a token
def create():
    print("[APP] Token created")
    return uuid.uuid4()

# store the token into the database
def store(username, token):
    c = connection()
    sql = "INSERT INTO auth (username, token, expiry) VALUES (?, ?, ?)"
    c.execute(sql, (str(username), str(token), str(datetime.datetime.now())))
    conn.commit()
    print("[APP] Token Stored")

# validate the token aka check if it is expired, if it is delete it from the database
def validate(date, token):
    c = connection()

    if date > datetime.datetime.now():
        return True
    # token is expired so remove it from the database
    sql = "DELETE FROM auth WHERE token = %s"
    val = (token)
    c.execute(sql,val)
    con.commit()
    
    print("[APP] Token expired, Token delete from database")
    return False

# find the token in the database, return false if token doesnt exist or is invalid
def find(tokenr):
    c = connection()
    print(str(tokenr))
    sql = "SELECT username,expiry,token FROM auth WHERE token = ?"
    val = (str(tokenr))
    print(val)
    c.execute(sql,val)
    result = c.fetchone()
    
    if result == None:
        return False
    if validate(result[1],result[2]):
        print("[APP] Token validated for " + result[0])
        return True
    
    return False
    
    