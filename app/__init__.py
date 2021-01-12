# app/__init__.py
# third-party imports
from flask import Flask, render_template
from flask_migrate import Migrate

# local imports
from config import app_config
from app import models
from app import tables
from app import db
db = db.get_db()
Student = models.Student

#make timetable
def create_timetable(fname, lname):
    
    












#flask app
def create_app(config_name):
    app = Flask(__name__, template_folder="../templates/")
    app.config.from_object(app_config[config_name])
    db.init_app(app)

    migrate = Migrate(app, db)
    
    #routes
    @app.route('/')
    def index():
        return render_template("home.html")

    @app.route('/timetable-search', methods=['GET','POST'])
    def timetable_search():
        if request.method == "GET":
            return render_template("timetable-search.html")
        if request.method == "POST":
            return create_timetable(request.form['firstname'], request.form['lastname'])

    return app
app = create_app

