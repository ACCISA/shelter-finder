import sqlite3
from database import conn
from database import Hash

c=conn.cursor()
def verify_shelter(shelter):
    c.execute("SELECT shelter_id FROM shelters WHERE shelter=%(shelter)s",{"shelter":shelter}) 
    result= c.fetchone()
    if result== None:
        return False
    return True

def verify_user(user):
    u=Hash(user)
    c.execute("SELECT user_id FROM users WHERE user=%(u)s",{"u":u}) 
    result= c.fetchone()
    if result== None:
        return False
    return True

def verify_shelter_info(shelter_inf):
    c.execute("SELECT shelter_info_id FROM shelter_info WHERE shelter=%(shelter)s",{"shelter":shelter_inf}) 
    result= c.fetchone()
    if result== None:
        return False
    return True



