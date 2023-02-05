from flask import Flask, request, jsonify, make_response, render_template, session
from datetime import datetime, timedelta
from functools import wraps
import database
import token_auth
import func
import sqlite3

conn = sqlite3.connect('shelter_finder.db') 
c = conn.cursor()
def connection():
    conn = sqlite3.connect('shelter_finder.db', check_same_thread=False) 
    return conn 

def auth_required(tokenR):
    if not token_auth.find(tokenR):
        return False
    return True

def verifyUser(username, password):
    c.execute("SELECT username,password FROM users WHERE username=%(username)s",{"username":username}) 
    result = c.fetchone()
    if result == None: 
        return False
    if result[0] == username and result[1] == database.Hash(password):
        return True
    return False

def verifyRoot(username, password):
    password = func.Hash(password)
    if username == "admin" and password == "4813494d137e1631bba301d5acab6e7bb7aa74ce1185d456565ef51d737677b2":
        print('[APP] Root access granted')
        return True
    return False
