from flask import Flask, redirect, request, render_template

import auth, database, datainsert, math

app = Flask(__name__)
app.config["SECRET_KEY"] = 'bbb07774f2284417a9303684df7c1470'

lat = 45.50418693241608
long = -73.61360121950645


@app.route("/")
def returnMainWebsite():
    return render_template("frontPage.html")


@app.route("/login", methods=['GET', 'POST'])
def returnLogin():
    username = request.form.get('username')
    password = request.form.get('password')

    if request.method == 'GET':
        return render_template("login.html", warning={'message': ''})
    if request.method == 'POST':
        if username == None or password == None or username == "" or password == "":
            print('[APP] No Login Info')
            return render_template("login.html", warning={'message': 'Please provide a valid username and password.'})
        if auth.verifyRoot(username, password):
            return redirect("/admin_panel?token=")
            # return render_template("admin_panel/admin.html",warning={'token':tokenR})
        if auth.verifyUser(username, password):
            shelter_name = auth.getUser(username)
            return redirect("/user_panel?shelter=" + shelter_name)
        return render_template("login.html", warning={'message': 'Invalid username or password.'})


@app.route("/board", methods=['GET','POST'])
def board():
    shelters = database.get_shelters()
    distances = []
    for i in range(0, 4):
        distances.append(math.sqrt((float(shelters[i][3]) - lat) ** 2 + (float(shelters[i][4]) - long) ** 2))

    closest = shelters[distances.index(min(distances))]
    closest = shelters[1]

    return render_template('board.html', name=closest[1], image=closest[7], address=closest[2])


@app.route("/user_panel", methods=['GET', 'POST'])
def returnUserPanel():
    if request.method == 'GET':
        shelter_name = request.args.get('shelter')
        return render_template("user_panel/user.html", info={'shelter_name': shelter_name})
    if request.method == 'POST':
        shower = request.form.get('shower')
        bed = request.form.get('bed')
        food = request.form.get('food')
        therapist = request.form.get('therapist')


@app.route("/admin_panel", methods=['GET', 'POST'])
def returnAdminPanel():
    token = 2
    if request.method == 'GET':
        # if not auth.auth_required(tokenR):
        #     return render_template("login.html",warning={'message':''})
        print("admin panel get")
        return render_template("admin_panel/admin.html", info={'token': token})
    if request.method == 'POST':
        if request.form.get('goto') == "Add User":
            return render_template("admin_panel/add_user.html", warning={'message': '', 'token': token})
        if request.form.get('goto') == "Add Shelter":
            return redirect("/admin_panel/add_shelter")
        return "error"
    # return render_template("admin_panel/admin.html")


@app.route("/admin_panel/add_shelter", methods=['GET', 'POST'])
def returnAdminPanelAddShelter():
    if request.method == 'GET':
        return render_template("admin_panel/add_shelter.html")
    if request.method == 'POST':
        pass


@app.route("/admin_panel/add_user", methods=['GET', 'POST'])
def returnAdminPanelAddUser():
    if request.method == 'GET':
        return render_template("admin_panel/add_user.html", warning={'msg': ''})
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        email = request.form.get('email')
        shelter_name = request.form.get('shelter_name')
        print(username, password, confirm_password, email, shelter_name)

        if password == None or confirm_password == None or username == None or email == None or shelter_name == None:
            return render_template("admin_panel/add_user.html", warning={'msg': 'Please provide all information.'})

        if password == "" or confirm_password == "" or username == "" or email == "" or shelter_name == "":
            return render_template("admin_panel/add_user.html", warning={'msg': 'Please provide all information.'})

        if password != confirm_password:
            return render_template("admin_panel/add_user.html", warning={'msg': 'Password do no match.'})
        if database.create_user(str(username), str(password), str(email), str(shelter_name)):
            return render_template("admin_panel/add_user.html", warning={'msg': 'User account created'})


@app.route("/test", methods=['GET', 'POST'])
def testing():
    if request.method == 'GET':
        return render_template('test/test.html')
    if request.form.get('test') == "yes":
        return render_template("test/test_redirect.html")


@app.route("/testdone", methods=['GET', 'POST'])
def testdone():
    print("this ")
    return "done"


def Debug():
    database.create_database()
    datainsert.create_bs_shelters()
    datainsert.create_bs_shelters_info()
    print("db created")


def test_connection():
    with app.app_context():
        Debug()


# Debug()
test_connection()

if __name__ == "__main__":
    app.run(debug=True)
