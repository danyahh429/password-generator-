"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app
import random

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template('index.html',
        title='Password Generator',
        year=datetime.now().year,)
@app.route("/generate/", methods=['POST'])
def generate_passowrd():
    #password generation
    letterSamples = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    password = "".join(random.sample(letterSamples,8))
    return render_template('index.html', password=password);
     

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template('contact.html',
        title='Contact Us!',
        year=datetime.now().year,
        message='You can visit us on these platforms:')

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template('about.html',
        title='The Purpose:',
        year=datetime.now().year,
        message='Ever been told your password is weak?')
