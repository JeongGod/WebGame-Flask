from flask import Blueprint, json, render_template, url_for, request, session, jsonify
from werkzeug.utils import redirect
from db_connect import db

bp = Blueprint('main', __name__, url_prefix='/')
user_col = db.get_collection("user")


@bp.route("/")
def home():
    if session.get('login') is None:
        return render_template("index.html")
    else:
        return redirect(url_for("main.game"))

@bp.route("/login", methods=["GET", "POST"])
def login():
    if session.get('login') == None:
        if request.method == "GET":
            return render_template("login.html")
        else:
            userId = request.form['userId']
            userPw = request.form['userPw']
            result = user_col.find_one({ "userId" : userId })
            if result is not None:
                if result["userPw"] == userPw:
                    session['login'] = 1234
                    return jsonify({"result": "success"})
                else:
                    return jsonify({"result": "fail pw"})
            else:
                return jsonify({"result":"fail id"})
    # session이 존재하지 않는 경우
    else:
        return redirect(url_for("main.game"))
    

@bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        userId = request.form['userId']
        userPw = request.form['userPw']
        userName = request.form['userName']

        result = user_col.insert_one({
            "userId": userId,
            "userPw": userPw,
            "userName": userName,
        })
        return jsonify({"result" : "success"})

@bp.route("/game")
def game():
    return render_template("game.html")

@bp.route("/logout")
def logout():
    session['login'] = None
    return redirect(url_for('main.home'))