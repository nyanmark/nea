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

Such requirements and objective have lead me to chose python as my program of choice using the flask library built into python allowing it to interface with html web pages. I have chosen python because I prefer it to and it provides me greater flexibility whilst setting up a system utilising a database to drive a web front end application. Furthermore it can easily integrate notification systems such as SMTP email sending and web hooks allowing it to notify choir members. I will be using uWSGI allowing python to interface with an Nginx web server allowing the web pages to be accessible from the internet on the choir website.

The database will be an integral part of my project as it would have to store all the members, logins and details for the system to function properly this would mean I have to employ proper table structure to make my database efficient. I have decided that there would be a table within the database for the members including their name, surname, email, password, voice type and quantity of events participated. Furthermore there will be a table for the events including the date, amount of slots and the location with another table for the event entries featuring the choir members who have entered having their first and last name, email and voice type. This will allow the choir master to see which people are in an event and how many of each voice type allowing him/her to alter the members as needed. Additionally the quantity of events participated which will be increased every time a user has been approved for an event and a notification has been sent out will be integral for the system in choosing users when there have been too many entries for an event allowing it to select those with the least performances.

For the web front end there will be simple html web pages with all the appropriate tabs. The web page list I had decided on is having an index home page, a registration page, a log in page, a personal info page allowing users to edit their email or password, an events page and an administrator page for the choir leader allowing them to edit user details, approve event sign ups, alter and overwrite members entered to an event and delete users. Furthermore the administration page will include SMTP setting for email sending allowing my customer to alter the email domain for his requirements.

The python back end will be central for the system to work as it would be running the link between the website and database and providing function for user notifications such as SMTP giving the customer the option of using the python or any external server for mail sending. This whole system would then interface with an Nginx allowing it to run a proper web conjunction with the python program. This may be considered unneccesary as flask runs a web server for you however to get much of the common features we rely on today such as ssl, sni, speed and versatility it would be ideal to run it using a web server such as Nginx or Apache2.

As mentioned previously I had chosen python for my website backend rather than common options such as PHP. Therefore I could simply split my code into 3 defined parts. The web, database and backend logic. The backend logic is the python part however the web part is done through the use of HTML and CSS finally the database part is done within python using Flask's (A python web driver alternative to django) SQLAlchemy package which allow easy interfacting between Flask and any database engine of choice, for testing I will be using sqlite3 database as it allows easy deletion and near instant access times however, I have added options into my code for using a MySQL database which providers better speed for larger deployment and has options such as high availability through clusters.

**Web**

The web design is done using Bootstrap CSS and JQuery JS located at [Here](https://github.com/twbs/bootstrap). This means that whilst I focused on writing HTML bulk of the work involved with writing CSS styling and Javascript was taken off my hands. Additionally using Flask has allowed me to create templates for a footer, header and navibar for the Member and Admin areas meaning each pages individual file only contained content unique to it. Using python has also allowed me to set variables and logic within the HTML code making me think of the most efficient decisions wether to do logic within python and then import the variable or do the code within the HTML. I have chosen to place the most important URL's within the header whilst keeping other essential however lesser important URL's in the footer. Some huge websites using boostrap [include](https://expo.getbootstrap.com/). Nearly 1/4 of the top 1 million websites are made with the help of bootstrap.

**Database**

My website database consists of 4 tables. The initial database for the website I designed was only the users table to hold the websites members. That consisted of essential collumns such as the 

**Backend**

Python Flask backend.

## Technical Solution 

If you would like to look at the files rather than screenshots they are located at [GitHub](https://github.com/nyanmark/nea). Files to note for my project "main.py" and the contents of the "templates" folder. Everything else may be ignored.

## Testing

To be done

## Evaluation

Waiting for response

