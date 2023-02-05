from flask import Flask, request, jsonify, make_response, render_template, session
from datetime import datetime, timedelta
from functools import wraps
import database
import token_auth
import func

def auth_required(tokenR):
    if not token_auth.find(tokenR):
        return False
    return True

def verifyUser(username, password):
    username = database.Hash(username)
    password = database.Hash(password)
    # TODO RICHARD
    # find if the username and passowrd are true
    # if true return True

def verifyRoot(username, password):
    username = func.Hash(username)
    password = func.Hash(password)
    if username == "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918" and password == "4813494d137e1631bba301d5acab6e7bb7aa74ce1185d456565ef51d737677b2":
        print('[APP] Root access granted')
        return True
    return False
