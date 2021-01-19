from mysql import connector
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "D4Lgt4T6ALnDzJjRi9"
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql+mysqlconnector://website@nea:p97iiFq2@nea.mysql.database.azure.com/website'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(hours=12)

db = SQLAlchemy(app)


class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    email = db.Column("email", db.String(100))
    password = db.Column("password", db.String(100))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        email = request.form["email"]
        session["name"] = name
        session["password"] = password
        session["email"] = email
        flash(f"Registration Successful {name}", "info")
        return redirect(url_for("members"))
    else:
        if "user" in session:
            flash(f"You are already a user {name}", "info")
            return redirect(url_for("members"))
        return render_template("register.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        checkbox = request.form["checkbox"]
        if checkbox:
            session.permanent = True
        password = request.form["password"]
        email = request.form["email"]
        session["password"] = password
        session["email"] = email
        flash(f"Login Successful {name}", "info")
        return redirect(url_for("members"))
    else:
        if "user" in session:
            flash(f"Already Logged In", "info")
            return redirect(url_for("members"))
        return render_template("login.html")


@app.route("/members", methods=["POST", "GET"])
def members():
    email = None
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            flash("Email was saved!")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("members.html", user=user, email=email)
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"You have been logged out, {user}", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("index"))


@app.route("/events")
def events():
    return render_template("events.html")


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
