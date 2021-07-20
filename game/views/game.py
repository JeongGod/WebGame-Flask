from flask import Blueprint, render_template, url_for

bp = Blueprint('game', __name__, url_prefix='/game')

@bp.route("/")
def home():
    return render_template("game.html")