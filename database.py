import hashlib
import sqlite3

def CreateUser(Username, Password):
    
    # encode it to bytes using UTF-8 encoding
    username = hashlib.sha256(Username.encode()).hexdigest()
    password= hashlib.sha256(Password.encode()).hexdigest()
    return username, password

sqlite3.connect('shelter_finder.db')



