from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///epl.sqlite'

db = SQLAlchemy(app)

# Import routes and models AFTER app is created to avoid circular imports
from epl import routes  # noqa: E402
from epl import models  # noqa: E402
