import email
from email.message import Message
from multiprocessing import connection
from re import S
import smtplib
from unicodedata import name
from flask import Flask, render_template, Request, request
from flask_mysqldb import MySQL
import MySQLdb as db_connect
from flask_mail import Mail, Message
import random
from flask_sqlalchemy import SQLAlchemy

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

#Connecting to database using SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:database99@localhost:3306/flask_project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class reservations(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    date=db.Column(db.Date, nullable=False)
    table_mark=db.Column(db.String(10), nullable=False)
    name=db.Column(db.String(60), nullable=False)
    email=db.Column(db.String(60), nullable=False)
    remark=db.Column(db.String(255), nullable=False)

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

# Code for subscribing to newsletter
@app.route("/newsletter", methods=["POST"])
def subscribe_to_newsletter():
    # Adding users to newsletter_users table in database and sending confirmation mail to users
    email=request.form.get("email_newsletter")
    email_msg=Message("Alcatraz newsletter", sender="alcatrazclubzadar@gmail.com", recipients=[email])
    email_msg.body="Hvala vam što ste se pretplatili na naš newsletter. \n \n Alcatraz team"
    
    if not email:
        error_statement_newsletter="Morate unijeti e-mail adresu!"
        return render_template("index.html", error_statement_newsletter=error_statement_newsletter)
    else:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO newsletter_users (email) VALUES ('%s')" %(email))
        connection.commit()
        cursor.close()
        mail.send(email_msg)
        statement="Uspješno ste se pretplatili na naš newsletter."
        return render_template("index.html", statement=statement)

@app.route("/reservation/table", methods=["POST"])
def table_reservation():
    name=request.form.get("name")
    surname=request.form.get("surname")
    date=request.form.get("date")
    table_mark=request.form.get("table_mark")
    email_res=request.form.get("email_res")
    remark=request.form.get("remark")
    unique=False
    list_tables=[]
    while not unique:
        id=random.randint(100001,999999)
        exists = db.session.query(db.exists().where(reservations.id == id)).scalar()
        if not exists:
            unique=True
    exists2=bool(reservations.query.filter_by(date=date,table_mark=table_mark).first())
    for mark in db.session.query(reservations.table_mark).filter_by(date=date):
        list_tables.append(mark)
    if exists2:
        table_reserved_statement1="Stol "+ table_mark +" je već rezerviran za datum: "
        table_reserved_statement2="Lista zauzetih stolova: "
        table_reserved_statement3="Molimo odaberite neki drugi stol!"
        return render_template("reservation.html", table_reserved_statement1=table_reserved_statement1,table_reserved_statement2=table_reserved_statement2,table_reserved_statement3=table_reserved_statement3,list_tables=list_tables, name=name, surname=surname, remark=remark, email_res=email_res, date=date, date_res=date)
    else:
        reservation=reservations(id=id, date=date,table_mark=table_mark, name=name+" "+surname, email=email_res, remark=remark)
        db.session.add(reservation)
        db.session.commit()
        email_msg=Message("Alcatraz rezervacija", sender="alcatrazclubzadar@gmail.com", recipients=[email_res])
        email_msg.body="Uspješno ste rezervirali stol za dan "+str(date)+"\nVaš broj rezervacije: "+ str(id)+"\nMolimo vas da u klub dođete najkasnije do 23:30 inaće će vaša rezervacija biti poništena. Hvala" +"\nVaš Alcatraz team"
        mail.send(email_msg)
        successfully_reserved_statement="Uspješno ste rezervirali stol! Vaš broj rezervacije: "
        return render_template("reservation.html", successfully_reserved_statement=successfully_reserved_statement, id_res=id)

 

if __name__=='__main__':
    app.run(debug=True)





