from flask import Flask, request, jsonify, make_response, render_template, session
from datetime import datetime, timedelta
from functools import wraps
import database, auth, math, datainsert, token_auth
from auth import auth_required
app = Flask(__name__)
app.config["SECRET_KEY"] = 'bbb07774f2284417a9303684df7c1470'

lat = 45.50418693241608
long = -73.61360121950645


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
            tokenR = token_auth.create()
            token_auth.store(username, tokenR)
            return render_template("admin_panel/admin.html")
        if auth.verifyUser(username, password):
            # user_info = database.UserInfo(username) TODO
            tokenR = token_auth.create()
            token_auth.store(username, tokenR)
        # TODO    return render_template("user_panel/user.html",info={'username':username,'shelter':user_info[0]})        
            return render_template("user_panel/user.html")
        return render_template("login.html", warning={'message':'Invalid username or password.'})

@app.route("/board", methods=['GET','POST'])
def returnBoard():
    shelters = database.get_shelters()
    distances = []
    for i in range(0, 4):
        distances.append(math.sqrt((float(shelters[i][3]) - lat) ** 2 + (float(shelters[i][4]) - long) ** 2))

    closest = shelters[distances.index(min(distances))]
    closest = shelters[3]

    return render_template('board.html', name=closest[1], image=closest[7], address=closest[2])

    # return shelters[distances.index(distances.min())]
    # return render_template("board.html", shelter = {'name':'abc'})

@app.route("/admin_panel", methods=['GET','POST'])
def returnAdminPanel():
    tokenR = request.args.get('token')
    if tokenR == None:
        return "Not Authed"
    if request.method == 'GET':
        if not auth.auth_required(tokenR):
            return "Not Authed"
        return render_template("admin_panel/admin.html")
    if request.method == 'POST':
        if request.form['add_user'] == "Add User":
            return render_template("admin_panel/add_user.html")
        # username = request.form.get('username')
        # password = request.form.get('password')
        # confirm_pasword = request.form.get('confirm_password')
        # email = request.form.get('email')
        # shelter_name = request.form.get('shelter_name')
        # info = [username, password, confirm_password, email,shelter_name]

        # print(username, password, confirm_pasword, email, shelter_name)
    return render_template("admin_panel/admin.html")

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
    print(database.get_shelters())
    datainsert.create_bs_shelters()
    datainsert.create_bs_shelters_info()

def test_connection():
    with app.app_context():
        Debug()

# Debug()
test_connection()

if __name__ == "__main__":
    app.run(debug=True)