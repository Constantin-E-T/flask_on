from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.fields.core import StringField
from wtforms.validators import DataRequired

# Create a Flask Instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "my super seacret key"

# Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("What's your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")

# Create a route decorator(url)
@app.route('/')
#def index():
#return "<h1>Hello, World!</h1>"

def index():
    first_name = "john"
    # python list
    favorite_pizza = ["Pepperoni", "Cheese", "Mushrooms", 41]
    return render_template("index.html", 
        first_name=first_name,
        favorite_pizza = favorite_pizza)

@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)

# Create Custom Error Pages

@app.errorhandler(404)
def page_not_fund(e):
	return render_template("404.html"), 404

# Internal Server Error

@app.errorhandler(500)
def page_not_fund(e):
	return render_template("500.html"), 500

# Create Name Page

@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submited Succesfully!")
    return render_template("name.html",
        name = name,
        form = form)
