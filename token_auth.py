import uuid
import datetime
import sqlite3

conn = sqlite3.connect('shelter_finder.db') 
c = conn.cursor()
# create a token
def create():
    print("[APP] Token created")
    return uuid.uuid4()

# store the token into the database
def store(username, token):
    sql = "INSERT INTO auth (username, token, expiry) VALUES (%s, %s, %s)"
    c.execute(sql, username, token, datetime.datetime.now())
    conn.commit()
    conn.close()
    print("[APP] Token Stored")

# validate the token aka check if it is expired, if it is delete it from the database
def validate(date, token):
    if date > datetime.datetime.now():
        return True
    # token is expired so remove it from the database
    sql = "DELETE FROM auth WHERE token = %s"
    c.execute(sql,token)
    conn.close()
    print("[APP] Token expired, Token delete from database")
    return False

# find the token in the database, return false if token doesnt exist or is invalid
def find(token):
    c.execute("SELECT username,expiry,token FROM auth WHERE token=%(token)s",{'token':token})
    result = c.fetchone()
    conn.close()
    if result == None:
        return False
    if validate(result[1],result[2]):
        print("[APP] Token validated for " + result[0])
        return True
    
    return False
    
    