from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from flask_jwt_extended import create_access_token, jwt_required
from .models import add_user, add_transaction, get_summary
from . import mongo

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/transaction", methods=["GET", "POST"])
@jwt_required()
def transaction():
    if request.method == "POST":
        data = {
            "type": request.form["type"],
            "amount": float(request.form["amount"]),
            "category": request.form["category"],
            "date": request.form["date"]
        }
        add_transaction(data)
        return redirect(url_for("main.summary"))
    return render_template("transaction.html")

@main.route("/summary")
@jwt_required()
def summary():
    summary_data = get_summary()
    return render_template("summary.html", summary=summary_data)
