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
            shelter_name = auth.getUser(username)
            return redirect("/user_panel?shelter="+shelter_name)
        return render_template("login.html", warning={'message':'Invalid username or password.'})

@app.route("/board", methods=['GET','POST'])
def returnBoard():
    return render_template("board.html", shelter = {'name':'abc'})

@app.route("/user_panel", methods=['GET','POST'])
def returnUserPanel():
    if request.method == 'GET':
        shelter_name = request.args.get('shelter')
        return render_template("user_panel/user.html",info = {'shelter_name':shelter_name})
    if request.method == 'POST':
       shower = request.form.get('shower')
       bed = request.form.get('bed')
       food = request.form.get('food')
       therapist = request.form.get('therapist')

@app.route("/admin_panel", methods=['GET','POST'])
def returnAdminPanel():
    token = 2
    if request.method == 'GET':
        # if not auth.auth_required(tokenR):
        #     return render_template("login.html",warning={'message':''})
        print("admin panel get")
        return render_template("admin_panel/admin.html",info={'token':token})
    if request.method == 'POST':
        if request.form.get('goto') == "Add User":
            return render_template("admin_panel/add_user.html",warning={'message':'','token':token})
        if request.form.get('goto') == "Add Shelter":
            return redirect("/admin_panel/add_shelter")
        return "error"
    # return render_template("admin_panel/admin.html")

@app.route("/admin_panel/add_shelter", methods=['GET','POST'])
def returnAdminPanelAddShelter():

    if request.method == 'GET':
        return render_template("admin_panel/add_shelter.html")
    if request.method == 'POST':
        pass
        

@app.route("/admin_panel/add_user", methods=['GET','POST'])
def returnAdminPanelAddUser():
    
    if request.method == 'GET':
        return render_template("admin_panel/add_user.html", warning={'msg':''})
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        email = request.form.get('email')
        shelter_name = request.form.get('shelter_name')
        print(username, password, confirm_password, email,shelter_name)
        
        if password == None or confirm_password == None or username == None or email == None or shelter_name == None:
            return render_template("admin_panel/add_user.html",warning={'msg':'Please provide all information.'})

        if password == "" or confirm_password == "" or username == "" or email == "" or shelter_name == "":
            return render_template("admin_panel/add_user.html",warning={'msg':'Please provide all information.'})


        if password != confirm_password:
            return render_template("admin_panel/add_user.html",warning={'msg':'Password do no match.'})
        if database.create_user(str(username), str(password), str(email), str(shelter_name)):
            return render_template("admin_panel/add_user.html", warning={'msg':'User account created'})

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
<<<<<<< HEAD
=======
    print(database.get_shelters())
    datainsert.create_bs_shelters()
    datainsert.create_bs_shelters_info()
    shelter.closer_shelter()
>>>>>>> 5ab903c9c6d39e65b5eeb8596d07424c74bc1fb4

def test_connection():
    with app.app_context():
        Debug()

# Debug()
test_connection()

if __name__ == "__main__":
    app.run(debug=True)