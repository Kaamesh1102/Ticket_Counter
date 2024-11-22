from flask import Flask,render_template
from backend.models import db


app = Flask(__name__)

app=None

def setup_app():
    app=Flask(__name__)
    # sqlite connection is pending
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///ticket_show.sqlite3" #Having db file
    db.init_app(app) #Flask app connected to db(SQL alchemy)
    # api.init_app(app) #Flask app connect to apis
    app.app_context().push() #Direct access to other modules
    app.debug=True
    print("Ticket Show app is started...")

setup_app()

from backend.controllers import *

if __name__=="__main__":
    app.run()