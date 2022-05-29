import email
from email.message import Message
from multiprocessing import connection
import smtplib
from unicodedata import name
from flask import Flask, render_template, Request, request
from flask_mysqldb import MySQL
import MySQLdb as db_connect
from flask_mail import Mail, Message

app=Flask(__name__)

host_name="localhost"
db_user="root"
db_password="database99"
db_name="flask_project"

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'alcatrazclubzadar@gmail.com'
app.config['MAIL_PASSWORD'] = 'ProgramiranjeZaWeb'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail=Mail(app)

#Creating a connection to the database
connection=db_connect.connect(host=host_name,user=db_user,password=db_password,database=db_name)

#Creating a connection cursor
cursor = connection.cursor()

#Executing SQL Statements
cursor.execute(''' CREATE TABLE IF NOT EXISTS newsletter_users(id BIGINT AUTO_INCREMENT PRIMARY KEY, email VARCHAR(60) NOT NULL UNIQUE) ''')
 
#Closing the cursor
cursor.close()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/gallery")
def gallery():
    return render_template('gallery.html')

@app.route("/aboutus")
def about_us():
    return render_template('aboutus.html')

@app.route("/reservation")
def reservation():
    return render_template('reservation.html')

@app.route("/events")
def events():
    return render_template('events.html')


# Sending e-mails using contact form from every page: homepage, aboutus page, events page, reservation page and gallery page
@app.route("/message", methods=["POST"])
def send_message_from_homepage():
    # Code for sending e-mail using contact form on the webpage
    email=request.form.get("email")
    msg=request.form.get("message")
    email_msg=Message("Alcatraz kontakt", sender=email, recipients=["alcatrazclubzadar@gmail.com"])
    email_msg.body=msg
    
    if not email or not msg:
        error_statement="Oba polja su obavezna!"
        return render_template("index.html", error_statement=error_statement, email=email, message=msg)
    else:
        mail.send(email_msg)
        success_statement="Poruka uspješno poslana! Javit ćemo vam se u najkraćem mogućem roku."
        return render_template("index.html", success_statement=success_statement)

@app.route("/aboutus/message", methods=["POST"])
def send_message_from_aboutus_page():
    # Code for sending e-mail using contact form on the webpage
    email=request.form.get("email")
    msg=request.form.get("message")
    email_msg=Message("Alcatraz kontakt", sender=email, recipients=["alcatrazclubzadar@gmail.com"])
    email_msg.body=msg
    
    if not email or not msg:
        error_statement="Oba polja su obavezna!"
        return render_template("aboutus.html", error_statement=error_statement, email=email, message=msg)
    else:
        mail.send(email_msg)
        success_statement="Poruka uspješno poslana! Javit ćemo vam se u najkraćem mogućem roku."
        return render_template("aboutus.html", success_statement=success_statement)

@app.route("/gallery/message", methods=["POST"])
def send_message_from_gallery_page():
    # Code for sending e-mail using contact form on the webpage
    email=request.form.get("email")
    msg=request.form.get("message")
    email_msg=Message("Alcatraz kontakt", sender=email, recipients=["alcatrazclubzadar@gmail.com"])
    email_msg.body=msg
    
    if not email or not msg:
        error_statement="Oba polja su obavezna!"
        return render_template("gallery.html", error_statement=error_statement, email=email, message=msg)
    else:
        mail.send(email_msg)
        success_statement="Poruka uspješno poslana! Javit ćemo vam se u najkraćem mogućem roku."
        return render_template("gallery.html", success_statement=success_statement)

@app.route("/reservation/message", methods=["POST"])
def send_message_from_reservation_page():
    # Code for sending e-mail using contact form on the webpage
    email=request.form.get("email")
    msg=request.form.get("message")
    email_msg=Message("Alcatraz kontakt", sender=email, recipients=["alcatrazclubzadar@gmail.com"])
    email_msg.body=msg
    
    if not email or not msg:
        error_statement="Oba polja su obavezna!"
        return render_template("reservation.html", error_statement=error_statement, email=email, message=msg)
    else:
        mail.send(email_msg)
        success_statement="Poruka uspješno poslana! Javit ćemo vam se u najkraćem mogućem roku."
        return render_template("reservation.html", success_statement=success_statement)

@app.route("/events/message", methods=["POST"])
def send_message_from_events_page():
    # Code for sending e-mail using contact form on the webpage
    email=request.form.get("email")
    msg=request.form.get("message")
    email_msg=Message("Alcatraz kontakt", sender=email, recipients=["alcatrazclubzadar@gmail.com"])
    email_msg.body=msg
    
    if not email or not msg:
        error_statement="Oba polja su obavezna!"
        return render_template("events.html", error_statement=error_statement, email=email, message=msg)
    else:
        mail.send(email_msg)
        success_statement="Poruka uspješno poslana! Javit ćemo vam se u najkraćem mogućem roku."
        return render_template("events.html", success_statement=success_statement)

if __name__=='__main__':
    app.run(debug=True)





