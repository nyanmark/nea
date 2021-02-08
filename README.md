<header>
  <h1 align="center">COMPUTER SCIENCE NON EXAM ASSESSMENT <br> CHOIR WEBSITE</h1>
</header>
<br>
<p align="center">
  <img src="https://nyanmark.github.io/nea/img/readme.png" width="200" height="200">
</p>

## Contents

#### [Analysis](#Analysis-1)

#### [Documented Design](#Documented-Design-1)

#### [Technical Solution](#Technical-Solution-1)

#### [Testing](#Testing-1)

#### [Evaluation](#Evaluation-1)

## Analysis

#### Problem Identification

Currently there is no efficient way to manage the local choir, post events, get members to commit to an event and accept the members for a choir event. This therefore has created a problem which needs a solution. A possible solution would most likely involve computers, considering how digitised the world has become. However, some management systems can be very expensive or too complex for less computer educated users. This is because web developers usually end up expensive and unless creating your own custom system, using something created for another purpose even though similar can result rather complex for many users.

Therefore a system for a solution to this problem would have to be on the web, allowing all members to access it effortlessly. It must be easy to use and navigate without requiring a steep learning curve excluding the administrator who for any computer system would have to get aquainted with the in and out working of it. Finally a solution would have to be cheap to run in the long term. Meaning the website has to be light weight allowing it to be ran cheaply on the web.

#### Clients

The possible clients for such system, would be those who run a choir or are very pationate members of their choir wanting to increase efficiency and productivity of their choir nethertheless the majority users for such software would range from experienced computer veterans to very new computer users regarding back to the point that it has to be simple to understand and to use.

My client for this software is part of this demoghraphic he is a passionate member of his choir with very good computer knowledge. Making this the perfect software for him and allowing himself and I to discuss a feasible solution accounting for all the features and options a choir may want and need. The points given to me by my client will help me code an efficient and powerful website for any choir. 

#### Investigating the Problem

I have went to ask many of my friends and peers about their experiences in a choir, I wanted to know to what extent was my problem a real world issue and how much possible intrest I could find for a software of this sort that can help therefore I had chosen to send our a questionare and collect some responses.

<p align="center">
  <img src="https://nyanmark.github.io/nea/img/chrome_gxiKSuvoe2.png" width="550">
</p>

Above is an image of a form which I had sent out to many of my friends and choir members I know this has allowed me to find out more about my problem, I have compiles the responses I have recieved to get a clear understanding of the issue. I have also added a text box at the bottom of the form allowing some responders to voice extra concerns and suggestions for myself so I could scope the problem further. This had lead me to the sysnopsis that there is indeed an issue with the way many choirs notify and inform members of current and future events.

Now I can show the compiled results for my questionare, as shown the majority of responses faced that there was some concern with the organisation and the aviailability of event information from their choir. Others have also raised concerns about a lack of images of their choir showcasing what type of members there are i.e. young members, old members, male members or female members which I also believe would be a great addition to the choir website as it could be used to encourage others to join the choir once they see their peers in it and with an easy registration feature it should be easier then ever for members to enlist.

<p align="center">
  <img src="https://nyanmark.github.io/nea/img/chrome_ddyQ79nG54.png" width="550">
</p>

This chart shows that a majority of choir members found it hard to find out what events were going on in their choir making this one of the issues that my technical solutions will solve by proving an easy to access web page listing all events the are currently on. Additionally many found it hard to sign up for an event as shown by the chart below.

<p align="center">
  <img src="https://nyanmark.github.io/nea/img/chrome_wBn2rra5Er.png" width="550">
</p>

Finally the last chart is about how easy was it for members to find out what event's they were accepted to be part of after signing up which showed that many users had trouble knowing wether or not they had been accepted to be in an event. I am hoping to solve this through my technical solution by displaying this info in an easy format for the users.

<p align="center">
  <img src="https://nyanmark.github.io/nea/img/chrome_kvI6panV2B.png" width="550">
</p>

#### Why is this problem ideal for a computer

I believe this problem is ideal for a computer to solve because computers are devices which are inherrently part of the internet and provide users access to the internet *an electronic communications network that connects computer networks and organizational computer facilities around the world*. This communications network gives users access to the world wide web with the help of a web browser where users can reach many resources on the internet through the use of *hyper text transfer protocol* a application layer protocol also reffered to as an L7 protocol on the OSI model which runs on top of the TCP transport layer protocol also known as an L4 protocol on the OSI model. This would allow users from anywhere in the world with the help of a laptop or a phone to access the website. 

Therefore, this would solve the issue of information being hard to reach as anyone with an internet connected device would be able to see what events are going on, what events they are going to be part of and sign up for those events they're interested in. Where other means of communication would not be able to acheive the same or would be inferior such as emails being able to notiy people and being commonly used today. They do not have the advantage of the user being able to check at any time of day and new users to easily sign up to the mailing list.

#### Requirements

My client and I had to come up with a solution to this problem. To me the ideal seemed a website as it would provide access to anyone from anywhere to see what events are going on and sign up for them, this would also give myself and my client an opportunity to notify members which events they are in. Overall this allowed my client and I to come up witha  sert of requirements listed below.

The requirements I had agreed on with my client would include:

    • A membership system
    • Tracking voice type (Soprano – Bass)
    • Tracking events
    • Storing choir membership
    • Event sign ups
    • Web page with secure login

#### Objectives

This task would require a smart approach to reach all the requirements me and my client have discussed leading to some objectives I had come up with listed below. Furthermore considerations have to be taken on how to approach this issue of making an easily accessible website for all the choir member such as needing a domain for the website and a web server.

Listed Objectives for the Technical Solution:

    • A system which people with a lack of technical knowledge can use (e)
    • Security users must log in to use the website (e)
    • A intuative admin panel (e)
    • Page listing all the events with a sign up (e)
    • Events entered and accepted displayed in member page (e)
    • Image gallery to show off past events
    • Options for admin to set user limits for events
    • Website hosted on the web accessible to anyone
    • Cheap to run in the long run 
    • Databases for fast access and indexing (e)
    
I had to decided to split these objectives into essential and possible to set proper priorities for my project. Those which I deemed essential have been marked with an (e) next to them therefore I can prioritise them when designing my project. Additionally I had to figure out ways to test my code for these requirement and objectives listed above which will be noted in the [Testing](#Testing-1) section of my write up.

## Documented Design

Such requirements and objective have lead me to chose python as my program of choice using the flask library built into python allowing it to interface with html web pages. I have chosen python because I prefer it to and it provides me greater flexibility whilst setting up a system utilising a database to drive a web front end application. Furthermore it can easily integrate notification systems such as SMTP email sending and web hooks. I will be using uWSGI allowing python to interface with an Nginx web server allowing the web pages to be accessible from the internet on the choir website.

The database will be an integral part of my project as it would have to store all the members, logins and details for the system to function properly this would mean I have to employ proper table structure to make my database efficient. I have decided that there would be a table within the database for the members including their name, surname, email, password, voice type and quantity of events participated. Furthermore there will be a table for the events including the date, amount of slots and the location with another table for the event entries featuring the choir members who have entered having their first and last name, email and voice type. This will allow the choir master to see which people are in an event and how many of each voice type allowing him/her to alter the members as needed. Additionally the quantity of events participated which will be increased every time a user has been approved for an event and a notification has been sent out will be integral for the system in choosing users when there have been too many entries for an event allowing it to select those with the least performances.

For the web front end there will be simple html web pages with all the appropriate tabs. The web page list I had decided on is having an index home page, a registration page, a log in page, a personal info page allowing users to edit their email or password, an events page and an administrator page for the choir leader allowing them to edit user details, approve event sign ups, alter and overwrite members entered to an event and delete users. Furthermore the administration page will include SMTP setting for email sending allowing my customer to alter the email domain for his requirements.

The python back end will be central for the system to work as it would be running the link between the website and database and providing function for user notifications. This whole system would then interface with an Nginx allowing it to run a proper web site in conjunction with the python program. This may be considered unneccesary as flask runs a web server for you however to get much of the common features we rely on today such as ssl, sni, speed and versatility it would be ideal to run it using a web server such as Nginx or Apache2.

As mentioned previously I had chosen python for my website backend rather than common options such as PHP. Therefore I could simply split my code into 3 defined parts. The web, database and backend logic. The backend logic is the python part however the web part is done through the use of HTML and CSS finally the database part is done within python using Flask's (A python web driver alternative to django) SQLAlchemy package which allow easy interfacting between Flask and any database engine of choice, for testing I will be using sqlite3 database as it allows easy deletion and near instant access times however, I have added options into my code for using a MySQL database which providers better speed for larger deployment and has options such as high availability through clusters.

**Web**

I was thinking what the ideal look would be for the web front. It needed to be simple however eye catching to get users attention to the website. Therefore I had to create a mock up sesign sketching out what my desired look would be. The Navbar and Footer were very important for me as they would be persistent across the whole website defined in the base template. This is the original design I came up with below.

<p align="center">
  <img src="https://nyanmark.github.io/nea/img/design_jqMulpKc4r.png" width="550">
</p>

Another question which I had is how to make the website fast response and good-looking. I had to do this with the consideration of the tight time constraints I had for this project. Therefore, when I found out there was a web framework known as bootstrap which would take away most of the work of writing CSS and JS allowing me to focus on the python end of the project I had decided to use it. You can find the source located [Here](https://github.com/twbs/bootstrap) on GitHub.

This means that whilst I focused on structuring the website markup bulk of the work  was taken off my hands. Additionally, using Flask has allowed me to create templates for a footer, header and navibar for the Member and Admin areas meaning each pages individual file only contained content unique to it. Using python has also allowed me to set variables and logic within the HTML code making me think of the most efficient decisions wether to do logic within python and then import the variable or do the code within the HTML. I have chosen to place the most important URL's within the header whilst keeping other essential however lesser important URL's in the footer. 

My decision to use bootstrap was partially inspired by many huge websites using it [including](https://expo.getbootstrap.com/) and many others such as the Target and NBA website. What striked me more is that nearly 1/4 of the top 1 million websites are made with the help of bootstrap. Additionally through my intended usage of bootrap it lead me to explore why was it so prevalent in the top websites today. This lead me to come up with a few reasons listed below:

- Easy to implement, You just have to input a few links at the <head> section and bottom of the <body> section in your code.
- Well [documented](https://getbootstrap.com/), There is vast documentation allowing you to find out what classes lead to what effect and structure.
- Versatile, as shown by many sites in the bootstrap expo linked above it. Allot of the work is still with the creator to design it and make it look good.
- Fast loading, Soon as bootstrap is so widely used. It is cached by many CDN's on the web such as cloudflare making it load very fast.
- Mobile support, Importantly bootstrap is has mobile support allowing you to get very high page loading scores on mobile without a seperate mobile version.
  
The great availiability of bootstrap [documentation](https://getbootstrap.com/docs/4.5/getting-started/introduction/), allowed me to style my website to my ideal needs. Additionally the availability of many premade objects for bootstrap allowed me to use this as a [base](https://github.com/bootstrapstudio/clean-sky-template/blob/master/template/index.html) for my website. This allowed me to have good and functional styling for the normal web pages where I could pick and chose wether to import python variables from my code and adjust them as I wanted.

**Database**

My website database consists of 3 tables. The initial database for the website I designed was only the users table to hold the websites members. That consisted of essential collumns such as the email, username and password however I had expanded my desin to do more and more.

| Users Table | Data Type |
| -------------  | ------------- |
| Name | String  |
| Email | String, PrimaryKey  |
| Password | String  |
| Voice | String  |
| is_admin | Boolean  |
| num_events | Intiger  |

These were my desired data types for the users collumn they will allow me to create a secured admin area and record the number of events the user has participated in therefore when the program is chosing the final user it knows how to do so by ordering them from most to least events participated in. Another database my project had is a simple database for the image gallery.

| Gallery Table | Data Type |
| -------------  | ------------- |
| ID | Int, PrimaryKey  |
| URL | String  |

This was a very basic table to allow the storage of images and their respective ids for purposes such as editing and allowing the image carousel to work properly by giving it the number of images through the use of the ID + 1, the reason a +1 is added to the id is because of a persistent base image for the gallery and the home page which will be loaded from a variable in my code for the sake of simplicity.

| Events Table | Data Type |
| -------------  | ------------- |
| ID | Int, PrimaryKey  |
| Title | String |
| Description | String  |
| Date | String (limitation of SQLite3, DATE can be used with MySQL) |
| Creator | String  |
| IMG_URL | String  |
| Finalized | Boolean  |

Finally the most important and arguably most complicated table is the events table for the website this had to consist of many features again just like the gallery the ID is used to order the table properly and efficients on the events page. The date allows the adming to show case when the event is occuring and when the choir members should prepare for it (in evaluation, I believe it would have been good to add a location and time to the events database) additionally, there is the creator collumn to identify what choir Admin has posted the event and the Image URL for the event. Last but not least the finalized feature denotes whether the event has been finalized by the choir leader meaning no more members can join the event and all those who are going to be in it have been written to file.

Additionally my website has multiple or possibly infinate no SQL databases, I would have prefered to make them SQL however, Flask SQLAlchemy has a limitation of not allowing you to create tables dynamically with variable names. This meant that I had to find another way of storing user data for a created event as originally I had planned to create a dedicated table for each event. However, the solution I have invisioned is to create a text file for each event identified by the event id in the format eventid.txt, This would make the file easy to locate and would put even more importance of using having the ID for the event collumn apart from it being the only collumn which can realistically be used as a primary key. 

Another feature I had to build on top of this is when a choir Admin decides to finalize an event. I have planned it would create an additional text file denoted eventid_final.txt, This text file would have the emails of all users confirmed to be in the event. Meaning the choir manager can easily get this file of the web server. Moreover, having a seperate file for event and finalized allowed me to sort the users in the event files by the num_events they had preformed in creating a relation ship between the two databases. Once sorted the users with the most performances would be deleted until the number is down to the choir Admin's desire. Then those users would be entered into the final txt. This way the Admin can see the amount of users whom have entered. Those who didn't make it into the final file and adjust his plans for the future accordingly.

**Backend**

Python Flask backend. This will be the most complicated and feature rich part of the code. As a strarted I will have to figure out what imports I would like for my project. I had decided on using Flask for my web and FlaskSQLAlchemy for the datbases attached to the website. Therefore I will be importing those two packages. Additionally for managing dates withing python I will have to import datetime from timedelta this is to add support for the time datatype when using MySQL with the website. Finally I would have to import os which allows python to interface with the operating system. This is the feature which allows me to open, edit and create text files for each event that is going on. Overall, this project is light on imports however, it is still light weight and does not over do by importing every package in the python library.

Another thing I have to consider is definining my app. The app is the Flask website, additionally I have to define the database connection string for SQLite for development and MySQL for the actual website. Other features I would have to include is the encryption key for the web sessions to keep the secure and the permanent session life time, to tell my site how long to hold these sessions in cache. Another feature that would need to be defined here is the admin user creation as without a default adming user "admin@localhost" pass "admin" there would be no way for the intended user of the website to log in manage events, the gallery and other users therefore this is a very important and essential feature. Also there would have to be an implemented check wether an admin user already excists i.e. has the database already been populated. So there are no errors caused in the code.

Just before defining the app.routes or the web pages for Flask. I would have to create the databases aformentioned previously. The web pages I had planned fro my website. Is having an index, register, login, gallery, events and members page in addition to this there would have to be an admin area to manage all of those comprised of the index for admin sub directory, the manage events, manage users and manage gallery pages.

One of the most challenging aspecs of my code would be the admin events. Therefore, I had to plan out procedually how it would work. The chart below is the structure I had invisioned it to be:

- User Accesses Page
  - Is user logged in ?
    - Yes
      - Is User Admin ?
        - Yes
          - Allow user through
            -Is request Get or Post
              - Get
                - Just display web page
              - Post
                - Pull variables from the form
                - What button is user using for post
                  - Add Event
                    - Create a database entry and pull the ID to create a txt file
                  - Edit Event
                    - Locate database entry and edit if excist or put error if not
                  - Delete Event
                    - Delete database entry for such id
                  - Finalize Event (logic)
                    - Alter database table and mark finalised
                    - Create an ID_final txt file
                      - Is users in eventid.txt less than event limit from form
                        - Yes
                          - Move users to eventid_final.txt and finalize event
                        - No
                          - Put users in temporary array
                          - Sort by number of events participated
                          - Delete users with most events until len array = event limit
                          - Move users to eventid_final.txt
                          - Finalize event.
        - No
          - Send to members Area
    - No
      - Send to Log in

I believe when converted to python there may be short comings and additions to this design I would have to make however, I believe that overall this will be a good template to code the logic for the python back end for event creation, editing, deletion and finalization. Additionally to this I had to design the login for the gallery allowing the admin user to add, remove and edit images. This would still be complicated to code at a whim therefore I had to desing some sort of structure for this as well. The design for the admin gallery page is shown below:


- User Accesses Page
  - Is user logged in ?
    - Yes
      - Is User Admin ?
        - Yes
          -Is request Get or Post
            - Get
              - Just display web page
            - Post
              - Pull variables from the form
              - Is image ID reserved image such as index image or gallery image ?
                - Yes
                  - What button is user using for post ?
                    - Add or Delete
                      - Tell user impossible
                    - Edit
                      - Update image URL
                - No
                  - What button is user using for post ?
                      - Add
                        - Create new database entry using variables input from user
                      - Edit
                        - Is image ID in database
                          - No
                            - Image not found try again
                          - Yes
                            - Update database record
                      - Delete
                        - Is image ID in database
                          - No
                            - Image not found try again
                          - Yes
                            - Remove database record
        - No
          - Send to members Area
    - No
      - Send to Log in

In addition to those admin pages I had to consider how I would go around the other pages and what variables would be used to furfil my code. For example how would user registration and login work. I believed the concept for registration would be similar to the concept of adding an event or an image to the gallery in this case a new entry would be added to the database with the appropriate users, with the email being used as the primary key as I would like to keep user emails unique. In addition to this I would have to check whether the email already excists not to creat errors. I would do this through querying the database for said registration email and then allowing or not allowing the user to register his account based on that.

Finally, for login I would have to add a function to query the database and check wether a user excists after that the person loggin in will either be told that a user with that email does not excist or the python code would proceed to check wether there is a match between the users email and password through querying the database. this it would report wether password is wrong otherwise the user will log in and be redirected to the members page. One down side to this approach is that its a security concern reporting wether a user under a certain email excists however, I think that for the usability this will be ideal as users with little technical expeirence may not have password managers and therefore may forget whether they had signed up.

## Technical Solution 

If you would like to look at the files rather than screenshots they are located at [GitHub](https://github.com/nyanmark/nea). Files to note for my project "main.py" and the contents of the "templates" folder. Everything else may be ignored.

**Main Py**
``` python
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
```

**Base HTML**
```html
<html lang="html">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
    <!-- Fixes an IOS Bug -->
    <title>{ block title }{ endblock }</title> <!-- Dynamic Title -->
    <!-- Had to redact % from variable as github had issues with it on the readme -->
    <link rel="stylesheet" href="{ url_for('static', filename='bootstrap.min.css')}">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/simple-line-icons/2.4.1/css/simple-line-icons.min.css">
    <link rel="shortcut icon" href="{ url_for('static', filename='singer.ico')}"/>
</head>

<body>
    <nav class="navbar navbar-light navbar-expand-lg fixed-top bg-light clean-navbar" style="color: var(--blue);background: var(--gray);">
        <div class="container"><a class="navbar-brand logo" href="./">Cambridge Choir</a><button data-toggle="collapse" class="navbar-toggler" data-target="#navcol-1"><span class="sr-only">Toggle navigation</span><span class="navbar-toggler-icon"></span></button>
            <div class="collapse navbar-collapse" id="navcol-1">
                <ul class="nav navbar-nav ml-auto"> <!-- Navbar -->
                    <li class="nav-item"><a class="nav-link active" href="./">Home</a></li>
                    <li class="nav-item"><a class="nav-link" href="./events">Events</a></li>
                    <li class="nav-item"><a class="nav-link" href="./gallery">gallery</a></li>
                    <li class="nav-item"><a class="nav-link" href="./login">login</a></li>
                </ul>
            </div>
        </div>
    </nav>
    { block content }{ endblock } <!-- Variable to input class main -->
    <!-- Had to redact % from variable as github had issues with it on the readme -->
    <footer class="page-footer dark"> <!-- Footer -->
        <div class="container">
            <div class="row">
                <div class="col-sm-3">
                    <h5>Get started</h5>
                    <ul>
                        <li><a href="./">Home</a></li>
                        <li><a href="./register">Sign up</a></li>
                    </ul>
                </div>
                <div class="col-sm-3">
                    <h5>About us</h5>
                    <ul>
                        <li><a href="./gallery">Image Gallery</a></li>
                        <li><a href="mailto:choir@example.com">Contact us</a></li>
                    </ul>
                </div>
                <div class="col-sm-3">
                    <h5>Members</h5>
                    <ul>
                        <li><a href="./members">Member Area</a></li>
                        <li><a href="./logout">Sign out</a></li>
                    </ul>
                </div>
                <div class="col-sm-3">
                    <h5>Legal</h5>
                    <ul>
                        <li><a href="./404">Terms of Service</a></li>
                        <li></li>
                        <li><a href="./404">Privacy Policy</a></li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="footer-copyright">
            <p>© 2021 Cambridge Choir</p>
        </div>
    </footer>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.5.3/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

**Members HTML**
``` html
{ extends "base.html" } <!-- Had to redact % from variable as github had issues with it on the readme -->
{ block title }Member Area{ endblock } <!-- Had to redact % from variable as github had issues with it on the readme -->
{ block content } <!-- Had to redact % from variable as github had issues with it on the readme -->
<main class="page">
    <section class="clean-block dark">
        <div class="container">
            <div class="block-heading">
                <h2 class="text-info">Members Area</h2>
                <h5 class="text-body">
                    { with messages = get_flashed_messages() }
                        { if messages }
                            { for msg in messages }
                                {{msg}} <!-- Shows flashed test from python code --> 
                            { endfor }
                        { endif }
                    { endwith } <!-- Had to redact % from variable as github had issues with it on the readme -->
                </h5>
            </div>
            <table class="table">
                <thead>
                    <tr>
                      <th>Event Entries</th>
                    </tr>
                </thead>
                <tbody>
                    { for item in events } <!-- for loop for all the items submitted from python code -->
                    <!-- Had to redact % from variable as github had issues with it on the readme -->
                    <tr>
                      <th>{{item}}</th>
                    </tr>
                    { endfor }
                </tbody>
            </table>
            <table class="table">
                <thead>
                    <tr>
                      <th>Events Accepted</th>
                    </tr>
                </thead>
                <tbody>
                    { for item in accepted } <!-- Had to redact % from variable as github had issues with it on the readme -->
                    <tr>
                      <th>{{item}}</th>
                    </tr>
                    { endfor }
                </tbody>
            </table>
        </div>
    </section>
</main>
{ endblock }
```

Other pages are individually located in the "templates" folder on [GitHub](https://github.com/nyanmark/nea). Due to the markdown errors with githubs interpretation of the code I believe that would be the most effective way of examinining the website HTML markup.

**Sitemap**

``` xml
<urlset xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
<!--
 created with Free Online Sitemap Generator www.xml-sitemaps.com 
-->
<url>
<loc>https://mlweb.me/</loc>
<lastmod>2021-02-07T17:44:49+00:00</lastmod>
<priority>1.00</priority>
</url>
<url>
<loc>https://mlweb.me/events</loc>
<lastmod>2021-02-07T17:44:49+00:00</lastmod>
<priority>0.80</priority>
</url>
<url>
<loc>https://mlweb.me/gallery</loc>
<lastmod>2021-02-07T17:44:49+00:00</lastmod>
<priority>0.80</priority>
</url>
<url>
<loc>https://mlweb.me/login</loc>
<lastmod>2021-02-07T17:44:49+00:00</lastmod>
<priority>0.80</priority>
</url>
<url>
<loc>https://mlweb.me/register</loc>
<lastmod>2021-02-07T17:44:49+00:00</lastmod>
<priority>0.80</priority>
</url>
```

Pages in the /admin directory are hidden and not hyperlinked therefore are not shown in the sitemap. These pages include:

- /admin
- /admin/events
- /admin/users
- /admin/gallery

**Uploading To Web Server**

Below are some image of the process taken for the website to become accessible to anyone on the World Wide Web,

<p align="center">
  <img src="https://nyanmark.github.io/nea/img/MobaXterm_3YDnmRjfWZ.png" width="550">
</p>

First I started off with a fresh Ubuntu 20.04 VPS. It is very cheap and therefore has little power (512MB RAM) leading me to believe the requirements for good stability for my website are a VPS with 2-4 GB Ram and 1 Dedicated CPU core which can be gotten for anywhere from $10-20.

<p align="center">
  <img src="https://nyanmark.github.io/nea/img/MobaXterm_bseHaWxynt.png" width="550">
</p>

After uploading the webfiles I create a virtual environment for the python web app just like there is in my ide. This allowed me to install pip modules just in the virtual environment without having to install them globally on the system. I have omitted the "apt install" commands from these images for simplicity reasons.

<p align="center">
  <img src="https://nyanmark.github.io/nea/img/MobaXterm_BllGd3URV2.png" width="550">
</p>

Once that was done. I created a MySQL database for my website and instructed my program to use it by altering the connection string. This is to provide the site with more datatypes such as the TIME datatype. More flexibility and scalability given to it by MySQL. The downside to this is MySQL uses ram making it have a big burden if the server is very weak. However, the typical ram usage is around 250 MB which is nothing in the grand scheme of things.

<p align="center">
  <img src="https://nyanmark.github.io/nea/img/MobaXterm_DROSh4lJtr.png" width="550">
</p>

Now I was ready to test my Flask app.

<p align="center">
  <img src="https://nyanmark.github.io/nea/img/MobaXterm_R1PIwK6D8z.png" width="550">
</p>

The final step was to create a service for the uWSGI module which allows interfacing between Flask and NGINX a web server. Once this was done the uWSGI module created a sock within the program folder which allows nginx to interface with it. PHP also uses a similar technique of interfacing with nginx by using a .sock file with similar syntax as my website.conf below. PHP is a scripting language for web development and is frequently used as an alternative to python for web apps.

<p align="center">
  <img src="https://nyanmark.github.io/nea/img/MobaXterm_UhXoYLL2nk.png" width="550">
</p>

Nginx uWSGI module ran by website.service is now functional.

<p align="center">
  <img src="https://nyanmark.github.io/nea/img/MobaXterm_K1IS7qlboE.png" width="550">
</p>

Nginx Web Server configuration.

<p align="center">
  <img src="https://nyanmark.github.io/nea/img/MobaXterm_UhXoYLL2nk.png" width="550">
</p>

Now my website is up and accessible to everyone on the internet. However, there was one issue, a lack of SSL. This is bad as passwords would be submitted over clear text on the internet.

<p align="center">
  <img src="https://nyanmark.github.io/nea/img/firefox_Qa6OCItrDx.png" width="550">
</p>

Below is me installing letsencrypt on my server which allows me to get Free SSL certificates. Providing secure and encrypted communication for users on the internet between my site.

<p align="center">
  <img src="https://nyanmark.github.io/nea/img/MobaXterm_dSamoWP8QW.png" width="550">
</p>

Now when you load it in your browser it has the lock showing that data is now being transmitted over hyper text transfer protocol secure.

<p align="center">
  <img src="https://nyanmark.github.io/nea/img/firefox_reE7HgQnt0.png" width="550">
</p>


## Testing

- [x] A system which people with a lack of technical knowledge can use. Throughout my testing and my questionnaire regarding my finished product I believe many would find it easy to use. To verify this further I had my grand mother try using and accessing the site. With little technical knowledge she was abe to get around it. I believe I own this success to the very simple and clean design where the most essential buttoms are right at the top of the page and everything is marked in a nice and clear text.

<p align="center">
  <img src="https://nyanmark.github.io/nea/img/chrome_fzcnnqCEh7.png" width="550">
</p>

These are some responses I had gotten from some friends and family for my website. Overall I believe they found it easy to use. Additionally, I allowed comments so others can express a deeper opinion and this is what I got in response.


<p align="center">
  <img src="https://nyanmark.github.io/nea/img/chrome_xoyaKb8B5d.png" width="550">
</p>

- [x] Security users must log in to use the website. The website does have a secure login page which requires the users email and password and whenever the user tries to access the members area he is send back to the login page to make sure he is signed in.
    
<p align="center">
  <img src="https://nyanmark.github.io/nea/img/firefox_y5i2OvyDmV.png" width="550">
</p>

- [x] A intuative admin panel. I believe the admin panel is easy for anyone to use with large clear buttons indicating what is where, the forms are large again with clear buttons and the tables are labeled properly on each page.

<p align="center">
  <img src="https://nyanmark.github.io/nea/img/firefox_FTjrXTfPp0.png" width="550">
</p>

- [x] Page listing all the events with a sign up. My website does include this page, so I believe this objective has been met.

<p align="center">
  <img src="https://nyanmark.github.io/nea/img/firefox_SHRuq7B4Bc.png" width="550">
</p>

- [x] Events entered and accepted displayed in member page. My website also had this display in the members page therefore I believe this objective has been met.

<p align="center">
  <img src="https://nyanmark.github.io/nea/img/firefox_EAdLjaa2pR.png" width="550">
</p>

- [x] Image gallery to show off past events. There is a dynamic image gallery on the website.
    
<p align="center">
  <img src="https://nyanmark.github.io/nea/img/firefox_93QkFQjQRs.jpg" width="550">
</p>    

The admin page for image gallery. The IDs are not in order as you can delete images from the gallery when you want, and you can add images to the gallery. Additionally, you can edit images in the gallery, and the variables in the python Flask code will adjust the HTML code to scale up or down for more or less images.  Currently there is an issue due to the Home Page and the Gallery Main image being loaded from an array rather than a database causing the image not to always update. Therefore I plan to alter this code to use a text file or another database in the future.

<p align="center">
  <img src="https://nyanmark.github.io/nea/img/firefox_ahHeW9Nuuk.png" width="550">
</p>
    
- [x] Website hosted on the web accessible to anyone. This is also a complete objective as anyone in the world can access my site [at](https://mlweb.me). Unfortunately the current server it is running on is not so powerful meaning there is a arbitrary user limitation. However, I would like to note that at this current moment the code would need some adjustments to run optimally on a linux webserver. This is because I was programing in a windows environment.

- [x] Databases for fast access and indexing. The website does use a database as shown in the technical solution.

<p align="center">
  <img src="https://nyanmark.github.io/nea/img/pycharm64_JyC0YKwSSa.png" width="550">
</p>

- [x] Cheap to Run. As shown above the website can be run on a $2 VPS, and most likely will work very well on something priced around $10. 

- [x] Options for admin to set user limits for events. The admin can set a user limit when finalizing an event meaning there will be an x amount of users accepted for an event. This is done through choosing users with the least performances.

<p align="center">
  <img src="https://nyanmark.github.io/nea/img/firefox_MmewKSCcPX.png" width="550">
</p>

## Evaluation

One of the criteria through which I will be evaluating the success of my website is whether the objectives were met? Overall I believe the objectives were met for my project. Throughout my testing I've encoutered that most of the websites objectives have indeed been met however, it is not the full picture. For example some objectives even though met I believe are not fully at their ideal stage. To beging with the option for administrator to set event limits is not fully fledged as quoted by my client "it seems to be basic" which I can agree with and in future endevaours I would like to alter aspects to include an option to set specific sizes for the ammounts of specific voice types and have an easy print out for the admin as well as the users. Currently the admin would have to fetch the text file from the server with the list of users. Another response I had gotten from my client is even though the event has a date there is a lack of time and place for the event which is a shortcoming I had completely overlooked. This means there would be a need to add two additional collumns to the events database to inclode those.

Other aspects of my site such as functionality have been working well. This was affirmed to me by my client however he noted there could be an extra feature for a password reset as that would save the administrator a lot of time allowing users to reset passwords. I had personally chosen to ommit this feature at the time of coding as it would require a large amount of work to implement a properly working mailing system with proper email templates. However, this could have been something I had focused more on rather than focusing on the gallery which my client found to be a great feature however, lacking options to upload image rather than putting a URL instead.

Finally, The site is "clean and modern" as stated by my client. This was ideally what I was aiming for, something users can see as professional, clean and easy to use which I believe has been achieved through my use of bootstrap and the many resources available for it. Additionally the mobile support is exceptional due to the steps taken by the bootstrap team to do so by no means am I trying to take credit however, in evaluation I believe it was a great choice to use bootstrap as a web framwork for my website.

Overall, I am very happy with my website and the real main aspect is the python backend code, which achieves many things that I wanted it to achieve and without it, all those web pages would be static and boring however, python has allowed me to make the website dynamic with logic adding features such as logins, events and image gallerys which otherwise would have been impossible. Another thing it has allowed me to do is use template for admin and normal areas of the site allowing me to bypass the header and footer issue plaguing many sites as stated by my client through editing just a couple files. Therefore, I believe this project has been a success as a proof of concept for easy to use modern choir websites and with the right amount of time the python code can be adapted to have more pages and features. The only regret I may have is not having enough python specifically python web development knowledge before starting this as it would have opened so many more doors and take this project from a proof of conecept to a commercial level website that can be used by any choir in the world.
