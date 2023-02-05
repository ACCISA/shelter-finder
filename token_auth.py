import uuid
import datetime
import sqlite3
from datetime import *

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
    co = connection()
    c = co.cursor()
    sql = "INSERT INTO auth (username, token, expiry) VALUES (?, ?, ?)"
    time = datetime.now()+timedelta(minutes=2)
    c.execute(sql, (str(username), str(token),time ))
    co.commit()
    print("[APP] Token Stored " + str(token) + "; time: " + str(time))

# validate the token aka check if it is expired, if it is delete it from the database
def validate(date, token):
    co = connection()
    c = co.cursor()    
    print(date)
    index = date.find(".")
    date = date[0:index ]
    dt_tuple=tuple([int(x) for x in date[:10].split('-')])+tuple([int(x) for x in date[11:].split(':')])
    date = datetime(*dt_tuple)
    date.replace(microsecond=0)

    if date > datetime.now().replace(microsecond=0):
        return True
    # token is expired so remove it from the database
    sql = "DELETE FROM auth WHERE token = ?"
    val = (token,)
    c.execute(sql,val)
    co.commit()
    
    print("[APP] Token expired, Token delete from database")
    return False

# find the token in the database, return false if token doesnt exist or is invalid
def find(tokenr):
    co = connection()
    c = co.cursor()
    sql = "SELECT username,expiry,token FROM auth WHERE token = ?"
    val = (str(tokenr),)
    print(val)
    c.execute(sql,val)
    result = c.fetchone()
    
    if result == None:
        return False
    if validate(result[1],result[2]):
        print("[APP] Token validated for " + result[0])
        return True
    
    return False
    
    