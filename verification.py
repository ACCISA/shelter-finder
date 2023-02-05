import sqlite3
from func import Hash

conn = sqlite3.connect('shelter_finder.db') 
c = conn.cursor()



def verify_shelter(name):
    c.execute("SELECT shelter_id FROM shelters WHERE name=%(name)s",{"name":name}) 
    result= c.fetchone()
    conn.close()
    if result== None:
        return False
    return True
    

def verify_user(user):
    u=Hash(user)
    c.execute("SELECT user_id FROM users WHERE user=%(u)s",{"u":u}) 
    result= c.fetchone()
    conn.close()
    if result== None:
        return False
    return True

def verify_shelter_info(shelter_inf):
    c.execute("SELECT shelter_info_id FROM shelter_info WHERE shelter=%(shelter)s",{"shelter":shelter_inf}) 
    result= c.fetchone()
    conn.close()
    if result== None:
        return False
    return True



