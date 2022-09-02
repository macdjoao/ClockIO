from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object('configs')

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from .models import Employee, Clock
from . import controllers_administrator
from . import controllers_employee
