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


class main_images(db.Model):
    name = db.Column("name", db.String(100), primary_key=True)
    url = db.Column("url", db.String(100))

    def __init__(self, name, url):
        self.name = name
        self.url = url


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

    def __init__(self, name, email, password, voice, is_admin):
        self.name = name
        self.email = email
        self.password = password
        self.voice = voice
        self.is_admin = is_admin


@app.route("/")
def index():
    return render_template("index.html", main_url=main_images.query.filter_by(name="home").first())


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
            usr = users(name, email, password, voice, None)
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
    return render_template("gallery.html", values=images.query.all(),
                           main_url=main_images.query.filter_by(name="gallery").first())


@app.route("/admin")
def admin():
    return render_template("admin/admin.html")


@app.route("/admin/users", methods=["POST", "GET"])
def admin_users():
    if request.method == "POST":
        email = request.form["u-mail"]
        found_user = users.query.filter_by(email=email).first()
        if found_user:
            db.session.delete(found_user)
            db.session.commit()
            flash(f"User Deleted", "info")
        else:
            flash(f"No Such User", "info")
        return render_template("admin/users.html", values=users.query.all())
    else:
        return render_template("admin/users.html", values=users.query.all())


@app.route("/admin/gallery", methods=["POST", "GET"])
def admin_gallery():
    if request.method == "POST":
        img_id = request.form["i-id"]
        img_url = request.form["i-url"]
        if request.form['submit-button'] == 'add':
            if img_id == 999:
                found_image = main_images.query.filter_by(name="home").first()
                if found_image:
                    flash(f"Cannot Add an Image which exists", "info")
                else:
                    img = main_images("home", img_url)
                    db.session.add(img)
                    db.session.commit()
            elif img_id == 998:
                found_image = main_images.query.filter_by(name="gallery").first()
                if found_image:
                    flash(f"Cannot Add an Image which exists", "info")
                else:
                    img = main_images("gallery", img_url)
                    db.session.add(img)
                    db.session.commit()
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
            if img_id == 999 or 998:
                flash(f"Cannot Delete Image", "info")
            found_image = images.query.filter_by(_id=img_id).first()
            if found_image:
                db.session.delete(found_image)
                db.session.commit()
                flash(f"Image Deleted", "info")
            else:
                flash(f"No Such Image", "info")
        return render_template("admin/gallery.html", values=images.query.all(),
                               home_img_url=main_images.query.filter_by(name="home").first(),
                               gallery_img_url=main_images.query.filter_by(name="gallery").first())
    else:
        return render_template("admin/gallery.html", values=images.query.all(),
                               home_img_url=main_images.query.filter_by(name="home").first(),
                               gallery_img_url=main_images.query.filter_by(name="gallery").first())


@app.route("/admin/events")
def admin_events():
    return render_template("admin/events.html", values=events.query.all())


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
