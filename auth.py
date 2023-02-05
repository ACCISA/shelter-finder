from flask import Flask, request, jsonify, make_response, render_template, session
from datetime import datetime, timedelta
from functools import wraps
import database
import sqlite3
import token_auth
import func

conn = sqlite3.connect('shelter_finder.db', check_same_thread=False) 
c = conn.cursor()
def connection():
    conn = sqlite3.connect('shelter_finder.db', check_same_thread=False) 
    return conn



def auth_required(tokenR):
    if not token_auth.find(tokenR):
        return False
    return True

def verifyUser(username, password):
    co = connection()
    c = co.cursor()
    password = func.Hash(password)
    sql = "SELECT username, password FROM users WHERE username =? "
    val = (username,)
    c.execute(sql,val)
    result = c.fetchone()
    if result == None:
        return False
    if result[0] == username and result[1] == password:
        return True
    return False
 

def verifyRoot(username, password):
    username = func.Hash(username)
    password = func.Hash(password)
    if username == "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918" and password == "4813494d137e1631bba301d5acab6e7bb7aa74ce1185d456565ef51d737677b2":
        print('[APP] Root access granted')
        return True
    return False
