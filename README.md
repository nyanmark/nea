<header>
  <h1 align="center">COMPUTER SCIENCE NON EXAM ASSESMENT <br> CHOIR WEBSITE</h1>
</header>

<p align="center">
  <img src="https://nyanmark.github.io/nea/img/readme.png" width="200" height="200">
</p>




My client has approached me with an issue. He needs a system to track the performance’s of his choir. A few issues he has presented to me is that it needs to be accessible from the members home and needs to send out notifications to the members, therefore we had agreed on a website with an email system allow email notifications to be sent out to the choir members.

## Analysis

An issue my client had is how do you track all the events your choir is down, and how do you know who is going to participate in those events? This was the issue my client had approached me with therefore, we had to come up with a solution to his problem. To me the ideal seemed a website as it would provide access to anyone from anywhere to see what events are going on and sign up for them, this would also give myself and my client an opportunity for an notification system which sends data to the users email when they sign up. Overall this allowed my client and I to come up witha  sert of requirements listed below.

The requirements I had agreed on with my client would include:

    • A membership system
    • Tracking voice type (Soprano – Bass)
    • Tracking events
    • Storing choir membership
    • Event sign ups
    • Web page with secure login

This task would require a smart approach to reach all the requirements me and my client have discussed leading to some requirements I had come up with listed below. Furthermore considerations have to be taken on how to approach this issue of making an easily accessible website for all the choir member such as needing a domain for the website and a web server.  For the duration of this project I will be using a free subdomain and host the project on a web server I have until I hand it over to the client allowing him to set his own parameters for the website and email sending. 

All of the requirements above come with a few objectives:

    • A system which people with a lack of technical knowledge can use
    • Security users must log in to use the website
    • Overrides for the choir leader / admin 
    • Event selection and limits, system would output to the choir leader the voice types, quantity of those signed up for the event, the system would also chose those with the least performances if too many have opted in for an event.

Such requirements and objective have lead me to chose python as my program of choice using the flask library built into python allowing it to interface with html web pages. I have chosen python because I prefer it to and it provides me greater flexibility whilst setting up a system utilising a database to drive a web front end application. Furthermore it can easily integrate notification systems such as SMTP email sending and web hooks allowing it to notify choir members. I will be using uWSGI allowing python to interface with an Nginx web server allowing the web pages to be accessible from the internet on the choir website.

The database will be an integral part of my project as it would have to store all the members, logins and details for the system to function properly this would mean I have to employ proper table structure to make my database efficient. I have decided that there would be a table within the database for the members including their name, surname, email, password, voice type and quantity of events participated. Furthermore there will be a table for the events including the date, amount of slots and the location with another table for the event entries featuring the choir members who have entered having their first and last name, email and voice type. This will allow the choir master to see which people are in an event and how many of each voice type allowing him/her to alter the members as needed. Additionally the quantity of events participated which will be increased every time a user has been approved for an event and a notification has been sent out will be integral for the system in choosing users when there have been too many entries for an event allowing it to select those with the least performances.

For the web front end there will be simple html web pages with all the appropriate tabs. The web page list I had decided on is having an index home page, a registration page, a log in page, a personal info page allowing users to edit their email or password, an events page and an administrator page for the choir leader allowing them to edit user details, approve event sign ups, alter and overwrite members entered to an event and delete users. Furthermore the administration page will include SMTP setting for email sending allowing my customer to alter the email domain for his requirements.

The python back end will be central for the system to work as it would be running the link between the website and database and providing function for user notifications such as SMTP giving the customer the option of using the python or any external server for mail sending. This whole system would then interface with an Nginx allowing it to run a proper web conjunction with the python program. This may be considered unneccesary as flask runs a web server for you however to get much of the common features we rely on today such as ssl, sni, speed and versatility it would be ideal to run it using a web server such as Nginx or Apache2.

## Design

As mentioned previously I had chosen python for my website backend rather than common options such as PHP. Therefore I could simply split my code into 3 defined parts. The web, database and backend logic. The backend logic is the python part however the web part is done through the use of HTML and CSS finally the database part is done within python using Flask's (A python web driver alternative to django) SQLAlchemy package which allow easy interfacting between Flask and any database engine of choice, for testing I will be using sqlite3 database as it allows easy deletion and near instant access times however, I have added options into my code for using a MySQL database which providers better speed for larger deployment and has options such as high availability through clusters.

**Web**

The web design is done using Bootstrap CSS and JQuery JS located at [Here](https://github.com/twbs/bootstrap). This means that whilst I focused on writing HTML bulk of the work involved with writing CSS styling and Javascript was taken off my hands. Additionally using Flask has allowed me to create templates for a footer, header and navibar for the Member and Admin areas meaning each pages individual file only contained content unique to it. Using python has also allowed me to set variables and logic within the HTML code making me think of the most efficient decisions wether to do logic within python and then import the variable or do the code within the HTML. I have chosen to place the most important URL's within the header whilst keeping other essential however lesser important URL's in the footer.

**Database**

My website database consists of 4 tables. The initial database for the website I designed was only the users table to hold the websites members. That consisted of essential collumns such as the 

**Backend**

Python Flask backend.

## Technical 

Located at [GitHub](https://github.com/nyanmark/nea). Files to note for my project "main.py" and the contents of the "templates" folder. Everything else may be ignored. Please request access by sending me your GitHub username.

## Testing

To be done

## Evaluation

Waiting for response

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>
</body>
