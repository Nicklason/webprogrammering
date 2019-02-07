'''xd'''
from flask import Blueprint, render_template

pages = Blueprint('index', __name__, url_prefix='/')

@pages.route('/')
def index():
    '''dx'''
    return render_template('index.html')
