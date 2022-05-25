from unicodedata import name
from flask import Flask, render_template

app=Flask(__name__)

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

if __name__=='__main__':
    app.run(debug=True)



