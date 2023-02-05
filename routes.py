import requests
from database import get_shelters_info, connection
from auth import auth_required
from flask import Flask
app = Flask(__name__)
app.config["SECRET_KEY"] = 'bbb07774f2284417a9303684df7c1470'

@app.route("/get_shelter_info", methods=['GET'])
def returnBoard():
    tokenr= requests.args.get('token')
    if not auth_required(tokenr):
        connection()
        return get_shelters_info()

    