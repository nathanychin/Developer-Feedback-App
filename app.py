from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)

ENV = 'prod' # Use dev if working in development environment

if ENV == 'dev':
    app.debug = True # Allows server to reload if in development     
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/python'
else:
    app.debug = False
    # Production database from heroku
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tjxlkgjwkahrvg:7c6468177be3d2732646077bbf2e4c8ff960b617e04fe8ef19604a14eff80e8e@ec2-54-156-121-142.compute-1.amazonaws.com:5432/dcp02v98mn0b7q'
    
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Clear warning

# Connect to database
db = SQLAlchemy(app)

# Model
class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key = True)
    customer = db.Column(db.String(200))
    developer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    # Initializer
    def __init__(self, customer, developer, rating, comments):
        self.customer = customer
        self.developer = developer
        self.rating = rating
        self.comments = comments

# When all forms are submitted, launch success page
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        developer = request.form['developer']
        rating = request.form['rating']
        comments = request.form['comments']
        # print(customer, developer, rating, comments)  Test to see if form data is submitted
        
        # Output alert if customer or developer is blank
        if customer == '' or developer == '': 
            return render_template('index.html', message='Please enter required fields')
        
        # Database filters to Feedback model's customer name.
        # If customer name in feedback has the amount of 0, customer does not exist in database yet
        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0: 
            data = Feedback(customer, developer, rating, comments)
            # Add data entered in fields
            db.session.add(data)
            # Commit data to database
            db.session.commit()
            # Send email after successful feedback
            send_mail(customer, developer, rating, comments)
            return render_template('success.html')
        # else return user to index
        return render_template('index.html', message='You have already submitted feedback')

# Index route - Beginning of form
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()