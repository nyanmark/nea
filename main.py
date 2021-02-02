from mysql import connector
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = "D4Lgt4T6ALnDzJjRi9"
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///website.sql'
# mysql+mysqlconnector://website@nea:p97iiFq2@nea.mysql.database.azure.com/website
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(hours=12)

db = SQLAlchemy(app)
main_img = ['https://nyanmark.github.io/nea/img/choir.jpg',
            'https://nyanmark.github.io/nea/img/gallery.jpg']


class images(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    url = db.Column("url", db.String(100))

    def __init__(self, url):
        self.url = url


class users(db.Model):
    name = db.Column("name", db.String(100))
    email = db.Column("email", db.String(100), primary_key=True)
    password = db.Column("password", db.String(100))
    voice = db.Column("voice", db.String(10))
    is_admin = db.Column("is_admin", db.Boolean())
    num_events = db.Column("num_events", db.Integer)

    def __init__(self, name, email, password, voice, is_admin, num_events):
        self.name = name
        self.email = email
        self.password = password
        self.voice = voice
        self.is_admin = is_admin
        self.num_events = num_events


class eventsdb(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(100))
    description = db.Column("description", db.Text)
    # Using String instead of datetime due to SQlite3 Limitation
    date = db.Column("date", db.String(100))
    creator = db.Column("creator", db.String(100))
    img_url = db.Column("img_url", db.String(100))

    def __init__(self, title, description, date, creator, img_url):
        self.title = title
        self.description = description
        self.date = date
        self.creator = creator
        self.img_url = img_url


# noinspection PyBroadException
try:
    usr = users("admin", "admin@localhost", "admin", "soprano", True, True)
    db.session.add(usr)
    db.session.commit()
except:
    print(" * Admin user already exists")


admin_auth = False


def admin_check(email):
    db_query = users.query.filter_by(email=email).first()
    if db_query.is_admin:
        return True
    else:
        return False


@app.route("/")
def index():
    return render_template("index.html", main_url=main_img[0])


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
            usr = users(name, email, password, voice, None, None)
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
    return render_template("events.html", values=eventsdb.query.all())


@app.route("/gallery")
def gallery():
    return render_template("gallery.html", values=images.query.all(),
                           main_url=main_img[1])


@app.route("/admin/")
def admin():
    if "email" in session:
        email = session["email"]
        if admin_check(email):
            global admin_auth
            admin_auth = True
            return render_template("admin/admin.html")
        else:
            flash(f"You are not an Admin", "info")
            return redirect(url_for("members"))
    else:
        return redirect(url_for("login"))


@app.route("/admin/users", methods=["POST", "GET"])
def admin_users():
    if admin_auth:
        if request.method == "POST":
            email = request.form["u-mail"]
            found_user = users.query.filter_by(email=email).first()
            if found_user:
                if request.form['submit-button'] == 'delete':
                    db.session.delete(found_user)
                    db.session.commit()
                    flash(f"User Deleted", "info")
                elif request.form['submit-button'] == 'admin':
                    found_user.is_admin = True
                    db.session.commit()
                    flash(f"User Made Admin", "info")
            else:
                flash(f"No Such User", "info")
            return render_template("admin/users.html", values=users.query.all())
        else:
            return render_template("admin/users.html", values=users.query.all())
    else:
        return redirect(url_for("admin"))


@app.route("/admin/gallery", methods=["POST", "GET"])
def admin_gallery():
    if admin_auth:
        if request.method == "POST":
            img_id = request.form["i-id"]
            img_url = request.form["i-url"]
            if img_id == '999' or img_id == '998':
                if request.form['submit-button'] == 'add' or request.form['submit-button'] == 'delete':
                    flash(f"Cannot Add or Delete this Image", "info")
                else:
                    if img_id == '999':
                        main_img[0] = img_url
                    elif img_id == '998':
                        main_img[1] = img_url
            else:
                print("else")
                if request.form['submit-button'] == 'add':
                    img = images(img_url)
                    db.session.add(img)
                    db.session.commit()
                    flash(f"Image Added", "info")
                if request.form['submit-button'] == 'edit':
                    found_image = images.query.filter_by(_id=img_id).first()
                    if found_image:
                        found_image.url = img_url
                        db.session.commit()
                        flash(f"Image Updated", "info")
                    else:
                        flash(f"No Such Image", "info")
                if request.form['submit-button'] == 'delete':
                    found_image = images.query.filter_by(_id=img_id).first()
                    if found_image:
                        db.session.delete(found_image)
                        db.session.commit()
                        flash(f"Image Deleted", "info")
                    else:
                        flash(f"No Such Image", "info")
            return render_template("admin/gallery.html", values=images.query.all(),
                                   home_img_url=main_img[0], gallery_img_url=main_img[1])
        else:
            return render_template("admin/gallery.html", values=images.query.all(),
                                   home_img_url=main_img[0], gallery_img_url=main_img[1])
    else:
        return redirect(url_for("admin"))


@app.route("/admin/events", methods=["POST", "GET"])
def admin_events():
    if admin_auth:
        if request.method == "POST":
            eve_id = request.form["e-id"]
            eve_title = request.form["e-title"]
            eve_desc = request.form["e-desc"]
            eve_date = request.form["e-date"]
            eve_url = request.form["e-url"]
            email = session["email"]
            user = users.query.filter_by(email=email).first()
            if request.form['submit-button'] == 'add':
                eve = eventsdb(eve_title, eve_desc, eve_date, user.name, eve_url)
                db.session.add(eve)
                db.session.commit()
                event = eventsdb.query.filter_by(title=eve_title).first()
                event_file = open(f"eventsdb/{event._id}.txt", "w+")
                flash(f"Event Created", "info")
            elif request.form['submit-button'] == 'delete':
                found_event = eventsdb.query.filter_by(_id=eve_id).first()
                if found_event:
                    db.session.delete(found_event)
                    db.session.commit()
                    flash(f"Event Deleted", "info")
                else:
                    flash(f"No Such Event", "info")
            return render_template("admin/events.html", values=eventsdb.query.all())
        else:
            return render_template("admin/events.html", values=eventsdb.query.all())
    else:
        return redirect(url_for("admin"))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

