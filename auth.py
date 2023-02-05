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
    password = database.Hash(password)
    # TODO RICHARD
    # find if the username and passowrd are true
    # if true return True

def verifyRoot(username, password):
    password = func.Hash(password)
    if username == "admin" and password == "4813494d137e1631bba301d5acab6e7bb7aa74ce1185d456565ef51d737677b2":
        print('[APP] Root access granted')
        return True
    return False
