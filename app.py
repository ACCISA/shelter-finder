from flask import Flask, request, jsonify, make_response, render_template, session
from datetime import datetime, timedelta
from functools import wraps
import database
app = Flask(__name__)
app.config["SECRET_KEY"] = 'bbb07774f2284417a9303684df7c1470'

@app.route("/")
def returnMainWebsite():
    return render_template("index.html")

@app.route("/login", methods=['GET','POST'])
def returnLogin():
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass

@app.route("/login", methods=['GET','POST'])
def returnPanel():
    pass

@app.route("/board", methods=['GET','POST'])
def returnBoard():
    
    return render_template("board.html", shelter = {'name':'abc'})

@app.route("/admin_panel", methods=['GET','POST'])
def returnAdminPanel():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_pasword = request.form.get('confirm_password')
        email = request.form.get('email')
        shelter_name = request.form.get('shelter_name')
        info = [username, password, confirm, email,shelter_name]

        print(username, password, confirm_pasword, email, shelter_name)
    return render_template("admin.html")



def Debug():
    database.create_database()
    print("db created")


Debug()

if __name__ == "__main__":
    app.run(debug=True)