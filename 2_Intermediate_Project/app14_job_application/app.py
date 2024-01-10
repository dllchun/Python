from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'myapplication123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    date = db.Column(db.DateTime)
    occupation = db.Column(db.String(80))



@app.route("/", methods=['GET', 'POST'])
def home():
    print(request.method)
    if request.method == 'POST':
        #Save to Datebase
        first_name = request.form['first_name']
        last_name = request.form["last_name"]
        email = request.form["email_address"]
        date = request.form["date"]
        date = datetime.strptime(date, '%Y-%m-%d')
        occupation = request.form["occupation"]
        result = Form(first_name=first_name, last_name=last_name, email=email, date=date, occupation=occupation)
        db.session.add(result)
        db.session.commit()
        flash("Your form was successfully submitted", "success")

        #Send email to admin

    return render_template("index.html")


if __name__ =="__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5001,)
