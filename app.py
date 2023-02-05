from flask import Flask, redirect,request, jsonify, make_response, render_template, session
from datetime import datetime, timedelta
from functools import wraps
import database
import auth
import datainsert
import shelter
import token_auth
import jwt
from auth import auth_required

app = Flask(__name__)
app.config["SECRET_KEY"] = 'a_scret_key'

def token_required(f):

    @wraps(f)
    def decorated(*args,**kwargs):
        token = request.args.get('token')
        print('token check: ' + str(token))
        if not token:
            return jsonify({'message':'Token missing'})
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            print(data)
        except Exception as e:
            print(e)
            return jsonify({'message':'Token is invalid'})
        return f(*args,**kwargs)
    return decorated

@app.route("/")
def returnMainWebsite():
    return render_template("frontPage.html")

    
@app.route("/login", methods=['GET','POST'])
def returnLogin():
    username = request.form.get('username')
    password = request.form.get('password')

    if request.method == 'GET':
        return render_template("login.html",warning={'message':''})
    if request.method == 'POST':
        if username == None or password == None or username=="" or password=="":
            print('[APP] No Login Info')
            return render_template("login.html", warning={'message':'Please provide a valid username and password.'})
        if auth.verifyRoot(username, password):
            token = jwt.encode({'user':username,'exp':datetime.utcnow()+timedelta(minutes=2)}, app.config['SECRET_KEY'])
            return redirect("/admin_panel?token="+token)
            # return render_template("admin_panel/admin.html",warning={'token':tokenR})
        if auth.verifyUser(username, password):
            # user_info = database.UserInfo(username) TODO
            tokenR = token_auth.create()
            token_auth.store(username, tokenR)
        # TODO    return render_template("user_panel/user.html",info={'username':username,'shelter':user_info[0]})        
            return render_template("user_panel/user.html")
        return render_template("login.html", warning={'message':'Invalid username or password.'})

@app.route("/board", methods=['GET','POST'])
def returnBoard():
    return render_template("board.html", shelter = {'name':'abc'})

@app.route("/admin_panel", methods=['GET','POST'])
@token_required
def returnAdminPanel():
    token = request.args.get('token')
    if request.method == 'GET':
        # if not auth.auth_required(tokenR):
        #     return render_template("login.html",warning={'message':''})
        return render_template("admin_panel/admin.html",warning={'token':token})
    if request.method == 'POST':
        print("form called")
        if request.form['add_user'] == "Add User":
            print("add user redirect")
            return render_template("admin_panel/add_user.html",warning={'message':'','token':token})
        if request.form['add_shelter'] == "Add Shelter":
            print("redirect to add shelter " + token)
            return redirect("/admin_panel/add_shelter?token="+token)
    # return render_template("admin_panel/admin.html")

@app.route("/admin_panel/add_shelter", methods=['GET','POST'])
@token_required
def returnAdminPanelAddShelter():
    token = request.args.get('token')
    print(token)
    if request.method == 'GET':
        return render_template("admin_panel/add_shelter.html",warning={'token':token})
    if request.method == 'POST':
        pass
        # cont = request.json
        # tokenr = cont['token']
        # if not auth.auth_required(tokenr):
        #     print("[APP] Invalid Token")
        #     return render_template("login.html",warning={'message':''})
        # print("redirect ")
        # return render_template("admin_panel/add_shelter.html")

@app.route("/test",methods=['GET','POST'])
def testing():
    if request.method == 'GET':
        return render_template('test/test.html')
    if request.form.get('test') == "yes":
        return render_template("test/test_redirect.html")

@app.route("/testdone",methods=['GET','POST'])
def testdone():
    print("this ")
    return "done"

def Debug():
    database.create_database()
    print("db created")

def test_connection():
    with app.app_context():
        Debug()

# Debug()
test_connection()

if __name__ == "__main__":
    app.run(debug=True)