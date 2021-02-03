from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)  # Defines variable app as a Flask program
app.secret_key = "D4Lgt4T6ALnDzJjRi9"  # Web Sessions encryption key
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///website.sql'
# 'mysql+pymysql://VARS' - Optional MySQL connection string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(hours=12)
# ^ Defines how long a session lasts when keep me logged in is selected

db = SQLAlchemy(app)
main_img = ['https://nyanmark.github.io/nea/img/choir.jpg',
            'https://nyanmark.github.io/nea/img/gallery.jpg']
# Array to store the essential images for the web index and gallery index


class images(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    url = db.Column("url", db.String(100))

    def __init__(self, url):
        self.url = url

# Defines the images database with 2 columns one of which  (_id) column is auto created
# _id is used throughout my code instead if just id as the ide sometimes reports variable clash


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

# Defines the users database which slowly grew from just name, email and password to having every column
# needed for the website such as the users voice type whether they are admin and how many events they been in


class eventsdb(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(100))
    description = db.Column("description", db.Text)
    # Using String instead of datetime due to SQlite3 Limitation
    date = db.Column("date", db.String(100))
    creator = db.Column("creator", db.String(100))
    img_url = db.Column("img_url", db.String(100))
    finalized = db.Column("finalized", db.Boolean)

    def __init__(self, title, description, date, creator, img_url, finalized):
        self.title = title
        self.description = description
        self.date = date
        self.creator = creator
        self.img_url = img_url
        self.finalized = finalized


# noinspection PyBroadException
try:  # Tries to create the admin user
    usr = users("admin", "admin@localhost", "admin", "soprano", True, 0)
    db.session.add(usr)
    db.session.commit()
except:  # If failed code concludes admin already exists
    print(" * Admin user already exists")
# No inspection stops idea marking just except as an error


admin_auth = False  # By default admin is not logged in


def admin_check(email):
    db_query = users.query.filter_by(email=email).first()
    if db_query.is_admin:
        return True
    else:
        return False
    # Script to check whether a user is admin


@app.route("/")
def index():  # Defines the website index page
    return render_template("index.html", main_url=main_img[0])


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        data = request.form
        email = data['u-mail']
        password = data['u-pass']
        name = data['u-name']
        voice = data['u-voice']  # Pulls data from form and saves email into session
        session['email'] = email
        found_user = users.query.filter_by(email=email).first()
        if found_user:
            flash(f"Please Try again, Email already in use", "info")
            return render_template("register.html") # Checks if email is already used as that is the db primary key
        else:
            usr = users(name, email, password, voice, None, 0)
            db.session.add(usr)
            db.session.commit()
            flash(f"Registration Successful {name}", "info")
            return redirect(url_for("members"))
    else:
        return render_template("register.html")


@app.route("/login", methods=["POST", "GET"])  # Allows method of POST as well as GET
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
        if db_query.password == password:  # Queries database for password match
            session["email"] = email
            flash(f"Login Successful {name}", "info")
        else:
            flash(f"Password Incorrect", "info")
        return redirect(url_for("members"))
    else:
        if "email" in session:  # Checks if user is already logged into the site
            flash(f"Already Logged In", "info")
            return redirect(url_for("members"))
        return render_template("login.html")


@app.route("/members", methods=["POST", "GET"])
def members():
    if "email" in session:
        user_events = []
        user_finalized = []
        email = session["email"]
        for event in eventsdb.query.all():
            # Members page check how many events in the database and checks every appropriate file for users email
            with open(f'eventsdb/{event._id}.txt', 'r') as the_file:
                for line in the_file:
                    if email in line:
                        user_events.append(event.title+" happening "+event.date)
            the_file.close()
# Use of txt files was done as Flask_SQLAlchemy does not allow for dynamic DB creation which I had preferred to use
        for event in eventsdb.query.filter_by(finalized=True).all():
            with open(f'eventsdb/{event._id}_final.txt', 'r') as final_file:
                for line in final_file:
                    if email in line:
                        user_finalized.append(event.title + " happening " + event.date)
            final_file.close()
        return render_template("members.html", events=user_events, accepted=user_finalized)
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    if "email" in session:  # Removes user email from session and logs him out
        email = session["email"]
        flash(f"You have been logged out", "info")
    session.pop("email", None)
    return redirect(url_for("index"))


@app.route("/events", methods=["POST", "GET"])
def events():
    already_signed_up = False
    if request.method == "POST":  # Allows a user to sign up for the event
        email = session["email"]
        if "email" in session:
            db_query = users.query.filter_by(email=email).first()
            name = db_query.name
            event_id = request.form['submit-button']
            event_query = eventsdb.query.filter_by(_id=event_id).first()
            if not event_query.finalized:  # Checks if the event has not already been finalized by admin
                with open(f'eventsdb/{event_id}.txt', 'w+') as the_file:
                    for line in the_file:
                        if email in line:
                            already_signed_up = True
                    if not already_signed_up:
                        the_file.write(email+"\n") # Writes email to file on a new line
                        flash(f"Dear {name} you have successfully signed up for event", "info")
                    the_file.close()
            else:
                flash(f"Dear {name} signups for this event are locked", "info")
            return render_template("events.html", values=eventsdb.query.all())
        else:
            return redirect(url_for("login"))
    else:
        return render_template("events.html", values=eventsdb.query.all())


@app.route("/gallery")
def gallery():
    return render_template("gallery.html", values=images.query.all(),
                           main_url=main_img[1]) # Image gallery with the database and main image import


@app.route("/admin/")
def admin():
    if "email" in session:
        email = session["email"]  # Admin main page which does the check for admin login
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
            if found_user:  # When admin posts form website checks if the user email is found in the database
                if request.form['submit-button'] == 'delete':
                    db.session.delete(found_user)
                    db.session.commit()
                    flash(f"User Deleted", "info")
                elif request.form['submit-button'] == 'admin':  # Determines which of the buttons is pressed
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
    if admin_auth:  # Checks if user has been authed for admin area
        if request.method == "POST":
            img_id = request.form["i-id"]
            img_url = request.form["i-url"]
            if img_id == '999' or img_id == '998':
                # Checks if the user wants to change one of the reserved index images
                if request.form['submit-button'] == 'add' or request.form['submit-button'] == 'delete':
                    flash(f"Cannot Add or Delete this Image", "info")
                else:
                    if img_id == '999':
                        main_img[0] = img_url
                    elif img_id == '998':
                        main_img[1] = img_url
            else:
                # If user is not trying to change reserved image proceeds with this code
                if request.form['submit-button'] == 'add':
                    img = images(img_url)
                    db.session.add(img)  # Adds the image URL in database
                    db.session.commit()
                    flash(f"Image Added", "info")
                if request.form['submit-button'] == 'edit':
                    found_image = images.query.filter_by(_id=img_id).first()
                    if found_image:
                        found_image.url = img_url  # Updates image URL in database
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
    if admin_auth:  # The event management page, probably the hardest one
        if request.method == "POST":
            eve_id = request.form["e-id"]
            email = session["email"]
            user = users.query.filter_by(email=email).first()
            if request.form['submit-button'] == 'add':
                eve_title = request.form["e-title"]
                eve_desc = request.form["e-desc"]
                eve_date = request.form["e-date"]
                eve_url = request.form["e-url"]
                eve = eventsdb(eve_title, eve_desc, eve_date, user.name, eve_url, False)
                db.session.add(eve)  # Adds the event to database
                db.session.commit()
                event = eventsdb.query.filter_by(title=eve_title).first()
                open(f"eventsdb/{event._id}.txt", "w+")  # Creates a txt file specific to event
                flash(f"Event Created", "info")
            elif request.form['submit-button'] == 'delete':
                found_event = eventsdb.query.filter_by(_id=eve_id).first()
                if found_event:
                    os.remove(f"eventsdb/{found_event._id}.txt")
                    db.session.delete(found_event)
                    db.session.commit()
                    if found_event.finalized:  # Deletes event from database and if finalized the text file
                        os.remove(f"eventsdb/{found_event._id}_final.txt")
                    flash(f"Event Deleted", "info")
                else:
                    flash(f"No Such Event", "info")
            elif request.form['submit-button'] == 'finalize':
                eve_limit = request.form["e-limit"]
                user_emails = []  # Function for marking an event as finalized
                user_nums = []  # Creates too arrays one fro storing number of user events and the users emails
                found_event = eventsdb.query.filter_by(_id=eve_id).first()
                if not found_event.finalized:  # Checks if event has already been finalized
                    found_event.finalized = True
                    db.session.commit()
                    if len(user_emails) > int(eve_limit):
                        final_file = open(f'eventsdb/{found_event._id}_final.txt', 'w+')  # Creates event final file
                        with open(f'eventsdb/{found_event._id}.txt', 'r') as the_file:
                            for line in the_file:
                                line = line.rstrip()
                                user_query = users.query.filter_by(email=line).first()
                                num = user_query.num_events
                                user_nums = user_nums.append(num)
                                user_emails = user_emails.append(line)
                        the_file.close() # Sorts both the arrays together
                        user_nums, user_emails = zip(*sorted(zip(user_nums, user_emails)))
                        num_to_remove = len(user_emails) - eve_limit
                        for x in (0, num_to_remove):
                            del user_nums[-1]  # Removes users which are not needed from the array
                            del user_emails[-1]
                        for line in user_emails:
                            user_query = users.query.filter_by(email=line).first()
                            temp = user_query.num_events
                            temp = temp + 1  # Writes users to event final file
                            user_query.num_events = temp
                            db.session.commit()
                            final_file.write(line+"\n")
                        final_file.close()
                        flash(f"Event Finalized", "info")
                    else:
                        final_file = open(f'eventsdb/{found_event._id}_final.txt', 'w+')
                        with open(f'eventsdb/{found_event._id}.txt', 'r') as the_file:
                            for line in the_file:
                                line = line.rstrip()
                                user_query = users.query.filter_by(email=line).first()
                                temp = user_query.num_events
                                temp = temp + 1  # Performs same as above however when there is no overflow of users
                                user_query.num_events = temp
                                db.session.commit()
                                final_file.write(line+"\n")
                        the_file.close()
                        final_file.close()
                    flash(f"Event Finalized", "info")
                else:
                    flash(f"No Such Event or Event already Finalized", "info")
            return render_template("admin/events.html", values=eventsdb.query.all())
        else:
            return render_template("admin/events.html", values=eventsdb.query.all())
    else:
        return redirect(url_for("admin"))


if __name__ == '__main__':
    db.create_all()  # Creates all the databases on startup
    app.run(debug=True)  # Initialises the app in debug mode so I can see errors

