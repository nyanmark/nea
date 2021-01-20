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

home_img_url = 'https://nyanmark.github.io/nea/img/choir.jpg'
gallery_img_url = 'https://nyanmark.github.io/nea/img/image1.jpg'

db = SQLAlchemy(app)


class users(db.Model):
    name = db.Column("name", db.String(100))
    email = db.Column("email", db.String(100), primary_key=True)
    password = db.Column("password", db.String(100))
    voice = db.Column("voice", db.String(10))

    def __init__(self, name, email, password, voice):
        self.name = name
        self.email = email
        self.password = password
        self.voice = voice


class gallery(db.Model):
    _id = db.Column("_id", db.Integer(), primary_key=True)
    url = db.Column("url", db.String(200))

    def __init__(self, _id, url):
        self._id = _id
        self.url = url


@app.route("/")
def index():
    return render_template("index.html", main_url=home_img_url)


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        data = request.form
        email = data['u-mail']
        password = data['u-pass']
        name = data['u-name']
        voice = data['u-voice']
        session['email'] = email
        found_user = users.query.filter_by(email=email).first()
        if found_user:
            flash(f"Please Try again, Email already in use", "info")
            return render_template("register.html")
        else:
            usr = users(name, email, password, voice)
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
    var_num = gallery.query.all().count() + 1
    return render_template("gallery.html", values=gallery.query.all(), main_url=gallery_img_url, num=var_num)


@app.route("/admin")
def admin():
    return render_template("admin/admin.html")


@app.route("/admin/users")
def admin_users():
    return render_template("admin/users.html", values=users.query.all())


@app.route("/admin/gallery")
def admin_gallery():
    return render_template("admin/gallery.html", values=gallery.query.all())


@app.route("/admin/events")
def admin_events():
    return render_template("admin/events.html", values=events.query.all())



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
