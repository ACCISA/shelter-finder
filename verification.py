import sqlite3
from func import Hash

conn = sqlite3.connect('shelter_finder.db', check_same_thread=False) 
c = conn.cursor()
def connection():
    conn = sqlite3.connect('shelter_finder.db', check_same_thread=False) 
    return conn



def verify_shelter(name):
    co = connection()
    c = co.cursor()
    sql = "SELECT shelter_id FROM shelters WHERE name=?"
    val = (name,)
    c.execute(sql,val)
    result= c.fetchone()
    # conn.close()
    if result== None:
        return False
    return True
    

def verify_user(user):
    co = connection()
    c = co.cursor()
    sql = "SELECT user_id FROM users WHERE username=?"
    val  = (user,)
    c.execute(sql,val) 
    result= c.fetchone()
    conn.close()
    if result== None:
        return False
    return True

def verify_shelter_info(shelter_inf):
    co = connection()
    c = co.cursor()
    c.execute("SELECT shelter_info_id FROM shelter_info WHERE shelter=%(shelter)s",{"shelter":shelter_inf}) 
    result= c.fetchone()
    conn.close()
    if result== None:
        return False
    return True



