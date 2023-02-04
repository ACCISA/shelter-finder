from flask import Flask, request, jsonify, make_response, render_template, session
from datetime import datetime, timedelta
from functools import wraps


app = Flask(__namme__)
app.config["SECRET_KEY"] = 'bbb07774f2284417a9303684df7c1470'

@app.route("/")
def returnMainWebsite():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)