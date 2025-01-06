from flask import Blueprint,render_template
import os

views = Blueprint('views',__name__)
base_path = os.path.dirname(__file__)

@views.route('/')
def home_site():
    
    return render_template('home.html')

