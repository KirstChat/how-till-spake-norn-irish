import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Render Home Page


@app.route("/")
@app.route("/how-till-spake-norn-irish")
def home():
    return render_template('index.html')


# Render Sign Up Page

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    return render_template("sign-up.html")

# Render Dictionary Page


@app.route("/our-wee-guide")
def dictionary():
    dictionary = mongo.db.dictionary.find()
    return render_template("dictionary.html", dictionary=dictionary)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
