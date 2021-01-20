from mysql import connector
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "D4Lgt4T6ALnDzJjRi9"
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///website.sql'
# mysql+mysqlconnector://website@nea:p97iiFq2@nea.mysql.database.azure.com/website
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(hours=12)

db = SQLAlchemy(app)


class users(db.Model):
    name = db.Column("name", db.String(100))
    email = db.Column("email", db.String(100), primary_key=True)
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
        data = request.form
        email = data['u-mail']
        password = data['u-pass']
        name = data['u-name']
        session['email'] = email
        found_user = users.query.filter_by(email=email).first()
        if found_user:
            flash(f"Please Try again, Email already in use", "info")
            return render_template("register.html")
        else:
            usr = users(name, email, password)
            db.session.add(usr)
            db.session.commit()
            flash(f"Registration Successful {name}", "info")
            return redirect(url_for("members"))
    else:
        return render_template("register.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        # noinspection PyBroadException
        try:
            checkbox = request.form["u-save"]
            if checkbox == "on":
                session.permanent = True
        except:
            session.permanent = False
        password = request.form["u-pass"]
        email = request.form["u-mail"]
        db_query = users.query.filter_by(email=email).first()
        name = db_query.name
        if db_query.password == password:
            session["email"] = email
            flash(f"Login Successful {name}", "info")
        else:
            flash(f"Password Incorrect", "info")
        return redirect(url_for("members"))
    else:
        if "email" in session:
            flash(f"Already Logged In", "info")
            return redirect(url_for("members"))
        return render_template("login.html")


@app.route("/members", methods=["POST", "GET"])
def members():
    if "email" in session:
        return render_template("members.html")
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    if "email" in session:
        email = session["email"]
        flash(f"You have been logged out", "info")
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
    return render_template("admin.html", values=users.query.all())


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
