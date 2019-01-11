from flask import Flask, render_template
from pony.flask import Pony
from flask_login import LoginManager, login_required
from database import db, User, Company
from config import appConfig

app = Flask(__name__)
app.config.update(appConfig)

Pony(app)
db.bind(**app.config['PONY'])
db.generate_mapping(create_tables=True)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.User.get(id=user_id)


@app.route('/')
def homepage():
    return "this is the homepage. Work in progress."


@app.route('/login')
def login_screen():
    return "in this page you log in"


@app.route('/signup')
def signup_screen():
    return "in this page you create an account"
